import sys
import socket
from tqdm import tqdm
from writer import FileWriter


class Server:
    def __init__(self, host: str, port: int, temp_folder: str,
                 result_folder: str, size: int = 4096, encoding: str = 'utf-8') -> None:
        self.__addr = (host, port)
        self.__temp_folder = temp_folder
        self.__result_folder = result_folder
        self.__size = size
        self.__format = encoding
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive_file(self) -> None:
        try:
            self.__sock.bind(self.__addr)
            self.__sock.listen()
            print('[+] Listening...')

            conn, addr = self.__sock.accept()
            print(f'[+] New connection from {addr[0]}:{addr[1]}')

            data = conn.recv(self.__size).decode(self.__format)
            file_name, file_size = data.split('&')
            file_size = int(file_size)

            print('[+] File name and file size received from the client')
            conn.send('Filename and filesize received'.encode(self.__format))

            bar = tqdm(range(file_size), f'Receiving {file_name}', unit='B', unit_scale=True, unit_divisor=self.__size)

            writer = FileWriter()
            writer_coroutine = writer.get_coroutine(f'{self.__temp_folder}{file_name}',
                                                    f'{self.__result_folder}{file_name}', is_binary=True)
            next(writer_coroutine)
            while True:
                data = conn.recv(self.__size)
                writer_coroutine.send(data)
                if not data:
                    break

                bar.update(len(data))

            conn.close()
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
        finally:
            self.__sock.close()
