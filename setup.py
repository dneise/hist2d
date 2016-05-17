from distutils.core import setup
setup(
    name='hist2d',
    version='0.0.1',
    description='projections and statistics on np.histogram2d results',
    url='https://github.com/dneise/hist2d',
    author='Dominik Neise',
    author_email='neised@phys.ethz.ch',
    license='MIT',
    packages=['hist2d'],
    install_requires=[
        'numpy',
    ],
    zip_safe=True,
)
