from shorts_gen import ShortsGen
import json
import datetime

sg = ShortsGen()

# Starting from today, take an integer starting from 1
startdate = datetime.datetime(2023, 4, 17)
today = datetime.datetime.today()
day_idx = (today - startdate).days

# Get the number of days
video_count = (startdate - today).days

with open("resource/expression.csv", 'r') as f:
    for i in range(day_idx - 1):
        f.readline()
    data = f.readline()
    data = json.loads(data)
    print(f"Key word: {data['0']}")
    sg.make_video(day_idx, data)