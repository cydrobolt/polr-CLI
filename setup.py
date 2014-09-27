from distutils.core import setup

setup(
    name='polr_cli',
    version='1.0.0',
    author='Chaoyi Zha',
    author_email='summermontreal@gmail.com',
    packages=['polr_cli'],
    url='http://github.com/Cydrobolt/polr-cli',
    license=''' Copyright (c) 2014 Chaoyi Zha
Copyright (C) 2014 Chaoyi Zha

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA''',
    description='Polr Command-Line Interface',
    long_description=open('README.md').read(),
    install_requires=["argparse", "urllib2"]
)
