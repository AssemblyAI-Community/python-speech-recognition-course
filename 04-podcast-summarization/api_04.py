import requests
import json
import time
from api_secrets import API_KEY_ASSEMBLYAI, API_KEY_LISTENNOTES
import pprint


transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers_assemblyai = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

listennotes_episode_endpoint = 'https://listen-api.listennotes.com/api/v2/episodes'
headers_listennotes = {
  'X-ListenAPI-Key': API_KEY_LISTENNOTES,
}



def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    response = requests.request('GET', url, headers=headers_listennotes)

    data = response.json()
    # pprint.pprint(data)

    episode_title = data['title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    audio_url = data['audio']
    return audio_url, thumbnail, podcast_title, episode_title

def transcribe(audio_url, auto_chapters):
    transcript_request = {
        'audio_url': audio_url,
        'auto_chapters': auto_chapters
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers_assemblyai)
    pprint.pprint(transcript_response.json())
    return transcript_response.json()['id']


def poll(transcript_id, **kwargs):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers_assemblyai)

    if polling_response.json()['status'] == 'completed':
        filename = transcript_id + '.txt'
        with open(filename, 'w') as f:
            f.write(polling_response.json()['text'])

        filename = transcript_id + '_chapters.json'
        with open(filename, 'w') as f:
            chapters = polling_response.json()['chapters']

            data = {'chapters': chapters}
            for key, value in kwargs.items():
                data[key] = value

            json.dump(data, f, indent=4)

        print('Transcript saved')
        return True
    return False


def get_transcription_result_url(url, auto_chapters, audio_url, thumbnail, podcast_title,
                  episode_title):
    transcribe_id = transcribe(url, auto_chapters)
    while True:
        result = poll(transcribe_id, audio_url=audio_url, thumbnail=thumbnail, podcast_title=podcast_title,
                  episode_title=episode_title)
        if result:
            break
            
        print("waiting for 60 seconds")
        time.sleep(60)



def pipeline(episode_id):
    audio_url, thumbnail, podcast_title, episode_title = get_episode_audio_url(episode_id)
    get_transcription_result_url(audio_url, auto_chapters=True, audio_url=audio_url, thumbnail=thumbnail, podcast_title=podcast_title,
                  episode_title=episode_title)


if __name__ == '__main__':
   pipeline("20bf194224434ebbba8462ea8136cc3d")