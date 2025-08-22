from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetStatsResponseDtoResponseCpu")


@_attrs_define
class GetStatsResponseDtoResponseCpu:
    """
    Attributes:
        cores (float):
        physical_cores (float):
    """

    cores: float
    physical_cores: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cores = self.cores

        physical_cores = self.physical_cores

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cores": cores,
                "physicalCores": physical_cores,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cores = d.pop("cores")

        physical_cores = d.pop("physicalCores")

        get_stats_response_dto_response_cpu = cls(
            cores=cores,
            physical_cores=physical_cores,
        )

        get_stats_response_dto_response_cpu.additional_properties = d
        return get_stats_response_dto_response_cpu

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
