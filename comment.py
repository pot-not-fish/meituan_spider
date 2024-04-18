'''
Author: LIKE_A_STAR
Date: 2024-03-05 11:04:54
LastEditors: LIKE_A_STAR
LastEditTime: 2024-03-05 12:29:24
Description: 
FilePath: \vscode program\Python file\meituan\comment.py
'''
import requests
import yaml
import json
import time
import pandas as pd

def GetAllComments(config, poi_id_str):
    # with open('poi_id_str.csv','a+') as fp:
    #     # 构造列表头
    #     name = ['用户名', '评论内容', '评分', '简介', '封面', 'id', '播放地址', '时间', '分区']

    #     # 写入文件
    #     writer = pd.DataFrame(self.data,columns=name)
    #     writer.to_csv('b站排行榜.csv',index=False,encoding='utf-8-sig')
    #     print('写入成功')
    #     fp.close()

    isEnd, nextIndex = GetComments(config, 0, poi_id_str)
    while not isEnd:
        isEnd, nextIndex = GetComments(config, nextIndex, poi_id_str)


def GetComments(config, startIndex, poi_id_str):
    headers = {
        "Accept":          config["headers"]["Accept"],
        "Accept-Encoding": config["headers"]["Accept-Encoding"],
        "Accept-Language": config["headers"]["Accept-Language"],
        "Connection":      config["headers"]["Connection"],
        "Content-Type":    config["headers"]["Content-Type"],
        "Cookie":          config["headers"]["Cookie"],
        "Host":            config["headers"]["Host"],
        "Mtgsig":          config["headers"]["Mtgsig"],
        "Origin":          config["headers"]["Origin"],
        "Referer":         config["headers"]["Referer"],
        "Sec-Fetch-Dest":  config["headers"]["Sec-Fetch-Dest"],
        "Sec-Fetch-Mode":  config["headers"]["Sec-Fetch-Mode"],
        "Sec-Fetch-Site":  config["headers"]["Sec-Fetch-Site"],
        "User-Agent":      config["headers"]["User-Agent"]
    }

    payload = {
        "optimus_code":           config["payload"]["optimus_code"],
        "optimus_risk_level":     config["payload"]["optimus_risk_level"],
        "lng":                    config["payload"]["lng"],
        "lat":                    config["payload"]["lat"],
        "gpsLng":                 config["payload"]["gpsLng"],
        "gpsLat":                 config["payload"]["gpsLat"],
        "shopId":                 config["payload"]["shopId"],
        "mtWmPoiId":              config["payload"]["mtWmPoiId"],
        "poi_id_str":             poi_id_str,
        "startIndex":             startIndex,
        "labelId":                config["payload"]["labelId"],
        "scoreType":              config["payload"]["scoreType"],
        "uuid":                   config["payload"]["uuid"],
        "platform":               config["payload"]["platform"],
        "partner":                config["payload"]["partner"],
        "originUrl":              config["payload"]["originUrl"],
        "riskLevel":              config["payload"]["riskLevel"],
        "optimusCode":            config["payload"]["optimusCode"],
        "wm_latitude":            config["payload"]["wm_latitude"],
        "wm_longitude":           config["payload"]["wm_longitude"],
        "wm_actual_latitude":     config["payload"]["wm_actual_latitude"],
        "wm_actual_longitude":    config["payload"]["wm_actual_longitude"],
        "wmUuidDeregistration":   config["payload"]["wmUuidDeregistration"],
        "wmUserIdDeregistration": config["payload"]["wmUserIdDeregistration"],
        "openh5_uuid":            config["payload"]["openh5_uuid"],
        "_token":                 config["payload"]["_token"],
    }

    resp = requests.post("https://i.waimai.meituan.com/openh5/poi/comments?_=1709565750638&yodaReady=h5&csecplatform=4&csecversion=2.4.0", data = payload, headers = headers)

    data = json.loads(resp.text)
    print(resp.status_code)
    for i in data["data"]["list"]:
        print(i["content"])
    
    time.sleep(3)

    return data["data"]["isEnd"], data["data"]["nextStartIndex"]


if __name__ == '__main__':
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    for i in config["poi_id_str"]:
        GetAllComments(config, i)