import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetUserHwidDevicesResponseDtoResponseDevicesItem")


@_attrs_define
class GetUserHwidDevicesResponseDtoResponseDevicesItem:
    """
    Attributes:
        hwid (str):
        user_uuid (UUID):
        platform (Union[None, str]):
        os_version (Union[None, str]):
        device_model (Union[None, str]):
        user_agent (Union[None, str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    hwid: str
    user_uuid: UUID
    platform: Union[None, str]
    os_version: Union[None, str]
    device_model: Union[None, str]
    user_agent: Union[None, str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hwid = self.hwid

        user_uuid = str(self.user_uuid)

        platform: Union[None, str]
        platform = self.platform

        os_version: Union[None, str]
        os_version = self.os_version

        device_model: Union[None, str]
        device_model = self.device_model

        user_agent: Union[None, str]
        user_agent = self.user_agent

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hwid": hwid,
                "userUuid": user_uuid,
                "platform": platform,
                "osVersion": os_version,
                "deviceModel": device_model,
                "userAgent": user_agent,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hwid = d.pop("hwid")

        user_uuid = UUID(d.pop("userUuid"))

        def _parse_platform(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        platform = _parse_platform(d.pop("platform"))

        def _parse_os_version(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        os_version = _parse_os_version(d.pop("osVersion"))

        def _parse_device_model(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        device_model = _parse_device_model(d.pop("deviceModel"))

        def _parse_user_agent(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_agent = _parse_user_agent(d.pop("userAgent"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        get_user_hwid_devices_response_dto_response_devices_item = cls(
            hwid=hwid,
            user_uuid=user_uuid,
            platform=platform,
            os_version=os_version,
            device_model=device_model,
            user_agent=user_agent,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_user_hwid_devices_response_dto_response_devices_item.additional_properties = d
        return get_user_hwid_devices_response_dto_response_devices_item

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
