from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0SsType0")


@_attrs_define
class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0SsType0:
    """
    Attributes:
        method (Union[None, Unset, str]):
    """

    method: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: Union[None, Unset, str]
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        method = _parse_method(d.pop("method", UNSET))

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_protocol_options_type_0_ss_type_0 = cls(
            method=method,
        )

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_protocol_options_type_0_ss_type_0.additional_properties = d
        return get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_protocol_options_type_0_ss_type_0

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
