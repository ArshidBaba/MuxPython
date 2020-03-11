import os
import mux_python
from mux_python.rest import ApiException
# import videosinfo
import pickle
import json

configuration = mux_python.Configuration()

#Configure HTTP basic authorization: accessToken
configuration.username = os.environ.get('MUX_TOKEN_ID')
configuration.password = os.environ.get('MUX_TOKEN_SECRET')

#create an instance of the API class
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))

with open('videosinfo.py', 'rb') as file:
    videos = pickle.loads(file.read())

print(videos)
playback_ids = {}
for name, url in videos.items():
    temp_id = name
    start = temp_id.find('_') + 1
    end = temp_id.find('.mp4', start)
    video_id = temp_id[start:end]
    print(video_id)
    create_asset_request = mux_python.CreateAssetRequest(
                                                    input=url,
                                                    playback_policy=["signed"],
                                                    passthrough="yt_video_id:"+video_id
                                                    ) 
    #create asset request
    print(create_asset_request)

    print(create_asset_request.input)
    try:
        #create an asset
        api_response = api_instance.create_asset(create_asset_request)
        print(api_response)

        d = vars(api_response.data)
        print(d)
        print(type(d))
      
        id = d['_playback_ids']
        print(id)
        p_id = vars(id[0])
        print(p_id['_id'])
        stream_url = 'https://stream.mux.com/'+p_id['_id']+'.m3u8'
        playback_ids[video_id] = stream_url
        
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset: %s\n" % e)

with open('playback_ids.txt', 'wb') as file:
    pickle.dump(playback_ids, file)