from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetNodesStatisticsResponseDtoResponseLastSevenDaysItem")


@_attrs_define
class GetNodesStatisticsResponseDtoResponseLastSevenDaysItem:
    """
    Attributes:
        node_name (str):
        date (str):
        total_bytes (str):
    """

    node_name: str
    date: str
    total_bytes: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_name = self.node_name

        date = self.date

        total_bytes = self.total_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeName": node_name,
                "date": date,
                "totalBytes": total_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_name = d.pop("nodeName")

        date = d.pop("date")

        total_bytes = d.pop("totalBytes")

        get_nodes_statistics_response_dto_response_last_seven_days_item = cls(
            node_name=node_name,
            date=date,
            total_bytes=total_bytes,
        )

        get_nodes_statistics_response_dto_response_last_seven_days_item.additional_properties = d
        return get_nodes_statistics_response_dto_response_last_seven_days_item

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
