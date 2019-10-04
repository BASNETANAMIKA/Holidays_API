# Holidays_API
test framework for REST API testing using pytest

test_holidays.py is the main test suite.It contains 2 test cases in parameterized format:
1. Verify Holidays count for country and year.
2. Fetch country name for country code provided.

##**Technology / Frameworks used:**

  1. python 3
  2. pytest
  3. pytest-html
  4. requests
  
##**Installation:**

`git clone https://github.com/BASNETANAMIKA/Holidays_API.git && cd Holidays_API`

`pip install -r requirements.txt`

##**How to Run tests:**

`cd <path to Holidays_API>`

`pytest`

OR

`pytest --html=report.html`
