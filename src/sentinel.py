# -*- coding: UTF-8 -*-

# 哨兵进程，用于在更新crontab任务后刷新任务


from flask import Flask
from flask import *
app = Flask(__name__)
import json
import os
import re
import signal


def kill_pid(program_name)
    # 要杀死程序名称，最好全名
    # 终端执行的命令
    order_str = "ps x | grep %s" % program_name
    # 执行
    strs_obj = os.popen(order_str)
    t_strs = strs_obj.read()
    # 通过正则获取pid
    pid_list = re.findall(r"(\d+).+chromedriver --port=\d+", t_strs, re.I)
    print(pid_list)
    for j in pid_list:
        print(j)
        # 杀死进程
        os.kill(int(j), signal.SIGKILL)


@app.route('/reflashcron', methods = ["GET"])
def hello_world():
    #data = request.get_data()
    url = request.url
    app.logger.debug(str(url))
    app.logger.debug(str(data))
    kill_pid("cron.py")
    os.system("python3 cron.py")
    return str(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8008",debug=True)

