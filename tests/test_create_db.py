# -*- coding: utf-8 -*-


import logging
import os
import sys
import socket
import peewee
import platform
import socket
import collections
import time
import dateutil


from peewee import (
    Model,
    CharField,
    ForeignKeyField,
)
from playhouse.sqlite_ext import (
    SqliteExtDatabase,
    ClosureTable,
)


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fr = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(fr)
log.addHandler(ch)

src_root = os.path.realpath(os.path.dirname(__file__))
log.debug("running in : {}".format(src_root))

app_root = os.path.realpath(os.path.dirname(src_root))
log.debug("application root is : {}".format(app_root))

#TODO: database selector
db = SqliteExtDatabase(os.path.join(src_root, 'test_create_db.db'))
#NOTE: the bin/sqlite/closure.so must be compilled before script use
db_closure_ext = os.path.join(app_root, 'bin/sqlite/closure')
#NOTE: do not include the ".so"
db.load_extension(db_closure_ext)
log.debug("database is : %s", db)
log.debug("sqlite closure extension loaded : {}".format(ClosureTable))

#~ username = os.environ.get("USER")
username = os.getenv("USER")
log.debug("username is : %s", username)


#~ class log(object):

#~ class Host:


def localhost_infos():
    """ Return a collections.namedtuples of host machine informations
    """
    host = {}
    d = socket.gethostbyaddr(socket.gethostname())
    host["name"], host["name_aliases"], host["ip_addresses"] = d


    log.debug("host_infos is : %s", host)


#~ hostname = socket.gethostname()
hostname = socket.gethostbyaddr(socket.gethostname())
log.debug("hostname is : %s", hostname)

system = platform.system()
if system.lower() == "linux":
    system = set([
        system,
        *platform.dist(),
        *platform.architecture(),
        platform.machine()
    ])
    #~ osvars = os.uname()
    #~ log.debug("osvars is : %s", osvars)
log.debug("system is : %s", system)

#~ if __name__ == "__main__":
    #~ log.setLevel(logging.DEBUG)
    #~ ch = logging.StreamHandler()
    #~ ch.setLevel(logging.DEBUG)
    #~ fr = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    #~ ch.setFormatter(fr)
    #~ log.addHandler(ch)
