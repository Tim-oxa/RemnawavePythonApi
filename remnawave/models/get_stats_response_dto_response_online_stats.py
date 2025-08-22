from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetStatsResponseDtoResponseOnlineStats")


@_attrs_define
class GetStatsResponseDtoResponseOnlineStats:
    """
    Attributes:
        last_day (float):
        last_week (float):
        never_online (float):
        online_now (float):
    """

    last_day: float
    last_week: float
    never_online: float
    online_now: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_day = self.last_day

        last_week = self.last_week

        never_online = self.never_online

        online_now = self.online_now

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastDay": last_day,
                "lastWeek": last_week,
                "neverOnline": never_online,
                "onlineNow": online_now,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_day = d.pop("lastDay")

        last_week = d.pop("lastWeek")

        never_online = d.pop("neverOnline")

        online_now = d.pop("onlineNow")

        get_stats_response_dto_response_online_stats = cls(
            last_day=last_day,
            last_week=last_week,
            never_online=never_online,
            online_now=online_now,
        )

        get_stats_response_dto_response_online_stats.additional_properties = d
        return get_stats_response_dto_response_online_stats

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
