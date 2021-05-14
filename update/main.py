import json
import sys
from datetime import datetime
import requests
import os


def update():
    response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?key={os.environ['YOUTUBE_API_KEY']}&channelId={os.environ['CHANNEL_ID']}&part=id&order=date&maxResults=3")

    if response.status_code == 200:
        yt = response.json()
        with open('update/template.md', 'r') as file:
            filedata = file.read()

            filedata = filedata.replace('{{VIDEO_1_LINK}}', yt['items'][0]['id']['videoId']).replace(
                '{{VIDEO_2_LINK}}', yt['items'][1]['id']['videoId']).replace('{{VIDEO_3_LINK}}', yt['items'][2]['id']['videoId'])

            filedata = filedata.replace(
                '{{LAST_UPDATED_AT}}', datetime.now().strftime("%d %b %Y %H:%M"))

            # Write the file out again
            with open('README.md', 'w') as file:
                file.write(filedata)


def formatTime(item):
    return datetime.strptime(item['snippet']['publishTime'], "%Y-%m-%dT%H:%M:%Sz").strftime('%d-%m-%Y')


update()
