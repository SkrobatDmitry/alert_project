import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from reader import FileReader
from writer import FileWriter
from normalizer import DFNormalizer
from alert_factory.more_10_fatal_errors_in_minute_factory import More10FatalErrorsInMinuteFactory
from alert_factory.more_10_fatal_errors_in_hour_with_bundle_factory import More10FatalErrorsInHourWithBundleFactory


class LogHandler:
    @staticmethod
    def process_log(path: str) -> None:
        try:
            load_dotenv()
            columns = os.getenv('COLUMNS').split(',')
            result_folder = os.getenv('RESULT_FOLDER')

            reader = FileReader()
            writer = FileWriter()
            normalizer = DFNormalizer(columns)

            data_df = reader.get_df_from_csv(path)
            data_df = normalizer(data_df)

            factories = [More10FatalErrorsInMinuteFactory(), More10FatalErrorsInHourWithBundleFactory()]
            for factory in factories:
                error_level_handler = factory.get_error_level_handler()
                notification_rule_handler = factory.get_notification_rule_handler()

                alert_df = error_level_handler(data_df)
                alert_df = notification_rule_handler(alert_df)
                # For demo, alerts are simply written to a csv file
                writer.write_df_to_csv(f'{result_folder}'
                                       f'{Path(path).stem}_'
                                       f'{notification_rule_handler.get_notification_rule_name().lower()}_'
                                       f'{error_level_handler.get_error_level_name().lower()}.csv', alert_df)

            print(f'[+] {Path(path).name} has been processed')
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
