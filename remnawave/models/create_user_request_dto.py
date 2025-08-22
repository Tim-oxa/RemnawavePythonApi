import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_user_request_dto_status import CreateUserRequestDtoStatus
from ..models.create_user_request_dto_traffic_limit_strategy import CreateUserRequestDtoTrafficLimitStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserRequestDto")


@_attrs_define
class CreateUserRequestDto:
    """
    Attributes:
        username (str): Unique username for the user. Required. Must be 3-36 characters long and contain only letters,
            numbers, underscores and dashes.
        expire_at (datetime.datetime): Account expiration date. Required. Format: 2025-01-17T15:38:45.065Z
        status (Union[Unset, CreateUserRequestDtoStatus]): Optional. User account status. Defaults to ACTIVE. Default:
            CreateUserRequestDtoStatus.ACTIVE.
        short_uuid (Union[Unset, str]): Optional. Short UUID identifier for the user.
        trojan_password (Union[Unset, str]): Optional. Password for Trojan protocol. Must be 8-32 characters.
        vless_uuid (Union[Unset, UUID]): Optional. UUID for VLESS protocol. Must be a valid UUID format.
        ss_password (Union[Unset, str]): Optional. Password for Shadowsocks protocol. Must be 8-32 characters.
        traffic_limit_bytes (Union[Unset, int]): Optional. Traffic limit in bytes. Set to 0 for unlimited traffic.
        traffic_limit_strategy (Union[Unset, CreateUserRequestDtoTrafficLimitStrategy]): Available reset periods
            Default: CreateUserRequestDtoTrafficLimitStrategy.NO_RESET.
        created_at (Union[Unset, datetime.datetime]): Optional. Account creation date. Format: 2025-01-17T15:38:45.065Z
        last_traffic_reset_at (Union[Unset, datetime.datetime]): Optional. Date of last traffic reset. Format:
            2025-01-17T15:38:45.065Z
        description (Union[Unset, str]): Optional. Additional notes or description for the user account.
        tag (Union[None, Unset, str]): Optional. User tag for categorization. Max 16 characters, uppercase letters,
            numbers and underscores only.
        telegram_id (Union[None, Unset, int]): Optional. Telegram user ID for notifications. Must be an integer.
        email (Union[None, Unset, str]): Optional. User email address. Must be a valid email format.
        hwid_device_limit (Union[Unset, int]): Optional. Maximum number of hardware devices allowed. Must be a positive
            integer.
        active_internal_squads (Union[Unset, list[UUID]]): Optional. Array of UUIDs representing enabled internal
            squads.
    """

    username: str
    expire_at: datetime.datetime
    status: Union[Unset, CreateUserRequestDtoStatus] = CreateUserRequestDtoStatus.ACTIVE
    short_uuid: Union[Unset, str] = UNSET
    trojan_password: Union[Unset, str] = UNSET
    vless_uuid: Union[Unset, UUID] = UNSET
    ss_password: Union[Unset, str] = UNSET
    traffic_limit_bytes: Union[Unset, int] = UNSET
    traffic_limit_strategy: Union[Unset, CreateUserRequestDtoTrafficLimitStrategy] = (
        CreateUserRequestDtoTrafficLimitStrategy.NO_RESET
    )
    created_at: Union[Unset, datetime.datetime] = UNSET
    last_traffic_reset_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    tag: Union[None, Unset, str] = UNSET
    telegram_id: Union[None, Unset, int] = UNSET
    email: Union[None, Unset, str] = UNSET
    hwid_device_limit: Union[Unset, int] = UNSET
    active_internal_squads: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        expire_at = self.expire_at.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        short_uuid = self.short_uuid

        trojan_password = self.trojan_password

        vless_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.vless_uuid, Unset):
            vless_uuid = str(self.vless_uuid)

        ss_password = self.ss_password

        traffic_limit_bytes = self.traffic_limit_bytes

        traffic_limit_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.traffic_limit_strategy, Unset):
            traffic_limit_strategy = self.traffic_limit_strategy.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        last_traffic_reset_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_traffic_reset_at, Unset):
            last_traffic_reset_at = self.last_traffic_reset_at.isoformat()

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
                "username": username,
                "expireAt": expire_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if short_uuid is not UNSET:
            field_dict["shortUuid"] = short_uuid
        if trojan_password is not UNSET:
            field_dict["trojanPassword"] = trojan_password
        if vless_uuid is not UNSET:
            field_dict["vlessUuid"] = vless_uuid
        if ss_password is not UNSET:
            field_dict["ssPassword"] = ss_password
        if traffic_limit_bytes is not UNSET:
            field_dict["trafficLimitBytes"] = traffic_limit_bytes
        if traffic_limit_strategy is not UNSET:
            field_dict["trafficLimitStrategy"] = traffic_limit_strategy
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_traffic_reset_at is not UNSET:
            field_dict["lastTrafficResetAt"] = last_traffic_reset_at
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
        username = d.pop("username")

        expire_at = isoparse(d.pop("expireAt"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateUserRequestDtoStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateUserRequestDtoStatus(_status)

        short_uuid = d.pop("shortUuid", UNSET)

        trojan_password = d.pop("trojanPassword", UNSET)

        _vless_uuid = d.pop("vlessUuid", UNSET)
        vless_uuid: Union[Unset, UUID]
        if isinstance(_vless_uuid, Unset):
            vless_uuid = UNSET
        else:
            vless_uuid = UUID(_vless_uuid)

        ss_password = d.pop("ssPassword", UNSET)

        traffic_limit_bytes = d.pop("trafficLimitBytes", UNSET)

        _traffic_limit_strategy = d.pop("trafficLimitStrategy", UNSET)
        traffic_limit_strategy: Union[Unset, CreateUserRequestDtoTrafficLimitStrategy]
        if isinstance(_traffic_limit_strategy, Unset):
            traffic_limit_strategy = UNSET
        else:
            traffic_limit_strategy = CreateUserRequestDtoTrafficLimitStrategy(_traffic_limit_strategy)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _last_traffic_reset_at = d.pop("lastTrafficResetAt", UNSET)
        last_traffic_reset_at: Union[Unset, datetime.datetime]
        if isinstance(_last_traffic_reset_at, Unset):
            last_traffic_reset_at = UNSET
        else:
            last_traffic_reset_at = isoparse(_last_traffic_reset_at)

        description = d.pop("description", UNSET)

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

        hwid_device_limit = d.pop("hwidDeviceLimit", UNSET)

        active_internal_squads = []
        _active_internal_squads = d.pop("activeInternalSquads", UNSET)
        for active_internal_squads_item_data in _active_internal_squads or []:
            active_internal_squads_item = UUID(active_internal_squads_item_data)

            active_internal_squads.append(active_internal_squads_item)

        create_user_request_dto = cls(
            username=username,
            expire_at=expire_at,
            status=status,
            short_uuid=short_uuid,
            trojan_password=trojan_password,
            vless_uuid=vless_uuid,
            ss_password=ss_password,
            traffic_limit_bytes=traffic_limit_bytes,
            traffic_limit_strategy=traffic_limit_strategy,
            created_at=created_at,
            last_traffic_reset_at=last_traffic_reset_at,
            description=description,
            tag=tag,
            telegram_id=telegram_id,
            email=email,
            hwid_device_limit=hwid_device_limit,
            active_internal_squads=active_internal_squads,
        )

        create_user_request_dto.additional_properties = d
        return create_user_request_dto

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
