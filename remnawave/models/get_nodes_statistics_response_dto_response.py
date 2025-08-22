from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_nodes_statistics_response_dto_response_last_seven_days_item import (
        GetNodesStatisticsResponseDtoResponseLastSevenDaysItem,
    )


T = TypeVar("T", bound="GetNodesStatisticsResponseDtoResponse")


@_attrs_define
class GetNodesStatisticsResponseDtoResponse:
    """
    Attributes:
        last_seven_days (list['GetNodesStatisticsResponseDtoResponseLastSevenDaysItem']):
    """

    last_seven_days: list["GetNodesStatisticsResponseDtoResponseLastSevenDaysItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_seven_days = []
        for last_seven_days_item_data in self.last_seven_days:
            last_seven_days_item = last_seven_days_item_data.to_dict()
            last_seven_days.append(last_seven_days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastSevenDays": last_seven_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_nodes_statistics_response_dto_response_last_seven_days_item import (
            GetNodesStatisticsResponseDtoResponseLastSevenDaysItem,
        )

        d = dict(src_dict)
        last_seven_days = []
        _last_seven_days = d.pop("lastSevenDays")
        for last_seven_days_item_data in _last_seven_days:
            last_seven_days_item = GetNodesStatisticsResponseDtoResponseLastSevenDaysItem.from_dict(
                last_seven_days_item_data
            )

            last_seven_days.append(last_seven_days_item)

        get_nodes_statistics_response_dto_response = cls(
            last_seven_days=last_seven_days,
        )

        get_nodes_statistics_response_dto_response.additional_properties = d
        return get_nodes_statistics_response_dto_response

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
