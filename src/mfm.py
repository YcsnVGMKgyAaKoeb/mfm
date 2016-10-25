#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# mfm.py

import logging

import core


class MFMType(type):
    __name__ = "MFMType"

    def __init__(self, *args, **kwargs):
        logging.debug(self.__name__)
        pass


class MFMBase(MFMType):
    __name__ = "MFMBase"

    def __init__(self, *args, **kwargs):
        logging.debug(self.__name__)
        pass

    def __str__(self):
        attributes = "\n".join(
            sorted(
                ["    [{}] : {}".format(k, v)
                    for k, v in self.__dict__.items()
                ]
            )
        )
        methods = "\n".join(
            sorted(
                ["    {}".format(m)
                    for m in dir(self) if not m in attributes
                ]
            )
        )
        return "Attributs : \n{}\nMethodes : \n{}".format(attributes, methods)

    def __del__(self):
        pass


class MFM(MFMBase):

    def __init__(self, *args, **kwargs):
        logging.debug(self.__name__)
        pass



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    mfm = MFM()
