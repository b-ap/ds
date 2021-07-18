#/usr/bin/python3

import pymysql
from os import environ as env
from flask import g

def get_db():
    if 'db' not in g:
        g.db = pymsql.connect(
            host       = env['DB_HOST'],
            db         = env['DB_NAME'],
            user       = env['DB_USER'],
            passwd     = env['DB_PASS'],
            autocommit = True
        )
    return g.db

def close_db():
    db = g.pop('db', None)
    if db:
        db.close()
