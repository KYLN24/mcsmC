# check.py

import os, requests


def isFirstTime() -> bool:
    if os.path.exists('config.json'):
        return False
    else:
        return True


def connectionCheck(serverAddr, serverName, isSSL) -> bool:
    if isSSL:
        url = "https://" + serverAddr + "/api/status/" + serverName
    else:
        url = "http://" + serverAddr + "/api/status/" + serverName
    if requests.get(url).status_code == 200:
        return True
    else:
        return False


def apiKeyCheck(serverAddr, serverName, isSSL, apiKey) -> bool:
    if isSSL:
        url = "https://" + serverAddr + "/api/execute/" + \
              "?apikey=" + apiKey + "&name=" + serverName + "&command=version"
    else:
        url = "http://" + serverAddr + "/api/execute/" + \
              "?apikey=" + apiKey + "&name=" + serverName + "&command=version"
    if requests.get(url).status_code == 200:
        return True
    else:
        return False

def checkAll(serverAddr, serverName, isSSL, apiKey):
    if isFirstTime():
        print("找不到配置文件")
    else:
        print("配置文件正常")
    if connectionCheck(serverAddr, serverName, isSSL):
        print("服务器连接正常")
    else:
        print("无法连接至服务器")
    if apiKeyCheck(serverAddr, serverName, isSSL, apiKey):
        print("API Key 有效")
    else:
        print("API Key 无效")