import sys
import pandas as pd


class FileWriter:
    @staticmethod
    def write_df_to_csv(path: str, df: pd.DataFrame, encoding: str = 'utf') -> None:
        try:
            df.to_csv(path, encoding=encoding, index=False)
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
