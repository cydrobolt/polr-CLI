Polr-CLI
========

####Polr command-line interface (CLI)

http://polr.me

http://github.com/Cydrobolt/polr-PaaS


#####How to install:

 - Edit polr-cli.py and set your API key (or leave blank if you don't have one)
 - If you are on Windows or on a system that does not support colors in the terminal, then set it to False, otherwise, leave it to True
 - Run `setup.py install`
 - Run `polr-cli` by running `python polr-cli.py <args>`

#####How to use `polr-cli`:
You can use `polr` if `polr-cli` is in `/usr/local/bin/` and `sudo ln -s /path/to/polr-cli/polr .` was run.
```
usage: ./polr [-h] [--version] [--shorten] [--lookup] value

Shorten and lookup URLs using the Polr CLI.

positional arguments:
  value          the link to shorten or the link ending to look up.

optional arguments:
  -h, --help     show this help message and exit
  --version, -v  show program's version number and exit
  --shorten, -s  shorten an URL using Polr
  --lookup, -l   lookup an URL using Polr
```

Found a bug? Create an issue, or send a pull request.
Need help? Join us at #polr on irc.freenode.net:6667

Polr command-line interface
    Copyright (C) 2014 Chaoyi Zha

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
