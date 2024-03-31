from googleapiclient.discovery import build
import matplotlib.pyplot as plt


api_key='xxxxxxxxxxxxxxxxxxxxxx'
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(part='statistics', forUsername='shabanafathimascse4754') // can add any other valid yt user name
response = request.execute()
print(response)


statistics = response['items'][0]['statistics']
subscriber_count = int(statistics['subscriberCount'])
view_count = int(statistics['viewCount'])
video_count = int(statistics['videoCount'])


print('Subscriber Count:', subscriber_count)
print('Total Views:', view_count)
print('Total Videos:', video_count)


labels = ['Subscribers', 'Total Videos']
sizes = [subscriber_count, video_count]
colors = ['lightblue', 'lightgreen']
explode = (0.1, 0) 

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal') 
plt.title('YouTube Channel Statistics')
plt.show()
