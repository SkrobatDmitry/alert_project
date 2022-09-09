# Alert system
`Alert system` - a system that can process and analyze logs and catch errors.

## Observer
In order to start processing files as soon as they arrive, the `Observer` behavioral design pattern was implemented. The `Observer` monitors the folder where the logs come from and notifies subscribers about this when a new file arrives.
```python
class Checker:
    @staticmethod
    def watch(path: str, callback) -> None:
        event_handler = FileEventHandler(callback)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=False)
        observer.start()
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
```

## Abstract factory
An `Abstract Factory` was used to create alert rules. An `Abstract Factory` is a generative design pattern that allows you to create families of related objects without being tied to the specific classes of objects you create.

An `Abstract Factory` hides from the client code the details of how and what specific objects will be created. But at the same time, the client code can work with all types of created handlers, since their common interface has been predefined. This is very handy for creating new notification rules, as you can easily create new objects for the factory or combine existing ones.

### Сreate new alert rules
To create a new alert rule, simply create a new class that inherits from the `Alert Factory` abstract class and put it in the factories list found in `log_handler.py[27]`.
```python
class AlertFactory(ABC):
    @abstractmethod
    def get_error_level_handler(self) -> ErrorLevelHandler:
        pass

    @abstractmethod
    def get_notification_rule_handler(self) -> NotificationRuleHandler:
        pass
```

Next, you just need to create your own rule handlers or use existing ones. To create your own handlers, you need to inherit from the abstract classes `Error Level Handler` and `Notification Rule Handler`.
```python
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
```

## The result of the program
As a result of the program, csv files are created for each notification rule.

- First 5 lines alerting more than 10 fatal errors in less than one minute: 
```text
date,errors_count
2021-09-11 00:00:00,35
2021-09-11 00:01:00,128
2021-09-11 00:02:00,133
2021-09-11 00:03:00,144
```

- First 5 lines alerting more than 10 fatal errors in less than one hour for a specific bundle id:
```text
date,bundle_id,errors_count
2021-09-11 00:00:00,com.mytalkingcatemma.ballerinagames,116
2021-09-11 01:00:00,com.mytalkingcatemma.ballerinagames,131
2021-09-11 02:00:00,com.mytalkingcatemma.ballerinagames,4537
2021-09-11 03:00:00,com.mytalkingcatemma.ballerinagames,16340
```