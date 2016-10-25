#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sqlite3
import socket

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fr = logging.Formatter('%(asctime)s - %(message)s')
ch.setFormatter(fr)
log.addHandler(ch)

db_file = "test_database_flat.db"

db_conn = sqlite3.connect(db_file)
db_conn.execute('PRAGMA encoding="UTF-8"')
db_conn.execute('PRAGMA journal_mode="MEMORY"')
db_conn.execute('PRAGMA foreign_keys="ON"')

db_curs = db_conn.cursor()

db_create = """
CREATE TABLE IF NOT EXISTS "Nodes"(
    "id" INTEGER NOT NULL,
    "label" TEXT NOT NULL, -- eg. store dirpath/filepath for a filesystem tree
    "type" TEXT NOT NULL, -- eg. f for file d for dir for a filesystem tree
    "datas" BLOB DEFAULT NULL, -- eg. file binary datas for a filesystem tree
    PRIMARY KEY ("id")
);

"""

with open("./datastore/sqlite/create_flat_tree.sql") as ff:
    sf = ff.read()
    db_curs.executescript(sf)

db_insert = """
INSERT INTO "Nodes" ("id", "label", "type") VALUES (?, ?, ?)
"""

log_msg = "parent_id={}, node_id={}, item={}"

node_id = 0

parsed_dir = os.path.expanduser('~/Images')
log.debug("Start exploration of : {}".format(parsed_dir))

for root, dirs, files in os.walk(parsed_dir):
    db_curs.execute(db_insert, (node_id, parsed_dir, "d"))
    log.debug(log_msg.format(parent_id, current_root_id, parsed_dir))
    for d in dirs:
        node_id += 1
        log.debug(log_msg.format(current_root_id, node_id, "d={}".format(d)))
        db_curs.execute(db_insert, (node_id, os.path.join(root, d), "d"))
    for f in files:
        node_id += 1
        log.debug(log_msg.format(current_root_id, node_id, "f={}".format(f)))
        db_curs.execute(db_insert, (node_id, os.path.join(root, f), "f"))
    node_id += 1

db_conn.commit()
db_conn.close()
