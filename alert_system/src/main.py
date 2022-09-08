import os
from dotenv import load_dotenv
from checker import Checker
from log_handler import LogHandler


def main():
    load_dotenv()
    obeserver_folder = os.getenv('OBSEVER_FOLDER')

    checker = Checker()
    checker.watch(obeserver_folder, LogHandler.process_log)


if __name__ == '__main__':
    main()
