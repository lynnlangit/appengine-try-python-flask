import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity

my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=15)
gcs.set_default_retry_params(my_default_retry_params)


GOOGLE_STORAGE = 'gs'
# URI scheme for accessing local files.
LOCAL_FILE = 'TestPhoto.png'

CLIENT_ID = '137213855825-jk2bag61sp8ha60t5tt7g6cuci7j5ibh.apps.googleusercontent.com'
CLIENT_SECRET = 'notasecret'
gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)

BUCKET_NAME = 'virtualproctor'
uri = boto.storage_uri(BUCKET_NAME+'/'+LOCAL_FILE,GOOGLE_STORAGE)
uri.new_key().set_contents_from_file('assets/'+LOCAL_FILE)
print(uri.object_name)


# @endpoints.api(name='screenshotsApi',version='v1',
#                description='Screenshots API')
# class Screenshots(remote.Service):
#     pass
#
# class ScreenshotRequestMessage(messages.Message):
#     pass
#
# class ScreenshotResponseMessage(messages.Message):
#     pass