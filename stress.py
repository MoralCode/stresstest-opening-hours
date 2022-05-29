
from opening_hours import OpeningHours
from datetime import date
import argparse

DATAFILE = "data/giscorps.txt"


parser = argparse.ArgumentParser(description='Stress test the opening hours parser with some real world data')
parser.add_argument('datafile', default="data/giscorps.txt", help='the path to the data file to use for this test')

args = parser.parse_args()

with open(args.datafile, "rb") as fp:
	success = 0
	fail = 0
	for line in fp:
		if not line:
			break
		# read as bytes and decode with unicode_escape to catch the escapes
		line = line.decode("unicode_escape")
	
		value = line.strip()#.encode('utf-8', 'ignore')
	
		try:

			OpeningHours.parse(line).json()
			success += 1
		except Exception as e:
			print("Could not parse: \"{}\"".format(value))
			fail += 1
	
	print("Results from {} on {}: {} lines total, {} successfully parsed, {} failed. {:.2f}% succeeded".format(args.datafile, date.today().isoformat(), success+fail, success, fail, (success/(success+fail))*100))