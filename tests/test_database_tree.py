#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sqlite3

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fr = logging.Formatter('%(asctime)s - %(message)s')
ch.setFormatter(fr)
log.addHandler(ch)

tree_db_file = "test_database_tree.db"
tree_db = sqlite3.connect(tree_db_file)
tree_db.execute('PRAGMA encoding="UTF-8"')
tree_db.execute('PRAGMA journal_mode="MEMORY"')
tree_db.execute('PRAGMA foreign_keys="ON"')
ct = tree_db.cursor()
with open("./datastore/sqlite/create_nodes_tree.sql") as ft:
    st = ft.read()
    ct.executescript(st)
tree_db_insert = """
INSERT INTO "Nodes" ("id", "parent_id", "label") VALUES (?, ?, ?)
"""

log_msg = "parent_id={}, node_id={}, item={}"

node_id = 0
current_root_id = 0
parsed_dir = os.path.expanduser('~/Images')
log.debug("Start exploration of : {}".format(parsed_dir))

datas = []

for root, dirs, files in os.walk(parsed_dir):
    #~ ct.execute(tree_db_insert, (node_id, current_root_id, root))
    datas.append((node_id, current_root_id, root))
    current_root_id = node_id
    log.debug(log_msg.format(node_id, current_root_id, root))
    #~ for d in dirs:
        #~ node_id += 1
        #~ log.debug(log_msg.format(current_root_id, node_id, "d={}".format(d)))
        #~ ct.execute(tree_db_insert, (node_id, current_root_id, d))
    for f in files:
        node_id += 1
        log.debug(log_msg.format(current_root_id, node_id, "f={}".format(f)))
        #~ ct.execute(tree_db_insert, (node_id, current_root_id, f))
        datas.append((node_id, current_root_id, f))
    node_id += 1

log.debug("Starting creating database...")
ct.executemany(tree_db_insert, datas)
tree_db.commit()
tree_db.close()
