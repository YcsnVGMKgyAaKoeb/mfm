#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# ./image_browser.py


import hashlib
import os
import re
import sys
import unicodedata
import collections
import itertools
import subprocess


try:
    #~ from PyQt5.QtCore import (
        #~ QByteArray,
        #~ QFile,
        #~ QPoint,
        #~ Qt,
    #~ )

    from PyQt5.QtWidgets import (
        #~ QAction,
        QShortcut,
        QApplication,
        #~ QFileDialog,
        #~ QGridLayout,
        #~ QLabel,
        QMainWindow,
        #~ QMenu,é
        #~ QPushButton,
        #~ QSizePolicy,
        #~ QVBoxLayout,
        QWidget,
    )

    from PyQt5.QtGui import (
        #~ QMovie,
        #~ QPixmap,
        QKeySequence,
        #~ QWheelEvent,
    )
except ImportError:
    sys.exit("This script needs the PyQt5 module to run.")


IMG_EXTENSIONS = [ # supported image format
    '.bmp',
    '.gif',
    '.jpg',
    '.jpeg',
    '.png',
    '.pbm',
    '.pgm',
    '.ppm',
    '.xbm',
    '.xpm',
]


def prev_current_and_next(an_iterable):
    """ return a triple of previous, current and next item in the given
        iterable
    """
    prevs, items, nexts = itertools.tee(an_iterable, 3)
    prevs = itertools.chain([None], prevs)
    nexts = itertools.chain(itertools.islice(nexts, 1, None), [None])
    return itertools.izip(prevs, items, nexts)


def unc_string(a_string):
    """ return a lower case string without any special character
    """
    # enlever les accents
    nkfd_form = unicodedata.normalize('NFKD', a_string)
    string = "".join([c for c in nkfd_form if not unicodedata.combining(c)])
    # remplacer les espaces par des underscores
    string = string.strip().replace(' ', '_')
    # enlever tous les caractères non alpha-numérique
    string = re.sub(r'[^\w]', '', string)
    # corriger les doubles underscores
    string = string.strip().replace('__', '_')
    return string.lower()


def sort_nicely(a_list):
    """ sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda k: [convert(c) for c in re.split('([0-9]+)', k)]
    a_list.sort(key=alphanum_key)


def files_from_dir(a_dirpath):
    """ return a list of files from given dirpath sorted in the way that
        humans expect.
    """
    root, dirs, files = next(os.walk(a_dirpath))
    files = [ os.path.join(root, f) for f in files ]
    sort_nicely(files)
    return files


def next_file(a_filepath):
    """ return the filepath of the next file in given filepath directory.
        the file list is sorted in the way that humans expect.
    """
    files = files_from_dir(os.path.dirname(a_filepath))
    l = len(files)
    for i, f in enumerate(files):
        if f == a_filepath:
            if i < (l - 1):
                return files[i + 1]
            else:
                return None


def prev_file(a_filepath):
    """ return the filepath of the previous file in given filepath directory.
        the file list is sorted in the way that humans expect.
    """
    files = files_from_dir(os.path.dirname(a_filepath))
    l = len(files)
    for i, f in enumerate(files):
        if f == a_filepath:
            if i > 0:
                return files[i - 1]
            else:
                return None


def prev_current_and_next_files(a_filepath):
    """ return a triple of previous, current and next file pathes in the given
        filepath directory
    """
    p = prev_file(a_filepath)
    n = next_file(a_filepath)
    return p, a_filepath, n


class Colors(object):

    @staticmethod
    def hex_to_rgb(hexcode):
        """ hexcode = 6 characters string hexcode
            Return a tuple of (red, green, blue) decimal values
        """
        dec = '0123456789abcdefABCDEF'
        hexdec = {v: int(v, 16) for v in (x+y for x in dec for y in dec)}
        return hexdec[hexcode[0:2]], hexdec[hexcode[2:4]], hexdec[hexcode[4:6]]

    @staticmethod
    def rgb_to_hex(rgb, *, case='low'):
        """ rgb = tuple of (red, green, blue) decimal values
            Return a 6 characters string hexcode
        """
        if case == 'up':
            lettercase = 'X'
        else:
            lettercase = 'x'
        return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)


class FileHash(object):

    @staticmethod
    def md5(fname):
        """ return md5 hash from file
        """
        _hash = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                _hash.update(chunk)
        return _hash.hexdigest()

    @staticmethod
    def sha1(fname):
        """ return sha1 hash from file
        """
        _hash = hashlib.sha1()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                _hash.update(chunk)
        return _hash.hexdigest()

    @staticmethod
    def sha256(fname):
        """ return sha256 hash from file
        """
        _hash = hashlib.sha256()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                _hash.update(chunk)
        return _hash.hexdigest()

    @staticmethod
    def sha512(fname):
        """ return sha512 hash from file
        """
        _hash = hashlib.sha512()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                _hash.update(chunk)
        return _hash.hexdigest()

    @staticmethod
    def sha(fname):
        """ return triple sha{1, 256, 512} hashes from file
        """
        _hash1 = hashlib.sha1()
        _hash256 = hashlib.sha256()
        _hash512 = hashlib.sha512()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                _hash1.update(chunk)
                _hash256.update(chunk)
                _hash512.update(chunk)
        return _hash1.hexdigest(), _hash256.hexdigest(), _hash512.hexdigest()

    @staticmethod
    def all(fname):
        """ return all availlable hashes from file
        """
        _hashes = {}
        for algo in hashlib.algorithms_available:
            _hashes[algo] = hashlib.new(algo)
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                for _hash  in _hashes.values():
                    _hash.update(chunk)
        for _algo, _hash  in _hashes.items():
            _hashes[_algo] = _hash.hexdigest()
        return collections.OrderedDict(sorted(_hashes.items()))


class Qt5ImageWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


class Qt5FSTreeView(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)



class Qt5UI(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(800, 600)
        self.setWindowTitle("Image Viewer")
        self.setStyleSheet("Qt5UI{background-color: rgba(110,110,110,210);}")
        self.showMaximized()
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.close)


def main_qt5(*args, **kwarg):
    app = QApplication([args])
    dia = Qt5UI()
    sys.exit(app.exec_())


def main(*args):
    _dir = "/home/rw/.rwbox/.rwpvt/tmp/20111201"
    for root, dirs, files in os.walk(_dir):
        sort_nicely(files)
        for f in files:
            fp = os.path.join(root, f)
            print(FileHash.sha(fp), fp)
    sys.exit(0)


if __name__ == '__main__':
    main_qt5(sys.argv[1:])
