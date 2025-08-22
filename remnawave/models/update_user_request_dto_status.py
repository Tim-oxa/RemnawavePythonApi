from enum import Enum


class UpdateUserRequestDtoStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
