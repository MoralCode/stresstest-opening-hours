
from opening_hours import OpeningHours


with open("big list.txt") as fp:
	success = 0
	fail = 0
	for line in fp:
		if not line:
			break

		try:

			JsonOpeningHours.parse(line)
			success += 1
		except:
			print("Could not parse: \"{}\"".format(line.strip()))
			fail += 1
	
	print("{} lines total, {} successfully parsed, {} failed. {}% succeeded".format(success+fail, success, fail, success/(success+fail)))