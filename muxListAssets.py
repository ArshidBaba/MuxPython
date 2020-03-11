import os 
import mux_python
from mux_python.rest import ApiException

#Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ.get('MUX_TOKEN_ID')
configuration.password = os.environ.get('MUX_TOKEN_SECRET')

#API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

#List Assets
print("Listing Assets: \n")
try:
    list_assets_response = assets_api.list_assets()
    # print(list_assets_response)
    for asset in list_assets_response.data:
        print('Asset ID: ' + asset.id)
        print('Status: ' + asset.status)
        print(asset.playback_ids)
        playback_ids = asset.playback_ids
        # print(type(playback_ids))
        for i in playback_ids:
            i = vars(i)
            print(i)
            print(type(i))
            id = i['_id']
            print(id)
        print('Duration: ' + str(asset.duration) + "\n")
        # print(asset, "\n")
except ApiException as e:
    print("Exception while calling AssetsApi->list_assets: %s\n" % e)