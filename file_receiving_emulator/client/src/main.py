import os
from dotenv import load_dotenv
from client import Client


def main() -> None:
    load_dotenv()
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    data_file = os.getenv('DATA_FILE')

    client = Client(host, port)
    client.send_file(data_file)


if __name__ == '__main__':
    main()
