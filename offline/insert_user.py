# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: insert_user.py
@Time: 2023-03-09 22:35
@Last_update: 2023-03-09 22:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from lib.MongdbClient import MongodbClient


if __name__ == '__main__':
    # 离线添加用户
    mongo_client = MongodbClient()
    username, password = '', ''
    mongo_client.insert_user(username, password)
