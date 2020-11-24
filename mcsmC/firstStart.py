# firstRun.py

import yaml
from mcsmC import MCSMServer
from . import check


def firstRun():
    print("mcsmC 初始化助理\n---------")
    serverAddr = input("MCSM 地址(127.0.0.1:23333): ")
    if not serverAddr:
        serverAddr = "127.0.0.1:23333"
    isSSL = input("启用 HTTPS 加密？(y/N): ") == "y"
    serverName = input("MCSM 服务器名称(main): ")
    if not serverName:
        serverName = "main"
    if isSSL:
        serverURL = "https://" + serverAddr + "/api/status/" + serverName
    else:
        serverURL = "http://" + serverAddr + "/api/status/" + serverName
    if input("是否检查服务器连通性？(y/N): ") == "y":
        if check.connectionCheck(serverAddr, serverName, isSSL):
            print("服务器连接成功！")
        else:
            print("服务器连接失败，初始化将继续，你稍后可在 config.yml 文件中修改相关配置。")

    apiKey = "000000000000000000000000000000"
    apiKey = input("输入 API Key(000000000000000000000000000000):")
    if input("是否检查 API Key 有效性？(y/N): ") == "y":
        if check.apiKeyCheck(serverAddr, serverName, isSSL, apiKey):
            print("API Key 有效！")
        else:
            print("API Key 无效或服务器无法连通，初始化将继续，你稍后可在 config.yml 文件中修改相关配置。")

    serverDict = {
        'serverAddr': serverAddr,
        'serverName': serverName,
        'isSSL': isSSL,
        'apiKey': apiKey
    }

    with open("config.yml", "w") as f:
        yaml.dump(serverDict, f)
    print("初始化完成！配置已覆盖，你可在 config.yml 文件中继续修改配置")
