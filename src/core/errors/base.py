#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# base.py


import logging


class BaseError(Exception):

    def __init__(self):
        super().__init__()
        logging.debug(self.__class__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
