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

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        # 'users': users
    }

@get('/test')
async def index(request):
    return {
        '__template__': 'test.html',
    }
