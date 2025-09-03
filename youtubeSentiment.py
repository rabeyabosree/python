from googleapiclient.discovery import build
from textblob import TextBlob
import matplotlib.pyplot as plt

api_key = ''
video_id = ''

youtube = build('youtube', 'v3', developerKey = api_key)

comments = []
request = youtube.commentThreads().list(
    part = 'snippet',
    videoId = video_id,
    maxResult = 40,
    textFormet = 'plainText'
)

response = request.execute()

for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comments.append(comment)

print(comments[:4])

result = {'Positive': 0, 'Negative': 0, "Neutral": 0}

for c in comments:
    analysis = TextBlob(c)
    if analysis.sentiment.polarity > 0:
        result['Positive'] += 1
    elif analysis.sentiment.polarity < 0:
        result['Negative'] += 1
    else:
        result['Neutral'] += 1

print(result)


plt.bar(result.keys(), result.values(), color=["green", "red", "gray"])
plt.title("Youtube comment sentiment analysis")
plt.show()