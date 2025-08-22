from enum import Enum


class UpdateHostRequestDtoSecurityLayer(str, Enum):
    DEFAULT = "DEFAULT"
    NONE = "NONE"
    TLS = "TLS"

    def __str__(self) -> str:
        return str(self.value)
