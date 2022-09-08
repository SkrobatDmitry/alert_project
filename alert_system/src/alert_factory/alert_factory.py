from abc import ABC, abstractmethod
from alert_factory.error_level_handler.error_level_handler import ErrorLevelHandler
from alert_factory.notification_rule_handler.notification_rule_handler import NotificationRuleHandler


class AlertFactory(ABC):
    @abstractmethod
    def get_error_level_handler(self) -> ErrorLevelHandler:
        pass

    @abstractmethod
    def get_notification_rule_handler(self) -> NotificationRuleHandler:
        pass
