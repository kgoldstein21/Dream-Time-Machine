from __future__ import unicode_literals
import youtube_dl

'''
This file uses a youtube video to download an mp3 file
'''


class MyLogger(object):

    #This helps tell you what goes wrong
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)



def my_hook(d):
    #shows messages that update you as to the progress of the download
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #actually downloads file
    ydl.download(['https://www.youtube.com/watch?v=mOYZaiDZ7BM'])
