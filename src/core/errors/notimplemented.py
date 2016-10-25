#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# ./notimplemented.py


import logging
logging.basicConfig(level=logging.DEBUG)


import base


class NotImplementedError(base.BaseError):
    """ for non critical functions/class """

    def __init__(self, element, *args, **kwargs):
        super().__init__()
        msg = "({t}.{n}) should ({d}) and does not the job!"
        typ = element.__class__.__name__
        try:
            nam = type(element)
        except Exception as ex:
            logging.debug('str')
            nam = str(element)

        doc = element.__doc__.strip()
        self.message = msg.format(t=typ, n=nam, d=doc)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    raise NotImplementedError(NotImplementedError)
