from enum import Enum


class GetSubscriptionByUsernameResponseDtoResponseUserTrafficLimitStrategy(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"
    NO_RESET = "NO_RESET"
    WEEK = "WEEK"

    def __str__(self) -> str:
        return str(self.value)
