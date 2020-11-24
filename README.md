# mcsmC
Minecraft Server Manager Commandline Tool

[![mcsmC 0.1.0](https://img.shields.io/badge/mcsmC-0.1.0-brightgreen)](https://github.com/KYLN24/mcsmC)
[![MCSM 8.6.15](https://img.shields.io/badge/MCSM-8.6.15-yellow)](http://mcsm.suwings.top)
[![Python 3.9.0](https://img.shields.io/badge/Python-3.9.0-blue)](https://www.python.org/downloads/release/python-390/)

## 使用方法
1. 在服务器运行 MCSM 并创建一个能正常运行的 Minecraft 服务器
2. 获取你的 API Key
3. 安装最新版 [Python](https://www.python.org/)
4. 在终端/命令提示符中切换到当前目录，执行 `pip install -r requirements.txt` 安装依赖
5. 运行 main.py `python main.py`

第一次运行会启动初始化助手生成配置文件，亦可手动创建 `config.yml` 配置文件

#### config.yml模板
```yaml
# 你的 MCSM 账户 APIKey
apiKey: 00000000000000000000000000000000

# 是否使用 HTTPS
isSSL: false

# MCSM 地址
serverAddr: '127.0.0.1:23333'

# MCSM 服务端名称
serverName: main
```

出现提示符 "-->" 意味着初始化完成，使用 help 指令查看帮助
