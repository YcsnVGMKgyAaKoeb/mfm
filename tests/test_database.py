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

flat_db_file = "test_database_flat.db"
tree_db_file = "test_database_tree.db"

flat_db = sqlite3.connect(flat_db_file)
flat_db.execute('PRAGMA encoding="UTF-8"')
flat_db.execute('PRAGMA journal_mode="MEMORY"')
flat_db.execute('PRAGMA foreign_keys="ON"')
cf = flat_db.cursor()
with open("./datastore/sqlite/create_flat_tree.sql") as ff:
    sf = ff.read()
    cf.executescript(sf)
flat_db_insert = """
INSERT INTO "Nodes" ("id", "label", "type") VALUES (?, ?, ?)
"""

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
cf.execute(flat_db_insert, (node_id, parsed_dir, "d"))
ct.execute(tree_db_insert, (node_id, current_root_id, root))
for root, dirs, files in os.walk(parsed_dir):
    current_root_id = ct.lastrowid
    log.debug(log_msg.format(parent_id, current_root_id, parsed_dir))
    for d in dirs:
        node_id += 1
        log.debug(log_msg.format(current_root_id, node_id, "d={}".format(d)))
        cf.execute(flat_db_insert, (node_id, os.path.join(root, d), "d"))
        ct.execute(tree_db_insert, (node_id, current_root_id, d))
    for f in files:
        node_id += 1
        log.debug(log_msg.format(current_root_id, node_id, "f={}".format(f)))
        cf.execute(flat_db_insert, (node_id, os.path.join(root, f), "f"))
        ct.execute(tree_db_insert, (node_id, current_root_id, f))
    node_id += 1
tree_db.commit()
tree_db.close()
flat_db.commit()
flat_db.close()
