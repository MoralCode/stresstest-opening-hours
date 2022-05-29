
from opening_hours import OpeningHours


DATAFILE = "data/giscorps.txt"
with open(DATAFILE, "rb") as fp:
	success = 0
	fail = 0
	for line in fp:
		if not line:
			break

		try:

			OpeningHours.parse(line).json()
			success += 1
		except:
			print("Could not parse: \"{}\"".format(line.strip()))
			fail += 1
	
	print("Results from {}: {} lines total, {} successfully parsed, {} failed. {}% succeeded".format(DATAFILE, success+fail, success, fail, (success/(success+fail))*100))