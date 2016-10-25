#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import getpass

from pysqlcipher import dbapi2 as sqlcipher

from playhouse.sqlcipher_ext import *

db = SqlCipherDatabase(None)  # Defer initialization of the database.

class Note(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

passphrase = getpass.getpass('Enter the diary password: ')
db.init('test_peewee_pysqlcipher3.db', passphrase=passphrase)
