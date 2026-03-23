import seu_easy_running
from seu_easy_running import run_example
from seu_easy_running.get_student_id import get_id
from seu_easy_running.tracks import get_track_data
import time
import random
import datetime

start_image = r"demo\IMG1.jpg"
end_image = r"demo\IMG2.jpg"
dt = random.randint(360, 420)
track_name = "liuyuan"
delay = False

with open("token.txt", "r") as f:
    token = f.read()
# 1. 获取当前系统时间

stu_id = get_id(token)
if delay:
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=dt)
else:
    end = datetime.datetime.now()
    start = end - datetime.timedelta(seconds=dt)

# 2. 转换为 'YYYY-MM-DD' 格式的日期字符串
current_date = end.strftime("%Y-%m-%d")
# 3. 转换为 'HH:MM:SS' 格式的时间字符串
end_time = end.strftime("%H:%M:%S")
start_time = start.strftime("%H:%M:%S")

track_data = get_track_data(track_name)

calo = random.randint(90, 150)
distance = random.uniform(1.22, 1.3)
run_example(stu_id, token, start_image, end_image, track_data, current_date,
            start_time, end_time, dt, distance, calo, trackname=track_name, delay=delay)
