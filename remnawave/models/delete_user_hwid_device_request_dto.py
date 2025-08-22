from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteUserHwidDeviceRequestDto")


@_attrs_define
class DeleteUserHwidDeviceRequestDto:
    """
    Attributes:
        user_uuid (UUID):
        hwid (str):
    """

    user_uuid: UUID
    hwid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_uuid = str(self.user_uuid)

        hwid = self.hwid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "hwid": hwid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_uuid = UUID(d.pop("userUuid"))

        hwid = d.pop("hwid")

        delete_user_hwid_device_request_dto = cls(
            user_uuid=user_uuid,
            hwid=hwid,
        )

        delete_user_hwid_device_request_dto.additional_properties = d
        return delete_user_hwid_device_request_dto

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
