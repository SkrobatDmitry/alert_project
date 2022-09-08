import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, callback) -> None:
        self.__callback = callback
        self.__is_worked = False  # (´。＿。｀)
        super().__init__()

    def on_created(self, event) -> None:
        self.__callback(event.src_path)
        self.__is_worked = True  # (╯°□°）╯︵ ┻━┻

    def get_is_worked(self) -> bool:
        """To shut down the observer for demo"""
        return self.__is_worked


class Checker:
    @staticmethod
    def watch(path: str, callback) -> None:
        event_handler = FileEventHandler(callback)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=False)
        observer.start()
        try:
            while True:
                if not event_handler.get_is_worked():  # Imagine that this line is not here
                    time.sleep(1)
                else:                                  # And this
                    raise KeyboardInterrupt            # And this too
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
