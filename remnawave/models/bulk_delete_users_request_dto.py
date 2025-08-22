from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkDeleteUsersRequestDto")


@_attrs_define
class BulkDeleteUsersRequestDto:
    """
    Attributes:
        uuids (list[UUID]):
    """

    uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuids = []
        for uuids_item_data in self.uuids:
            uuids_item = str(uuids_item_data)
            uuids.append(uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuids": uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuids = []
        _uuids = d.pop("uuids")
        for uuids_item_data in _uuids:
            uuids_item = UUID(uuids_item_data)

            uuids.append(uuids_item)

        bulk_delete_users_request_dto = cls(
            uuids=uuids,
        )

        bulk_delete_users_request_dto.additional_properties = d
        return bulk_delete_users_request_dto

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
