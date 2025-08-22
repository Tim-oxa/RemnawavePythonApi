from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_remnawave_health_response_dto_response_pm_2_stats_item import (
        GetRemnawaveHealthResponseDtoResponsePm2StatsItem,
    )


T = TypeVar("T", bound="GetRemnawaveHealthResponseDtoResponse")


@_attrs_define
class GetRemnawaveHealthResponseDtoResponse:
    """
    Attributes:
        pm_2_stats (list['GetRemnawaveHealthResponseDtoResponsePm2StatsItem']):
    """

    pm_2_stats: list["GetRemnawaveHealthResponseDtoResponsePm2StatsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pm_2_stats = []
        for pm_2_stats_item_data in self.pm_2_stats:
            pm_2_stats_item = pm_2_stats_item_data.to_dict()
            pm_2_stats.append(pm_2_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pm2Stats": pm_2_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_remnawave_health_response_dto_response_pm_2_stats_item import (
            GetRemnawaveHealthResponseDtoResponsePm2StatsItem,
        )

        d = dict(src_dict)
        pm_2_stats = []
        _pm_2_stats = d.pop("pm2Stats")
        for pm_2_stats_item_data in _pm_2_stats:
            pm_2_stats_item = GetRemnawaveHealthResponseDtoResponsePm2StatsItem.from_dict(pm_2_stats_item_data)

            pm_2_stats.append(pm_2_stats_item)

        get_remnawave_health_response_dto_response = cls(
            pm_2_stats=pm_2_stats,
        )

        get_remnawave_health_response_dto_response.additional_properties = d
        return get_remnawave_health_response_dto_response

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
