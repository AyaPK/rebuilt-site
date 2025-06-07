import subprocess
import sys
import time
from threading import Thread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCHED_DIRS = ['content', 'theme']

class PelicanReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f"Change detected: {event.src_path}. Rebuilding site...")
        subprocess.run([sys.executable, '-m', 'pelican', 'content'])

def serve():
    subprocess.run([sys.executable, '-m', 'pelican', '--listen'])

if __name__ == "__main__":
    # Run the update history script ONCE at startup
    subprocess.run([sys.executable, 'scripts/fetch_update_history.py'])

    # Start Pelican server in a separate thread
    server_thread = Thread(target=serve, daemon=True)
    server_thread.start()

    # Start watchdog observer
    event_handler = PelicanReloadHandler()
    observer = Observer()
    for directory in WATCHED_DIRS:
        observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    print("Watching for changes. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()