import sys
import pandas as pd


class DFNormalizer:
    def __init__(self, columns: list) -> None:
        self.__columns = columns

    def __call__(self, *args, **kwargs) -> pd.DataFrame:
        return self.__normilize(*args)

    def __normilize(self, df: pd.DataFrame) -> pd.DataFrame:
        """Rename columns and convert date to datetime"""
        try:
            df.columns = self.__columns
            df['date'] = pd.to_datetime(df['date'], unit='s')
            return df
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
