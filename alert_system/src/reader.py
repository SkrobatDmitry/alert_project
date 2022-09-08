import sys
import pandas as pd


class FileReader:
    @staticmethod
    def get_df_from_csv(path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(path)
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
