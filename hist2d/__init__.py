"""
"""

import numpy as np

def bincenter(bins):
    return (bins[1:] + bins[:-1]) / 2.

class Hist2d:
    def __init__(self, H, bx, by):
        self.e = H  # e : for entries
        self.bx = bx
        self.by = by
        self.cx = bincenter(bx)
        self.cy = bincenter(by)



def _method_mode(H):
    return H.cy[H.e.argmax(axis=1)]

def _method_mean(H):
    return (H.e * H.cy).sum(axis=1) / H.e.sum(axis=1)

def _method_std(H):
    m = _method_mean(H)[:, np.newaxis]
    s = np.sqrt(
            (
                H.e * (H.cy[np.newaxis,:] - m)**2
            ).sum(axis=1) / (H.e.sum(axis=1) - 1)
        )
    return s

methods = {
    "mean": _method_mean,
    "mode": _method_mode,
    "std": _method_std,
}

def profile_along_x(H, bx=None, by=None, method="mean"):
    if bx is not None and by is not None:
        H = Hist2d(H, bx, by)

    method = methods[method]
    return H.cx, method(H)


if __name__ == "__main__":

    x = np.linspace(0, 7, 100)
    y = 3 + 0.4*x

    x = x.repeat(3000)
    y = y.repeat(3000)

    y += np.random.normal(scale=y/5, size=y.shape)

    import matplotlib.pyplot as plt

    H, bx , by, img = plt.hist2d(x,y, bins=[
        np.linspace(-1, 8, 51),
        np.linspace(-1, 10, 101),
        ], cmap="viridis")

    H = Hist2d(H, bx, by)

    mode = _method_mode(H)
    mean = _method_mean(H)
    std = _method_std(H)
    plt.plot(H.cx, mode, 'bo')
    plt.errorbar(x=H.cx, y=mean, yerr=std, fmt="ro")
    
    plt.ion()
    plt.show()