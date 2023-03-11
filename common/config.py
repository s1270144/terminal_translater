"""
config.py

各設定値を環境変数へ設定する

import config

print(config.MYAPP_USER)
print(config.MYAPP_PASS)
"""

import os
import configparser
from dotenv import load_dotenv

# .env ファイルをロードして環境変数へ反映させる
load_dotenv(override=True)

# 環境変数を参照する
OPENAI_API = os.getenv('OPENAI_API')

# .ini ファイル
ini = configparser.ConfigParser()
ini.read('./config.ini', 'UTF-8')


def reload_env():
    global OPENAI_API

    load_dotenv(override=True)
    OPENAI_API = os.getenv('OPENAI_API')
