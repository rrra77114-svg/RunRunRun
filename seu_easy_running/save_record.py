import requests
import json

plan_config = {
    "taoyuan": {
        'planId': '403640124545491473',
        'routeName': '桃园田径场',
        'routeRule': '九龙湖校区',
        'ruleId': '402186368309502988',
        'maxTime': 12,
        'minTime': 4,
        'orouteKilometre': 1.2,
        'ruleStartTime': '06:00',
        'ruleEndTime': '22:00'
    },
    "liuyuan": {
        "planId": "403640128840458521",
        "routeName": "四牌楼体育场",
        "routeRule": "四牌楼校区",
        "ruleId": "403640128840458519",
        'maxTime': 12,
        'minTime': 4,
        'orouteKilometre': 1.2,
        'ruleStartTime': '06:00',
        'ruleEndTime': '22:00'
    },
    "xiaoying": {
        "ruleId": "403640128840458519",
        "routeRule": "四牌楼校区",
        "ruleStartTime": "06:00",
        "ruleEndTime": "22:00",
        "planId": "403640128840458727",
        "routeName": "小营田径场",
        "routeKilometre": 1.2,
        "minTime": 4,
        "maxTime": 12
    },
}



def send_request(url, headers, data, trackname):
    # 设置请求头
    headers.update({'content-type': 'application/json;charset=utf-8',
                    'Referer': 'https://servicewechat.com/wx5da07e9f6f45cabf/38/page-frame.html',
                    'charset': 'utf-8'})

    data.update(plan_config[trackname])

    response = requests.post(url, headers=headers, json=data)

    return response


def save_start_record(headers: dict, info: dict, start_img_url: str ,trackname) -> str:
    """保存开始记录并返回记录ID"""
    url = f"https://{headers['Host']}/api/exercise/exerciseRecord/saveStartRecord"

    data = {
        'recordTime': info['date'],
        'startTime': info['start_time'],
        'endTime': '',
        'dispTimeText': 0,
        'exerciseTimes': '',
        'routeKilometre': '',
        'speed': "0'00''",
        'calorie': 0,

        'startImage': start_img_url,
        'endImage': '',

        'studentId': info['student_id'],
        'strLatitudeLongitude': []
    }

    response = send_request(url, headers, data,trackname)

    if response.status_code == 200:
        record_id = json.loads(response.text)['data']
        return record_id
    else:
        raise Exception(f'Request failed with status code {response.status_code}. Response: {response.text}')


def save_final_record(headers: dict, info: dict,
                      start_img_url: str, finish_img_url: str, record_id: str,trackname) -> None:
    """保存最终记录"""
    url = f"https://{headers['Host']}/api/exercise/exerciseRecord/saveRecord"

    data = {
        'recordTime': info['date'],
        'startTime': info['start_time'],
        'endTime': info['finish_time'],
        'dispTimeText': info['display_time'],
        'exerciseTimes': info['seconds'],
        'routeKilometre': info['distance'],
        'speed': info['speed'],
        'calorie': info['calorie'],

        'startImage': start_img_url,
        'endImage': finish_img_url,

        'id': record_id,
        'studentId': info['student_id'],
        'strLatitudeLongitude': info['track_data'],
        'nowStatus': 2
    }

    response = send_request(url, headers, data,trackname)

    if response.status_code != 200:
        raise Exception(f'Request failed with status code {response.status_code}. Response: {response.text}')
