import requests
from api_02 import *

filename = "Natural Language Processing Short.m4a"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')