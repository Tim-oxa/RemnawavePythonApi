from enum import Enum


class OAuth2AuthorizeRequestDtoProvider(str, Enum):
    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"

    def __str__(self) -> str:
        return str(self.value)
