import streamlit as st
import glob
import json
from api_04 import save_transcript

st.title("Podcast Summaries")

json_files = glob.glob('*.json')

episode_id = st.sidebar.text_input("Episode ID")
button = st.sidebar.button("Download Episode summary", on_click=save_transcript, args=(episode_id,))


def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
        
    return start_t


if button:
    filename = episode_id + '_chapters.json'
    print(filename)
    with open(filename, 'r') as f:
        data = json.load(f)

    chapters = data['chapters']
    episode_title = data['episode_title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast_title']
    audio = data['audio_url']

    st.header(f"{podcast_title} - {episode_title}")
    st.image(thumbnail, width=200)
    st.markdown(f'#### {episode_title}')

    for chp in chapters:
        with st.expander(chp['gist'] + ' - ' + get_clean_time(chp['start'])):
            chp['summary']