
from googleapiclient.discovery import build

api_key='xxxxxxxxxxxxxxxx'
youtube=build('youtube','v3',developerKey=api_key)
request=youtube.channels().list(part='statistics',forUsername='shabanafathimascse4754')
response=request.execute()
print(response)
