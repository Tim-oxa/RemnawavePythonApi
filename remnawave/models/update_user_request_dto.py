import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_user_request_dto_status import UpdateUserRequestDtoStatus
from ..models.update_user_request_dto_traffic_limit_strategy import UpdateUserRequestDtoTrafficLimitStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserRequestDto")


@_attrs_define
class UpdateUserRequestDto:
    """
    Attributes:
        uuid (UUID):
        status (Union[Unset, UpdateUserRequestDtoStatus]):
        traffic_limit_bytes (Union[Unset, int]): Traffic limit in bytes. 0 - unlimited
        traffic_limit_strategy (Union[Unset, UpdateUserRequestDtoTrafficLimitStrategy]): Available reset periods
            Default: UpdateUserRequestDtoTrafficLimitStrategy.NO_RESET.
        expire_at (Union[Unset, datetime.datetime]): Expiration date: 2025-01-17T15:38:45.065Z
        description (Union[None, Unset, str]):
        tag (Union[None, Unset, str]):
        telegram_id (Union[None, Unset, int]):
        email (Union[None, Unset, str]):
        hwid_device_limit (Union[None, Unset, int]):
        active_internal_squads (Union[Unset, list[UUID]]):
    """

    uuid: UUID
    status: Union[Unset, UpdateUserRequestDtoStatus] = UNSET
    traffic_limit_bytes: Union[Unset, int] = UNSET
    traffic_limit_strategy: Union[Unset, UpdateUserRequestDtoTrafficLimitStrategy] = (
        UpdateUserRequestDtoTrafficLimitStrategy.NO_RESET
    )
    expire_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET
    tag: Union[None, Unset, str] = UNSET
    telegram_id: Union[None, Unset, int] = UNSET
    email: Union[None, Unset, str] = UNSET
    hwid_device_limit: Union[None, Unset, int] = UNSET
    active_internal_squads: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        traffic_limit_bytes = self.traffic_limit_bytes

        traffic_limit_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.traffic_limit_strategy, Unset):
            traffic_limit_strategy = self.traffic_limit_strategy.value

        expire_at: Union[Unset, str] = UNSET
        if not isinstance(self.expire_at, Unset):
            expire_at = self.expire_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tag: Union[None, Unset, str]
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        telegram_id: Union[None, Unset, int]
        if isinstance(self.telegram_id, Unset):
            telegram_id = UNSET
        else:
            telegram_id = self.telegram_id

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        hwid_device_limit: Union[None, Unset, int]
        if isinstance(self.hwid_device_limit, Unset):
            hwid_device_limit = UNSET
        else:
            hwid_device_limit = self.hwid_device_limit

        active_internal_squads: Union[Unset, list[str]] = UNSET
        if not isinstance(self.active_internal_squads, Unset):
            active_internal_squads = []
            for active_internal_squads_item_data in self.active_internal_squads:
                active_internal_squads_item = str(active_internal_squads_item_data)
                active_internal_squads.append(active_internal_squads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if traffic_limit_bytes is not UNSET:
            field_dict["trafficLimitBytes"] = traffic_limit_bytes
        if traffic_limit_strategy is not UNSET:
            field_dict["trafficLimitStrategy"] = traffic_limit_strategy
        if expire_at is not UNSET:
            field_dict["expireAt"] = expire_at
        if description is not UNSET:
            field_dict["description"] = description
        if tag is not UNSET:
            field_dict["tag"] = tag
        if telegram_id is not UNSET:
            field_dict["telegramId"] = telegram_id
        if email is not UNSET:
            field_dict["email"] = email
        if hwid_device_limit is not UNSET:
            field_dict["hwidDeviceLimit"] = hwid_device_limit
        if active_internal_squads is not UNSET:
            field_dict["activeInternalSquads"] = active_internal_squads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateUserRequestDtoStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateUserRequestDtoStatus(_status)

        traffic_limit_bytes = d.pop("trafficLimitBytes", UNSET)

        _traffic_limit_strategy = d.pop("trafficLimitStrategy", UNSET)
        traffic_limit_strategy: Union[Unset, UpdateUserRequestDtoTrafficLimitStrategy]
        if isinstance(_traffic_limit_strategy, Unset):
            traffic_limit_strategy = UNSET
        else:
            traffic_limit_strategy = UpdateUserRequestDtoTrafficLimitStrategy(_traffic_limit_strategy)

        _expire_at = d.pop("expireAt", UNSET)
        expire_at: Union[Unset, datetime.datetime]
        if isinstance(_expire_at, Unset):
            expire_at = UNSET
        else:
            expire_at = isoparse(_expire_at)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag = _parse_tag(d.pop("tag", UNSET))

        def _parse_telegram_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        telegram_id = _parse_telegram_id(d.pop("telegramId", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_hwid_device_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        hwid_device_limit = _parse_hwid_device_limit(d.pop("hwidDeviceLimit", UNSET))

        active_internal_squads = []
        _active_internal_squads = d.pop("activeInternalSquads", UNSET)
        for active_internal_squads_item_data in _active_internal_squads or []:
            active_internal_squads_item = UUID(active_internal_squads_item_data)

            active_internal_squads.append(active_internal_squads_item)

        update_user_request_dto = cls(
            uuid=uuid,
            status=status,
            traffic_limit_bytes=traffic_limit_bytes,
            traffic_limit_strategy=traffic_limit_strategy,
            expire_at=expire_at,
            description=description,
            tag=tag,
            telegram_id=telegram_id,
            email=email,
            hwid_device_limit=hwid_device_limit,
            active_internal_squads=active_internal_squads,
        )

        update_user_request_dto.additional_properties = d
        return update_user_request_dto

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
