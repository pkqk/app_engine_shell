#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
# Copyright © 2010 Andrew D. Yates
# All Rights Reserved.
"""Google App Engine Python Shell Environment Utility

Import to enable App Engine Python library imports outside the app
engine webserver. This is useful for debugging, testing, and using
Google App Engine libraries in a local Python shell.

Example:

$ ipython
>>> import app_engine_shell
... from google.appengine.api import urlfetch
... response = urlfetch.fetch("http://hhmds.com")
... from google.appengine.ext import db
... class Model(db.Model):
...   pass
... m = Model()
"""
__authors__ = ["'Andrew D. Yates', <andrew.yates@hhmds.com>"]


import os
import sys
sys.path = sys.path + [
  '/usr/local/google_appengine',
  '/usr/local/google_appengine/lib/django',
  '/usr/local/google_appengine/lib/webob',
  '/usr/local/google_appengine/lib/yaml/lib',
  '/usr/local/google_appengine/google/appengine',
  ]
 
from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import urlfetch_stub
from google.appengine.api import user_service_stub


APPLICATION_ID = u'shell'
AUTH_DOMAIN = 'localhost'
# empty string is "no user"
USER_EMAIL = ''


os.environ['APPLICATION_ID'] = APPLICATION_ID
os.environ['AUTH_DOMAIN'] = AUTH_DOMAIN
os.environ['USER_EMAIL'] = USER_EMAIL
 
apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
 
# null datastore; datastore changes will not be saved to disk
stub = datastore_file_stub.DatastoreFileStub(
  APPLICATION_ID, '/dev/null', '/dev/null')
apiproxy_stub_map.apiproxy.RegisterStub(
  'datastore_v3', stub)

# other app engine services
apiproxy_stub_map.apiproxy.RegisterStub(
  'mail', mail_stub.MailServiceStub())
apiproxy_stub_map.apiproxy.RegisterStub(
  'urlfetch', urlfetch_stub.URLFetchServiceStub())
apiproxy_stub_map.apiproxy.RegisterStub(
  'user', user_service_stub.UserServiceStub())
