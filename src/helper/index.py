# coding=utf-8

import requests
import os


def handler(event, context):
    url = os.environ['KEEP_WARM_FC_URL']
    res = requests.head(url)
    print(res.status_code)
