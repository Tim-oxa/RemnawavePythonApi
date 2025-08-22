from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserHwidDeviceRequestDto")


@_attrs_define
class CreateUserHwidDeviceRequestDto:
    """
    Attributes:
        hwid (str):
        user_uuid (UUID):
        platform (Union[Unset, str]):
        os_version (Union[Unset, str]):
        device_model (Union[Unset, str]):
        user_agent (Union[Unset, str]):
    """

    hwid: str
    user_uuid: UUID
    platform: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    device_model: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hwid = self.hwid

        user_uuid = str(self.user_uuid)

        platform = self.platform

        os_version = self.os_version

        device_model = self.device_model

        user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hwid": hwid,
                "userUuid": user_uuid,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if os_version is not UNSET:
            field_dict["osVersion"] = os_version
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hwid = d.pop("hwid")

        user_uuid = UUID(d.pop("userUuid"))

        platform = d.pop("platform", UNSET)

        os_version = d.pop("osVersion", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        create_user_hwid_device_request_dto = cls(
            hwid=hwid,
            user_uuid=user_uuid,
            platform=platform,
            os_version=os_version,
            device_model=device_model,
            user_agent=user_agent,
        )

        create_user_hwid_device_request_dto.additional_properties = d
        return create_user_hwid_device_request_dto

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
