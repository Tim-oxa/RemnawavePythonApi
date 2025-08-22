from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_stats_response_dto_response_users_status_counts import (
        GetStatsResponseDtoResponseUsersStatusCounts,
    )


T = TypeVar("T", bound="GetStatsResponseDtoResponseUsers")


@_attrs_define
class GetStatsResponseDtoResponseUsers:
    """
    Attributes:
        status_counts (GetStatsResponseDtoResponseUsersStatusCounts):
        total_users (float):
        total_traffic_bytes (str):
    """

    status_counts: "GetStatsResponseDtoResponseUsersStatusCounts"
    total_users: float
    total_traffic_bytes: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_counts = self.status_counts.to_dict()

        total_users = self.total_users

        total_traffic_bytes = self.total_traffic_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCounts": status_counts,
                "totalUsers": total_users,
                "totalTrafficBytes": total_traffic_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_stats_response_dto_response_users_status_counts import (
            GetStatsResponseDtoResponseUsersStatusCounts,
        )

        d = dict(src_dict)
        status_counts = GetStatsResponseDtoResponseUsersStatusCounts.from_dict(d.pop("statusCounts"))

        total_users = d.pop("totalUsers")

        total_traffic_bytes = d.pop("totalTrafficBytes")

        get_stats_response_dto_response_users = cls(
            status_counts=status_counts,
            total_users=total_users,
            total_traffic_bytes=total_traffic_bytes,
        )

        get_stats_response_dto_response_users.additional_properties = d
        return get_stats_response_dto_response_users

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
