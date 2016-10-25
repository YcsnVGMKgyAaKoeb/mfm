#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# ./networks.py


import errors


def get_public_ip():
    """ Return internet public ip """
    raise errors.NotImplementedError(get_public_ip)


if __name__ == "__main__":
    print(get_public_ip())
