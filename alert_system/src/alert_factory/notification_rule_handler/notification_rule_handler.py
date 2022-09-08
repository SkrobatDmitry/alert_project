import pandas as pd
from abc import ABC, abstractmethod


class NotificationRuleHandler(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_notification_rule_name(self) -> str:
        pass

    @abstractmethod
    def _get_df_by_notification_rule(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
