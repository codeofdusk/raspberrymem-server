    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The server side of a free memory aid for seniors, powered by Raspberry Pi)',
    'author': 'Bill Dengler',
    'url': 'http://launchpad.net/raspberrymem-server',
    'download_url': 'http://launchpad.net/raspberrymem-server',
    'author_email': 'billkd2008@gmail.com',
    'version': '1.0 pre',
    'install_requires': [],
    'packages': ['raspberrymem-server'],
    'scripts': [],
    'name': 'raspberrymem-server'
}

setup(**config)
