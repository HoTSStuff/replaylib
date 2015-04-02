import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

VERSION = '0.0.1'

DEPENDENCYLINKS = []
REQUIRES = []


setup(
    name='replaylib',
    description='Parse Heroes of the Storm Replays',
    keywords='hots',
    version=VERSION,
    author='Bruce Stringer',
    author_email='bruce.stringer.it@gmail.com',
    dependency_links=DEPENDENCYLINKS,
    install_requires=REQUIRES,
    # TODO(bs): Update this once we have an updated
    entry_points={
        'console_scripts': [
            'replaylib=replaylib.sample:main'
        ]
    },
    tests_require=['tox'],
    packages=find_packages(exclude=['bin', 'ez_setup']),
    include_package_data=True,
    license='Apache License (2.0)',
    classifiers=["Programming Language :: Python"],
    url='http://github.com/HoTSStuff/replaylib'
)