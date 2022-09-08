import sys
import pandas as pd
from alert_factory.notification_rule_handler.notification_rule_handler import NotificationRuleHandler


class More10ErrorsInMinuteRuleHandler(NotificationRuleHandler):
    def __call__(self, *args, **kwargs) -> pd.DataFrame:
        return self._get_df_by_notification_rule(*args)

    def get_notification_rule_name(self) -> str:
        return 'More_10_errors_in_minute'

    def _get_df_by_notification_rule(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df = df.groupby([df['date'].map(lambda t: t.year).rename('year'),
                             df['date'].map(lambda t: t.month).rename('month'),
                             df['date'].map(lambda t: t.day).rename('day'),
                             df['date'].map(lambda t: t.hour).rename('hour'),
                             df['date'].map(lambda t: t.minute).rename('minute')]
                            ).agg(errors_count=('severity', 'count')).reset_index()

            df = df[df['errors_count'] > 10]
            df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']])
            return df[['date', 'errors_count']]
        except Exception as e:
            traceback = sys.exc_info()[2]
            print(e.with_traceback(traceback), file=sys.stderr)