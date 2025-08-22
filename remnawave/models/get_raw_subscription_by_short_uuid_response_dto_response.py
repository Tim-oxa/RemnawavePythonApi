from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_headers import (
        GetRawSubscriptionByShortUuidResponseDtoResponseHeaders,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_user import (
        GetRawSubscriptionByShortUuidResponseDtoResponseUser,
    )


T = TypeVar("T", bound="GetRawSubscriptionByShortUuidResponseDtoResponse")


@_attrs_define
class GetRawSubscriptionByShortUuidResponseDtoResponse:
    """
    Attributes:
        user (GetRawSubscriptionByShortUuidResponseDtoResponseUser):
        subscription_url (str):
        raw_hosts (list['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem']):
        headers (GetRawSubscriptionByShortUuidResponseDtoResponseHeaders):
        is_hwid_limited (bool):
    """

    user: "GetRawSubscriptionByShortUuidResponseDtoResponseUser"
    subscription_url: str
    raw_hosts: list["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem"]
    headers: "GetRawSubscriptionByShortUuidResponseDtoResponseHeaders"
    is_hwid_limited: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        subscription_url = self.subscription_url

        raw_hosts = []
        for raw_hosts_item_data in self.raw_hosts:
            raw_hosts_item = raw_hosts_item_data.to_dict()
            raw_hosts.append(raw_hosts_item)

        headers = self.headers.to_dict()

        is_hwid_limited = self.is_hwid_limited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "subscriptionUrl": subscription_url,
                "rawHosts": raw_hosts,
                "headers": headers,
                "isHwidLimited": is_hwid_limited,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_headers import (
            GetRawSubscriptionByShortUuidResponseDtoResponseHeaders,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_user import (
            GetRawSubscriptionByShortUuidResponseDtoResponseUser,
        )

        d = dict(src_dict)
        user = GetRawSubscriptionByShortUuidResponseDtoResponseUser.from_dict(d.pop("user"))

        subscription_url = d.pop("subscriptionUrl")

        raw_hosts = []
        _raw_hosts = d.pop("rawHosts")
        for raw_hosts_item_data in _raw_hosts:
            raw_hosts_item = GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem.from_dict(raw_hosts_item_data)

            raw_hosts.append(raw_hosts_item)

        headers = GetRawSubscriptionByShortUuidResponseDtoResponseHeaders.from_dict(d.pop("headers"))

        is_hwid_limited = d.pop("isHwidLimited")

        get_raw_subscription_by_short_uuid_response_dto_response = cls(
            user=user,
            subscription_url=subscription_url,
            raw_hosts=raw_hosts,
            headers=headers,
            is_hwid_limited=is_hwid_limited,
        )

        get_raw_subscription_by_short_uuid_response_dto_response.additional_properties = d
        return get_raw_subscription_by_short_uuid_response_dto_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
