"""
ISSH/RDP command line tool for EC2
"""
from setuptools import find_packages, setup
from pip.req import parse_requirements
import pip

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=pip.download.PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name='connect-ec2',
    version='0.1.0',
    url='https://github.com/jamiegs/connect-ec2',
    license='BSD',
    author='Jamie Snell',
    author_email='jgsnell@gmail.com',
    description='ISSH/RDP command line tool for EC2',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=reqs,
    setup_requires=[
        'pytest-runner'
        ],
    tests_require=[
        'pytest'
        ],
    entry_points={
        'console_scripts': [
            'connect-ec2 = connect_ec2.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
