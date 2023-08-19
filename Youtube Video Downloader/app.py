from pytube import YouTube

link = "https://www.youtube.com/watch?v=LUx8wlA_dk8"
youtube1 = YouTube(link)

print(youtube1.title)
print(youtube1.thumbnail_url)
videos = youtube1.streams.all()
# audios = youtube1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("Enter: "))
videos[strm].download()
print("Successfully!!")

# For playlist
from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?")

print(f'Downloading: {py.title}')

for video in py.videos:
    video.streams.first().download()