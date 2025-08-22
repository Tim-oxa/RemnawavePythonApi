from enum import Enum


class GetUserByUuidResponseDtoResponseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"
    LIMITED = "LIMITED"

    def __str__(self) -> str:
        return str(self.value)
