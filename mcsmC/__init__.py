"""
mcsmC: Minecraft Server Manager CommandLine Tool
"""

import json, requests, yaml
from . import check


class MCSMServer:
    def __init__(self, serverAddr, serverName, isSSL, apiKey):
        self.addr = serverAddr
        self.apiKey = apiKey
        self.name = serverName
        self.isSSL = isSSL

    def genURL(self, method: str):
        if self.isSSL:
            url = "https://"
        else:
            url = "http://"
        url += "{}/api/{}/{}?apikey={}".format(self.addr, method, self.name, self.apiKey)
        return url

    def status(self):
        url = self.genURL("status")
        status = json.loads(requests.get(url).text)
        if 'serverName' in status.keys():
            if status["version"]:
                print("服务器名称: {}\n玩家个数: {}/{}\nmotd: {}\n版本: {}".format(
                    status["serverName"],
                    status["current_players"], status["max_players"],
                    status["motd"],
                    status["version"]
                )
                )
            else:
                print("服务器 {} 正在运行，但没有获取到信息\n上次更新时间: {}".format(
                    status["id"],
                    status["lastDate"]
                ))
        else:
            print("服务器 {} 未运行\n上次更新时间: {}".format(
                status["id"],
                status["lastDate"]
            ))

    def start(self):
        url = self.genURL("start_server")
        started = requests.get(url).status_code
        if started == 200:
            print("服务器已开启")
        else:
            print("开启失败")

    def close(self):
        url = self.genURL("stop_server")
        closed = requests.get(url).status_code
        if closed == 200:
            print("服务器已关闭")
        else:
            print("关闭失败")

    def restart(self):
        url = self.genURL("restart_server")
        restarted = requests.get(url).status_code
        if restarted == 200:
            print("服务器已重启")
        else:
            print("重启失败")

    def exec(self, cmd):
        if self.isSSL:
            url = "https://"
        else:
            url = "http://"
        url += "{}/api/execute/".format(self.addr)
        data = {
            "apikey": self.apiKey,
            "name": self.name,
            "command": cmd
        }
        close = requests.post(url, data=data)
        if close.status_code == 200:
            print("已发送指令")
        else:
            print("指令发送失败！")


def loadConfig() -> MCSMServer:
    with open('config.yml', 'r') as cfgF:
        cfg = yaml.load(cfgF, Loader=yaml.FullLoader)
        server = MCSMServer(cfg['serverAddr'], cfg['serverName'], cfg['isSSL'], cfg['apiKey'])
        if server.isSSL:
            print("通过 HTTPS ", end='')
        else:
            print("通过 HTTP ", end='')
        print("连接到 {} 上的服务器 {}".format(server.addr, server.name))
        return server


def mainLoop(server: MCSMServer):
    """帮助：
    help: 帮助菜单
    status: 查询服务器状态
    start: 开启服务器
    close: 关闭服务器
    restart: 重启服务器
    exec: 发送控制台指令
    check: 自检
    exit: 退出
    """
    arg = input("--> ")
    if arg == 'help':
        print(mainLoop.__doc__)
    elif arg == 'status':
        server.status()
    elif arg == 'start':
        server.start()
    elif arg == 'close':
        server.close()
    elif arg == 'restart':
        server.restart()
    elif arg == 'exec':
        cmd = input('exec: ')
        server.exec(cmd)
    elif arg == 'check':
        check.checkAll(server.addr, server.name, server.isSSL, server.apiKey)
    elif arg == 'exit':
        exit()
    else:
        print("没有这个指令！请输入 help 查看帮助")
