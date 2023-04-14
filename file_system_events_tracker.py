import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Addhayan/OneDrive/Documents"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Hey, {event.src_path} has been deleted")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved")
eventHandler = FileMovementHandler()

observer = Observer()
observer.schedule(eventHandler, from_dir, recursive = True)
observer.start()
try:
    while True:
        time.sleep(True)
        print("running....")
except KeyboardInterrupt:
    print("stopped!!")
    observer.stop()
