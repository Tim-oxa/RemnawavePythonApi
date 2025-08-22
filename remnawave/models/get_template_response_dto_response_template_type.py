from enum import Enum


class GetTemplateResponseDtoResponseTemplateType(str, Enum):
    CLASH = "CLASH"
    MIHOMO = "MIHOMO"
    SINGBOX = "SINGBOX"
    SINGBOX_LEGACY = "SINGBOX_LEGACY"
    STASH = "STASH"
    XRAY_JSON = "XRAY_JSON"

    def __str__(self) -> str:
        return str(self.value)
