#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("status code:", r.status_code)
requestsz_dict = r.json()

print(r.key())
