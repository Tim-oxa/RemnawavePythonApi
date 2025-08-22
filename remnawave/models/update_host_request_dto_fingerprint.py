from enum import Enum


class UpdateHostRequestDtoFingerprint(str, Enum):
    ANDROID = "android"
    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    IOS = "ios"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"
    SAFARI = "safari"

    def __str__(self) -> str:
        return str(self.value)
