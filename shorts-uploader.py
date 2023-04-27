from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Define the credentials object
creds = service_account.Credentials.from_service_account_file('client_secret.json')

# Define the YouTube API object
youtube = build('youtube', 'v3', credentials=creds)

# Define the path to the video file
video_path = 'poutput/day6.mp4'

day_idx = 6

# Define the request body for the video
request_body = {
    'snippet': {
        'title': f'1 minute Korean expresssion day{day_idx} #shorts',
        'description': 'Wanna learn Korean voca and expression in 1 min? Try this!',
        'tags': ['Shorts', 'Korean', 'koreandrama', 'koreanlanguage', 'koreanvocabulary', 'koreanfood', 'learningkorean'],
        'categoryId': 22
    },
    'status': {
        'privacyStatus': 'public',
        'selfDeclaredMadeForKids': False,
    }
}



try:
    # Upload the video
    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=MediaFileUpload(video_path)
    ).execute()

    print(f'Video uploaded: {response["id"]}')
except HttpError as error:
    print(f'An error occurred: {error}')
