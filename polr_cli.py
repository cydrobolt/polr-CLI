#!/usr/bin/env python

#######################################################
#	Polr CLI; http://github.com/Cydrobolt/polr-cli    #
#	[c] Copyright 2014 Chaoyi Zha (cydrobolt)         #
#######################################################
import argparse, urllib2, sys, os
from urllib2 import *

# If you have an API key, set it below; otherwise, it will connect
# to the public API, which has an 8 link/min quota
apikey = ''

# Enable colors? Colors should work on most UNIX terminals, but does not work on Windows.
colors = True
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
def get_bv(url):
	try:
		bv = find_between(url, "http://polr.me/", "")
		return bv
	except:
		return "error"
parser = argparse.ArgumentParser(description='Shorten and lookup URLs using the Polr CLI.')

parser.add_argument('value', metavar='value', type=str, help='the link to shorten or the link ending to look up.')
parser.add_argument('--version', '-v', action='version', version='Polr CLI 1.0.1 http://github.com/polr-cli')
parser.add_argument('--shorten', '-s', action='store_true', default='shorten', help = 'shorten an URL using Polr')
parser.add_argument('--lookup', '-l', action='store_true', default = 'lookup', help = 'lookup an URL using Polr')

args = parser.parse_args()


if args.lookup == True:
	action = 'lookup'
else:
	action = 'shorten'

value = args.value

if action == "shorten":
	if apikey == '':
		try:
			#public_api = urllib2.urlopen('http://polr.me/publicapi.php?action=shorten&url='+value)
			#response = public_api.read()

			request = urllib2.Request('http://polr.me/publicapi.php?action=shorten&url='+value)
			opener = urllib2.build_opener()
			request.add_header('User-Agent', '0.Polr CLI/1.0.0 +http://github.com/Cydrobolt/polr-cli')
			response = opener.open(request).read()
		except urllib2.HTTPError,e:
			if colors == True:
				print "\033[91m"
			if "401" in e:
				print "Error: Something went wrong. :( [401 Unauthorized]"
			elif "400" in e:
				print "Error: Hmmm. Something went wrong with the CLI. Please report this bug at http://github.com/Cydrobolt/polr-cli"
			elif "503" in e:
				print "Error: You are either exeeding your quota or Polr is currently experiencing problems."
			else:
				print "Unknown Error: %s" % e
			print "\033[0m";sys.exit()
		print "\033[0m"

		if "http://polr.me" not in str(response):
			if response == "Hey, slow down! Exeeding your perminute quota. Try again in around a minute.":
				print "Error: You are exeeding your minute quota of 8 links per min. Try again later."
			print "Error: " + response
			print "\033[0m";sys.exit()
		else:
			if colors == True:
				print "\033[94mShortened: "+response+"\n\n\033[94mStats: http://polr.me/+%s" % get_bv(response)
			else:
				print "Shortened: "+response+"\n\nStats: http://polr.me/+%s" % get_bv(response)
			print "\033[0m"
	elif len(apikey) > 3:
		try:
			request = urllib2.Request("http://polr.me/api.php?apikey={0}&action=shorten&url={1}".format(apikey, value))
			opener = urllib2.build_opener()
			request.add_header('User-Agent', 'Polr CLI/1.0.0 +http://github.com/Cydrobolt/polr-cli')
			response = opener.open(request).read()
		except urllib2.HTTPError, e:
			if colors == True:
				print "\033[91m"
			if "401" in e:
				print "Error: Your API is invalid. Please verify it is correct and try again."
			elif "400" in e:
				print "Error: The URL provided or API key are invalid or empty."
			elif "503" in e:
				print "Error: You are either exeeding your quota or Polr is currently experiencing problems."
			else:
				print "Unknown Error: %s" % e
			print "\033[0m";sys.exit()


		if "http://polr.me" not in str(response):
			if colors == True:
				print "\033[91m"
			if response == "Hey, slow down! Exeeding your perminute quota. Try again in around a minute.":
				print "Error: You are exeeding your minute quota. Try again later."
			elif response == "401 Unauthorized":
				print "Invalid API key"
				print "\033[0m";sys.exit()
			print "Error: " + response
			print "\033[0m";sys.exit()

		else:
			if colors == True:
				print "\033[94mShortened: "+response+"\n\n\033[94mStats: http://polr.me/+%s" % get_bv(response)
			else:
				print "Shortened: "+response+"\n\nStats: http://polr.me/+%s" % get_bv(response)
		print "\033[0m"
	else:
		if colors == True:
			print "\033[91m"
		print "We tried to use the API key you specified, but it was invalid. If you do not have an API key, please set apikey to ''."
		print "\033[0m";sys.exit()
elif action == 'lookup':
	global color
	if "polr.me" in str(value):
		if colors == True:
			print "\033[91mPlease only enter the ending of the short URL. (i.e polr.me/\033[92mjustenterthis\033[91m)."
			print "\033[0m";sys.exit()
		else:
			print "Please only enter the ending of the short URL. (i.e polr.me/justenterthis)"
			print "\033[0m";sys.exit()
		print "\033[0m"

	try:
		request = urllib2.Request('http://polr.me/publicapi.php?action=lookup&url='+value)
		opener = urllib2.build_opener()
		request.add_header('User-Agent', 'Polr CLI/1.0.0 +http://github.com/Cydrobolt/polr-cli')
		response = opener.open(request).read()
		if colors == True:
			print "\033[94mLong URL: "+response+"\n\n\033[94mStats: http://polr.me/+%s" % value
		else:
			print "Long URL: "+response+"\n\nStats: http://polr.me/+%s" % value
		print "\033[0m"
	except urllib2.HTTPError, e:
		if colors == True:
			print "\033[91m"
		if "404" in e:
			print "The link ending you tried to look up was not found; try again."
			print "\033[0m";sys.exit()
		if "403" in e:
			print "403 Forbidden; There was an error connecting to the server. Either you are querying Polr too quickly, your IP is blacklisted, or there was a bug in the CLI."
			print "\033[0m";sys.exit()
		else:
			print "An error has occured. Make sure the link ending you are looking up is valid, or report this bug at http://github.com/Cydrobolt/polr-cli"
	print "\033[0m";sys.exit()
