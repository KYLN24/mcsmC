# mcsmC
Minecraft Server Manager Commandline Tool

![mcsmC 0.1](https://img.shields.io/badge/mcsmC-0.1-brightgreen)
[![MCSM 8.6.15](https://img.shields.io/badge/MCSM-8.6.15-yellow)](http://mcsm.suwings.top)
[![Python 3.9.0](https://img.shields.io/badge/Python-3.9.0-blue)](https://www.python.org/downloads/release/python-390/)

## 使用方法
1. 安装最新版 [Python](https://www.python.org/)
2. 在终端/命令提示符中切换到当前目录，执行`pip install -r requirements.txt`安装依赖
3. 运行 main.py `python main.py`

第一次运行会启动初始化助手生成配置文件，亦可手动生成 config.json 配置文件

```json
{
    "apiKey": "00000000000000000000000000000000",
    "isSSL": false,
    "serverAddr": "127.0.0.1:23333",
    "serverName": "main"
}
```

出现提示符 "--->" 意味着初始化完成，使用 help 指令查看帮助
