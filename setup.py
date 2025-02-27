from imagecleaner._version import __version__ as version
import os


try:
    from setuptools import find_packages, setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import find_packages, setup


def readfile(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), filename)) as f:
            return f.read()
    except (IOError, OSError):
        return ''


install_reqs = [
    'Pillow>=8.1.0',
]


setup(
    name='imagecleaner',
    description='Remove duplicated images from a path',
    long_description=readfile('README.rst'),
    version=version,
    url='https://github.com/Kjwon15/image-cleaner',
    download_url='https://github.com/Kjwon15/image-cleaner/releases',
    author='Kjwon15',
    author_email='kjwonmail@gmail.com',
    entry_points={
        'console_scripts': [
            'image-cleaner = imagecleaner.cli:main'
        ]
    },
    packages=find_packages(),
    install_requires=install_reqs,
)
