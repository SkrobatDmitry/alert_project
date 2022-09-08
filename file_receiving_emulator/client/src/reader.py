import sys


class FileReader:
    @staticmethod
    def get_data(path: str, size: int = False, is_binary: bool = False):
        try:
            mode = 'rb' if is_binary else 'r'
            with open(path, mode) as file:
                while True:
                    data = file.read(size)
                    if data:
                        yield data
                    else:
                        break
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
