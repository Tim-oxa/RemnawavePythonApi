from enum import Enum


class SubscriptionControllerGetSubscriptionByClientTypeClientType(str, Enum):
    CLASH = "clash"
    JSON = "json"
    MIHOMO = "mihomo"
    SINGBOX = "singbox"
    SINGBOX_LEGACY = "singbox-legacy"
    STASH = "stash"
    V2RAY_JSON = "v2ray-json"

    def __str__(self) -> str:
        return str(self.value)
