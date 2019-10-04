import json
import Config
import requests
import pytest
from conftest import APIUtils


@pytest.mark.parametrize("country, year, exp_holidays_count", [("IN", 2018, 27),("US", 2018, 83)])
def test_verify_holidays_count(country, year, exp_holidays_count):
    """
    https://holidayapi.com/v1/holidays
    :param exp_holidays_count: expected holidays count
    """

    request_url = __builtins__['api_url'] + "/holidays"
    api_call_params = {'key': __builtins__['api_key'], 'country': country, 'year': year}
    print("api_call_params %s" % api_call_params)

    response = APIUtils.execute_get_request(request_url, api_call_params)
    print("verify_chapters_count HTTP Response code is %s" % response.status_code)
    assert response.status_code == requests.codes['ok']

    holidays_details = json.loads(response.text)['holidays']
    print("Actual holidays count %s" % len(holidays_details))
    print("Expected holidays count %s" % exp_holidays_count)
    assert int(exp_holidays_count) == len(holidays_details)

@pytest.mark.parametrize("country_code", [("IN"),("ST")])
def test_fetch_country_name_for_code(country_code):
    """
    https://holidayapi.com/v1/holidays
    :param exp_holidays_count: expected holidays count
    """

    request_url = __builtins__['api_url'] + "/countries"
    api_call_params = {'key': __builtins__['api_key']}
    print("api_call_params %s" % api_call_params)

    response = APIUtils.execute_get_request(request_url, api_call_params)
    print("verify_chapters_count HTTP Response code is %s" % response.status_code)
    assert response.status_code == requests.codes['ok']

    all_country_details = json.loads(response.text)['countries']
    country_details = [country for country in all_country_details if country['code'] == country_code]
    print("country_details count %s" % country_details)
    assert len(country_details) == 1
    country_name = country_details[0]['name']
    print("country_name %s" % country_name)

