import os
from dotenv import load_dotenv
from server import Server


def main() -> None:
    load_dotenv()
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    temp_folder = os.getenv('TEMP_FOLDER')
    result_folder = os.getenv('RESULT_FOLDER')

    server = Server(host, port, temp_folder, result_folder)
    server.receive_file()


if __name__ == '__main__':
    main()
