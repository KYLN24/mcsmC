# main.py

from mcsmC import *
from mcsmC import check, firstStart

motd = """\
- MCSM 命令行工具 -
mcsmC: Minecraft Server Manager CommandLine Tool
=================================\
"""
print(motd)

if check.isFirstTime():
    firstStart.firstRun()

server = loadConfig()

while True:
    mainLoop(server)
