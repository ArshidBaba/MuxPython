import os
import mux_python
from mux_python.rest import ApiException

configuration = mux_python.Configuration()

configuration.username = os.environ.get('MUX_TOKEN_ID')
configuration.password = os.environ.get('MUX_TOKEN_SECRET')

api_instance = mux_python.URLSigningKeysApi(mux_python.ApiClient(configuration))

try:
    api_response = api_instance.create_url_signing_key()
    print(api_response)
except ApiException as e:
    print("Exception when calling URLSigningKeysApi->create_url_signing_key: %s\n" % e)