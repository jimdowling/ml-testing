## How to run the tests

Install the requirements.txt first:

sudo pip install -r requirements.txt

From this directory, the following will run the unit-tests:

python3 -m pytest


To run the e2e-tests, uncomment "# e2e-tests" in pytest.ini and then re-run:

python3 -m pytest
