
from opening_hours import OpeningHours
from datetime import date, datetime
import argparse
from pathlib import Path
import csv

DATAFILE = "data/giscorps.txt"


parser = argparse.ArgumentParser(description='Stress test the opening hours parser with some real world data')
parser.add_argument('datafile', default="data/giscorps.txt", help='the path to the data file to use for this test')

parser.add_argument('--results', default= "results.csv", help='the path to a csv file to use for writing the results to')
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
	percent = "{:.2f}".format((success/(success+fail))*100)
	print("Results from {} on {}: {} lines total, {} successfully parsed, {} failed. {}% succeeded".format(args.datafile, date.today().isoformat(), success+fail, success, fail, percent))

	if args.results:
		filepath = Path(args.results)
		createHeader = False
		mode = "a"
		if not filepath.exists():
			mode = "w"
			createHeader = True

		with open(args.results, mode) as results:
			fieldnames = ['timestamp', 'datafile', 'total_lines', 'lines_succeeded', 'lines_failed', 'success_rate']
			writer = csv.DictWriter(results, fieldnames=fieldnames)
			if createHeader:
				writer.writeheader()
			writer.writerow({
				'timestamp': datetime.now().isoformat(),
				'datafile': args.datafile,
				'total_lines': success+fail,
				'lines_succeeded': success,
				'lines_failed': fail,
				'success_rate': percent
				})
