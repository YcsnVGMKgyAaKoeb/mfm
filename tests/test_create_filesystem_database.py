#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os

for root, dirs, files in os.walk('..'):
    print("current root :", root)
    for d in dirs:
        print(os.path.join(root,d))
