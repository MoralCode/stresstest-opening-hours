## Opening Hours Stress Test

Because the [parse-opening-hours](https://github.com/MoralCode/parse-opening-hours) library was created to parse large datasets of scraped COVID vaccination site opening hours for the [vaccinatethestates ingest pipeline](https://github.com/caVaccineInventory/vaccine-feed-ingest/), there was plenty of sample data available to test with.

this repository serves as a basica usage example and stress-test for this library by feeding it with large amounts of data from the massive GISCorps database of covid vaccination sites.

This is real world data with real-world quirks that parse-opening-hours hopes to take care of so more variations of opening hours can be supported.

## Usage

Just `pipenv install` and `pipenv run python3 ./stress.py`. you can also pass an optional path to a file containing dates to parse, one per line. The default is to use the file at `data/giscorps.txt`

there is also a `--results` flag that can be used to passa  filepath to a csv file in which to store the results.