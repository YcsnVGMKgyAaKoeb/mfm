# -*- coding: utf-8 -*-


# Example: prints statistics.
#
import pyinotify

class Identity(pyinotify.ProcessEvent):
    def process_default(self, event):
        # Does nothing, just to demonstrate how stuffs could trivially
        # be accomplished after having processed statistics.
        print( 'Does nothing.')

def on_loop(notifier):
    # notifier.proc_fun() is Identity's instance
    s_inst = notifier.proc_fun().nested_pevent()
    print( repr(s_inst), '\n', s_inst, '\n')


wm = pyinotify.WatchManager()
# Stats is a subclass of ProcessEvent provided by pyinotify
# for computing basics statistics.
s = pyinotify.Stats()
notifier = pyinotify.Notifier(wm, default_proc_fun=Identity(s), read_freq=5)
wm.add_watch('/tmp/', pyinotify.ALL_EVENTS, rec=True, auto_add=True)
notifier.loop(callback=on_loop)


#~ import os
#~ import sys
#~ import time
#~ import logging
#~ from watchdog.observers import Observer
#~ from watchdog.events import LoggingEventHandler

#~ if __name__ == "__main__":
    #~ logging.basicConfig(level=logging.INFO,
                        #~ format='%(asctime)s - %(message)s',
                        #~ datefmt='%Y-%m-%d %H:%M:%S')
    #~ default_path = os.path.expanduser('~')
    #~ path = sys.argv[1] if len(sys.argv) > 1 else default_path
    #~ print(path)
    #~ event_handler = LoggingEventHandler()
    #~ observer = Observer()
    #~ observer.schedule(event_handler, path, recursive=True)
    #~ observer.start()
    #~ try:
        #~ while True:
            #~ time.sleep(1)
    #~ except KeyboardInterrupt:
        #~ observer.stop()
    #~ observer.join()

#~ import os, sys
#~ from pyinotify import WatchManager, Notifier, ProcessEvent, EventsCodes
#~ import pyinotify
#~ events_codes = pyinotify.EventsCodes.ALL_VALUES

#~ def Monitor(path):
    #~ class PClose(ProcessEvent):
        #~ def process_IN_CLOSE(self, event):
            #~ f = event.name and os.path.join(event.path, event.name) or event.path
            #~ print('close event: ' + f)

    #~ wm = WatchManager()
    #~ notifier = Notifier(wm, PClose())
    #~ wm.add_watch(path, events_codes.IN_CLOSE_WRITE|events_codes.IN_CLOSE_NOWRITE)

    #~ try:
        #~ while 1:
            #~ notifier.process_events()
            #~ if notifier.check_events():
                #~ notifier.read_events()
    #~ except KeyboardInterrupt:
        #~ notifier.stop()
        #~ return


#~ if __name__ == '__main__':
    #~ try:
        #~ path = sys.argv[1]
        #~ path = os.path.expanduser('~')
    #~ except IndexError:
        #~ print('use: %s dir' % sys.argv[0])
    #~ else:
        #~ Monitor(path)
