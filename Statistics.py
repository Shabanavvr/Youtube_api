import matplotlib.pyplot as plt
from googleapiclient.discovery import build


def get_channel_statistics(api_key, username):
   
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(part='statistics', forUsername=username)
    response = request.execute()
    return response['items'][0]['statistics']

def plot_statistics(statistics):
    
    labels = list(statistics.keys())
    values = [int(statistics[label]) for label in labels]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Statistics')
    plt.ylabel('Values')
    plt.title('YouTube Channel Statistics')
    plt.show()

def main():
    api_key='xxxxxxxxxxxxxxxxxxx'
    username = 'shabanafathimascse4754'

    statistics = get_channel_statistics(api_key, username)
    print('Channel Statistics:', statistics)

    plot_statistics(statistics)

if __name__ == '__main__':
    main()
