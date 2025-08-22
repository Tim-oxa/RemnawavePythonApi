from enum import Enum


class CreateHostRequestDtoAlpn(str, Enum):
    H2 = "h2"
    H2HTTP1_1 = "h2,http/1.1"
    H3 = "h3"
    H3H2 = "h3,h2"
    H3H2HTTP1_1 = "h3,h2,http/1.1"
    HTTP1_1 = "http/1.1"

    def __str__(self) -> str:
        return str(self.value)
