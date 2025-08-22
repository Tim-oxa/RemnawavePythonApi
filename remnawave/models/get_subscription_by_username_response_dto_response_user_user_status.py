from enum import Enum


class GetSubscriptionByUsernameResponseDtoResponseUserUserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"
    LIMITED = "LIMITED"

    def __str__(self) -> str:
        return str(self.value)
