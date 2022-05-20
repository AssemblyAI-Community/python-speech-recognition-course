import json
from yt_extractor import get_video_info, get_audio_url
from api_03 import save_transcript


def save_video_sentiments(url):
    video_info = get_video_info(url)
    url = get_audio_url(video_info)
    if url:
        title = video_info['title']
        title = title.strip().replace(" ", "_")
        title = "data/" + title
        save_transcript(url, title, sentiment_analysis=True)

if __name__ == "__main__":
    # save_video_sentiments("https://youtu.be/e-kSGNzu0hM")
    
    with open("data/iPhone_13_Review:_Pros_and_Cons_sentiments.json", "r") as f:
        data = json.load(f)
    
    positives = []
    negatives = []
    neutrals = []
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)
        
    n_pos = len(positives)
    n_neg  = len(negatives)
    n_neut = len(neutrals)

    print("Num positives:", n_pos)
    print("Num negatives:", n_neg)
    print("Num neutrals:", n_neut)

    # ignore neutrals here
    r = n_pos / (n_pos + n_neg)
    print(f"Positive ratio: {r:.3f}")

