import json
import random
with open(r"seu_easy_running/tracks.json", 'r', encoding='utf-8') as f:
    tracks = json.load(f)
def get_track_data(trackname: str):
    """
    Args:
        trackname (str): 操场名（liuyuan:四牌楼体育场 taoyuan:九龙湖桃园田径场 xiaoying:小营操场）
    """
    track_select = tracks[trackname]
    track_random = []
    sortnum = 1
    for points in track_select:
        dLat = (random.random() - 0.5) * 0.00002
        dLng = (random.random() - 0.5) * 0.00002
        for i in range(random.randint(10, 11)):
            point = {"lat": float(points["lat"]) + dLat, "lng": float(points["lng"]) + dLng, "sortNum": sortnum}
            track_random.append(point)
            sortnum += 1
    return str(track_random)


# tr=tracks["xiaoying"]
# tr1 = []
# lastlat = 0
# for p in tr:
#
#     if lastlat != p["lat"]:
#         point = {"lat": float(p["lat"]) , "lng": float(p["lng"]) }
#         tr1.append(point)
#     lastlat = p["lat"]
# print(tr1)
# print(get_track_data("taoyuan"))