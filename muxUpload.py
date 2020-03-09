import os 
import mux_python
from mux_python.rest import ApiException

#Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

#API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

#List Assets
print("Listing Assets: \n")
try:
    list_assets_response = assets_api.list_assets()
    for asset in list_assets_response.data:
        print('Asset ID: ' + asset.id)
        print('Status: ' + asset.status)
        print('Duration: ' + str(asset.duration) + "\n")
except ApiException as e:
    print("Exception while calling AssetsApi->list_assets: %s\n" % e)