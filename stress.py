
from opening_hours import OpeningHours
from datetime import date

DATAFILE = "data/giscorps.txt"
with open(DATAFILE, "rb") as fp:
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
	
	print("Results from {} on {}: {} lines total, {} successfully parsed, {} failed. {:.2f}% succeeded".format(DATAFILE, date.today().isoformat(), success+fail, success, fail, (success/(success+fail))*100))