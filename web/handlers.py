#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from comm.coroweb import get, post
from comm.apis import APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id

#导入api链接的
from HANDLERS.Users_i import *

# @get('/')
# async def index(request):
#     # users = await User.findAll()
#     return {
#         '__template__': 'index.html',
#         # 'users': users
#     }
@get('/{ht}.html')
async def html(ht):
    # users = await User.findAll()

    ###增加文件判断，判断是否有文件，如无，返回404.html
    return {
        '__template__': '%s.html' %(ht),
        # 'users': users
    }
@get('/test')
async def test(request):
    return {
        '__template__': 'index.html',
    }
