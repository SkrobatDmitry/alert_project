import sys
import pandas as pd
from alert_factory.error_level_handler.error_level_handler import ErrorLevelHandler


class FatalErrorHandler(ErrorLevelHandler):
    def __call__(self, *args, **kwargs) -> pd.DataFrame:
        return self._get_df_by_error_level(*args)

    def get_error_level_name(self) -> str:
        return 'Fatal'

    def _get_df_by_error_level(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            return df[df['severity'] == 'Error']
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)
