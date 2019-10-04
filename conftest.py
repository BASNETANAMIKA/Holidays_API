import requests
import builtins
import pytest
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import Config
import traceback


class APIUtils(object):

    @staticmethod
    def execute_get_request(request_url, params):
        session = requests.Session()
        # __builtins__['session'] = session
        try:
            print("Execute get request, url - [%s], params - [%s]" % (request_url, params))
            if params is not None:
                response = session.get(request_url, params=params, verify=False)
            else:
                response = session.get(request_url, verify=False)

            response.raise_for_status()
            if 'error' in response.text:
                raise Exception("Error in API response")
            else:
                pass

            print("Get request executed successfully.")
            print("cookies - [%s]" % session.cookies.get_dict())
            print("response status - [%s]" % response.status_code)
            print("response headers - %s" % response.headers)
            print("response content - %s" % response.text)

            return response
        except Exception as ex:
            traceback.print_exc()
            msg = str(ex) + '\n' + "Exception while executing get request. Request detail : " \
                                   "url - [%s], params - [%s]" % (request_url, params)
            raise Exception(msg)


@pytest.fixture(autouse=True, scope="session")
def initialise():
    __builtins__['baseurl'] = Config.HTTP_SCHEME + Config.BASE_URL
    __builtins__['api_url'] = __builtins__['baseurl'] + Config.API_VERSION
    __builtins__['api_key'] = Config.API_KEY
