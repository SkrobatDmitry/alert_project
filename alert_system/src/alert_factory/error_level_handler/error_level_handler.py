import pandas as pd
from abc import ABC, abstractmethod


class ErrorLevelHandler(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_error_level_name(self) -> str:
        pass

    @abstractmethod
    def _get_df_by_error_level(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
