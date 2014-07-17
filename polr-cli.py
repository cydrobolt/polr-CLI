#!/usr/bin/env python

#######################################################
#	Polr CLI; http://github.com/Cydrobolt/polr-cli    #
#	[c] Copyright 2014 Chaoyi Zha (cydrobolt)         #
#######################################################
import argparse, urllib2, sys
from urllib2 import *

# If you have an API key, set it below; otherwise, it will connect
# to the public API, which has an 8 link/min quota
apikey = ''


parser = argparse.ArgumentParser(description='Shorten and lookup URLs using the Polr CLI.')

parser.add_argument('value', metavar='value', type=str, help='the link to shorten or the link ending to look up.')
parser.add_argument('--version', '-v', action='version', version='Polr CLI 0.1 http://github.com/polr-cli')
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
			#public_api = urllib2.urlopen('http://polr.cf/publicapi.php?action=shorten&url='+value)
			#response = public_api.read()

			request = urllib2.Request('http://polr.cf/publicapi.php?action=shorten&url='+value)
			opener = urllib2.build_opener()
			request.add_header('User-Agent', 'Polr CLI/0.1 +http://github.com/Cydrobolt/polr-cli')                                  
			response = opener.open(request).read()
		except urllib2.HTTPError,e :
			print "There was an error: %s; either your request was invalid, you are exeeding your quota, or there was an error." % e
			sys.exit()

		if "http://polr.cf" not in str(response):
			if response == "Hey, slow down! Exeeding your perminute quota. Try again in around a minute.":
				print "Error: You are exeeding your minute quota of 8 links per min. Try again later."
			print "Error: " + response
			sys.exit()
		else:
			print "Shortened: " + response
	elif len(apikey) > 3:
		try:
			request = urllib2.Request("http://polr.cf/api.php?apikey={0}&action=shorten&url={1}".format(apikey, value))
			opener = urllib2.build_opener()
			request.add_header('User-Agent', 'Polr CLI/0.1 +http://github.com/Cydrobolt/polr-cli')                                  
			response = opener.open(request).read()
		except urllib2.HTTPError, e:
			print "There was an error: %s; either your request was invalid, you are exeeding your quota, or there was an error." % e
			sys.exit()


		if "http://polr.cf" not in str(response):
			if response == "Hey, slow down! Exeeding your perminute quota. Try again in around a minute.":
				print "Error: You are exeeding your minute quota. Try again later."
			elif response == "401 Unauthorized":
				print "Invalid API key"
				sys.exit()
			print "Error: " + response
			sys.exit()
		else:
			print "Shortened: " + response
	else:
		print "We tried to use the API key you specified, but it was invalid. If you do not have an API key, please set apikey to ''."
		sys.exit()
elif action == 'lookup':
	pass