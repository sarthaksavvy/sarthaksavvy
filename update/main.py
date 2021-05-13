
import sys
from datetime import datetime


def update():
    with open('update/template.md', 'r') as file:
        filedata = file.read()

        if(len(sys.argv) > 1):
            yt = eval(sys.argv[1])
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
