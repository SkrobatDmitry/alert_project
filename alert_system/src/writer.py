import sys
import pandas as pd


class FileWriter:
    @staticmethod
    def write_df_to_json(path: str, df: pd.DataFrame) -> None:
        try:
            df.to_json(path, orient='index', indent=4)
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
