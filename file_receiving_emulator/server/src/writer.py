import sys
import shutil


class FileWriter:
    @staticmethod
    def get_coroutine(path: str, result_path: str = None, is_binary: bool = False):
        try:
            mode = 'wb' if is_binary else 'w'
            with open(path, mode) as file:
                while True:
                    data = (yield)
                    if data:
                        file.write(data)
                    else:
                        break
            if result_path:
                shutil.move(path, result_path)
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
