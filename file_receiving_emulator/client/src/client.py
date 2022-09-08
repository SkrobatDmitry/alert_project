import os
import sys
import socket
from tqdm import tqdm
from reader import FileReader


class Client:
    def __init__(self, host: str, port: int, size: int = 4096, encoding: str = 'utf-8') -> None:
        self.__addr = (host, port)
        self.__size = size
        self.__format = encoding
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_file(self, path: str) -> None:
        try:
            self.__sock.connect(self.__addr)

            file_name = os.path.basename(path)
            file_size = os.path.getsize(path)

            data = f'{file_name}&{file_size}'
            self.__sock.send(data.encode(self.__format))
            msg = self.__sock.recv(self.__size).decode(self.__format)
            print(f'SERVER: {msg}')

            bar = tqdm(range(file_size), f'Sending {file_name}', unit='B', unit_scale=True, unit_divisor=self.__size)

            file_reader = FileReader()
            for data in file_reader.get_data(path, size=self.__size, is_binary=True):
                self.__sock.send(data)
                bar.update(len(data))
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
        finally:
            self.__sock.close()
