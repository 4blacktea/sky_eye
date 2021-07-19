# -*- coding: UTF-8 -*-

# 用于打印post请求体


from flask import Flask
from flask import *
app = Flask(__name__)
import json


@app.route('/reflashcron', methods = ["GET"])
def hello_world():
    #data = request.get_data()
    url = request.url
    # print data
    #app.logger.warning('testing warning log')
    #app.logger.error('testing error log')
    #app.logger.info('testing info log')
    app.logger.debug(str(url))
    app.logger.debug(str(data))
    return str(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8008",debug=True)

