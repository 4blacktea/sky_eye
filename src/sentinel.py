# -*- coding: UTF-8 -*-

# 哨兵进程，用于在更新crontab任务后刷新任务


from flask import Flask
from flask import *
app = Flask(__name__)
import json


@app.route('/reflashcron', methods = ["GET"])
def hello_world():
    #data = request.get_data()
    url = request.url
    app.logger.debug(str(url))
    app.logger.debug(str(data))
    return str(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8008",debug=True)

