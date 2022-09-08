from alert_factory.alert_factory import AlertFactory
from alert_factory.error_level_handler.fatal_error_handler import FatalErrorHandler
from alert_factory.notification_rule_handler.more_10_errors_in_hour_with_bundle_rule_handler import More10ErrorsInHourWithBundleRuleHandler


class More10FatalErrorsInHourWithBundleFactory(AlertFactory):
    def get_error_level_handler(self) -> FatalErrorHandler:
        return FatalErrorHandler()

    def get_notification_rule_handler(self) -> More10ErrorsInHourWithBundleRuleHandler:
        return More10ErrorsInHourWithBundleRuleHandler()
