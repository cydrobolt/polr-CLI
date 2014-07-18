Polr-CLI
========

####Polr command-line interface (CLI)

http://polr.cf

http://github.com/Cydrobolt/polr-PaaS


#####How to install:

 - Edit polr-cli.py and set your API key (or leave blank if you don't have one)
 - If you are on Windows or on a system that does not support colors in the terminal, then set it to False, otherwise, leave it to True
 - Run `setup.py install`
 - Run `polr-cli` by running `python polr-cli.py <args>`

#####How to use `polr-cli`:
```
usage: polr-cli.py [-h] [--version] [--shorten] [--lookup] value

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
