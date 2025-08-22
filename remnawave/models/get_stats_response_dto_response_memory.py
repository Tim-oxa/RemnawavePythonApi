from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetStatsResponseDtoResponseMemory")


@_attrs_define
class GetStatsResponseDtoResponseMemory:
    """
    Attributes:
        total (float):
        free (float):
        used (float):
        active (float):
        available (float):
    """

    total: float
    free: float
    used: float
    active: float
    available: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        free = self.free

        used = self.used

        active = self.active

        available = self.available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "free": free,
                "used": used,
                "active": active,
                "available": available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        free = d.pop("free")

        used = d.pop("used")

        active = d.pop("active")

        available = d.pop("available")

        get_stats_response_dto_response_memory = cls(
            total=total,
            free=free,
            used=used,
            active=active,
            available=available,
        )

        get_stats_response_dto_response_memory.additional_properties = d
        return get_stats_response_dto_response_memory

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
