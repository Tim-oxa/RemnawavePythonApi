from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0")


@_attrs_define
class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0:
    """
    Attributes:
        mode (Union[None, Unset, str]):
        heartbeat_period (Union[None, Unset, float]):
    """

    mode: Union[None, Unset, str] = UNSET
    heartbeat_period: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[None, Unset, str]
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        heartbeat_period: Union[None, Unset, float]
        if isinstance(self.heartbeat_period, Unset):
            heartbeat_period = UNSET
        else:
            heartbeat_period = self.heartbeat_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if heartbeat_period is not UNSET:
            field_dict["heartbeatPeriod"] = heartbeat_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_heartbeat_period(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        heartbeat_period = _parse_heartbeat_period(d.pop("heartbeatPeriod", UNSET))

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_additional_params_type_0 = cls(
            mode=mode,
            heartbeat_period=heartbeat_period,
        )

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_additional_params_type_0.additional_properties = d
        return get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_additional_params_type_0

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
