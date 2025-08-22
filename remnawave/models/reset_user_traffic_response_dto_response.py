import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reset_user_traffic_response_dto_response_status import ResetUserTrafficResponseDtoResponseStatus
from ..models.reset_user_traffic_response_dto_response_traffic_limit_strategy import (
    ResetUserTrafficResponseDtoResponseTrafficLimitStrategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reset_user_traffic_response_dto_response_active_internal_squads_item import (
        ResetUserTrafficResponseDtoResponseActiveInternalSquadsItem,
    )
    from ..models.reset_user_traffic_response_dto_response_happ import ResetUserTrafficResponseDtoResponseHapp
    from ..models.reset_user_traffic_response_dto_response_last_connected_node_type_0 import (
        ResetUserTrafficResponseDtoResponseLastConnectedNodeType0,
    )


T = TypeVar("T", bound="ResetUserTrafficResponseDtoResponse")


@_attrs_define
class ResetUserTrafficResponseDtoResponse:
    """
    Attributes:
        uuid (UUID):
        short_uuid (str):
        username (str):
        used_traffic_bytes (float):
        lifetime_used_traffic_bytes (float):
        sub_last_user_agent (Union[None, str]):
        sub_last_opened_at (Union[None, datetime.datetime]):
        expire_at (datetime.datetime):
        online_at (Union[None, datetime.datetime]):
        sub_revoked_at (Union[None, datetime.datetime]):
        last_traffic_reset_at (Union[None, datetime.datetime]):
        trojan_password (str):
        vless_uuid (UUID):
        ss_password (str):
        description (Union[None, str]):
        tag (Union[None, str]):
        telegram_id (Union[None, int]):
        email (Union[None, str]):
        hwid_device_limit (Union[None, int]):
        first_connected_at (Union[None, datetime.datetime]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        active_internal_squads (list['ResetUserTrafficResponseDtoResponseActiveInternalSquadsItem']):
        subscription_url (str):
        last_connected_node (Union['ResetUserTrafficResponseDtoResponseLastConnectedNodeType0', None]):
        happ (ResetUserTrafficResponseDtoResponseHapp):
        status (Union[Unset, ResetUserTrafficResponseDtoResponseStatus]):  Default:
            ResetUserTrafficResponseDtoResponseStatus.ACTIVE.
        traffic_limit_bytes (Union[Unset, int]):  Default: 0.
        traffic_limit_strategy (Union[Unset, ResetUserTrafficResponseDtoResponseTrafficLimitStrategy]): Available reset
            periods Default: ResetUserTrafficResponseDtoResponseTrafficLimitStrategy.NO_RESET.
        last_triggered_threshold (Union[Unset, int]):  Default: 0.
    """

    uuid: UUID
    short_uuid: str
    username: str
    used_traffic_bytes: float
    lifetime_used_traffic_bytes: float
    sub_last_user_agent: Union[None, str]
    sub_last_opened_at: Union[None, datetime.datetime]
    expire_at: datetime.datetime
    online_at: Union[None, datetime.datetime]
    sub_revoked_at: Union[None, datetime.datetime]
    last_traffic_reset_at: Union[None, datetime.datetime]
    trojan_password: str
    vless_uuid: UUID
    ss_password: str
    description: Union[None, str]
    tag: Union[None, str]
    telegram_id: Union[None, int]
    email: Union[None, str]
    hwid_device_limit: Union[None, int]
    first_connected_at: Union[None, datetime.datetime]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    active_internal_squads: list["ResetUserTrafficResponseDtoResponseActiveInternalSquadsItem"]
    subscription_url: str
    last_connected_node: Union["ResetUserTrafficResponseDtoResponseLastConnectedNodeType0", None]
    happ: "ResetUserTrafficResponseDtoResponseHapp"
    status: Union[Unset, ResetUserTrafficResponseDtoResponseStatus] = ResetUserTrafficResponseDtoResponseStatus.ACTIVE
    traffic_limit_bytes: Union[Unset, int] = 0
    traffic_limit_strategy: Union[Unset, ResetUserTrafficResponseDtoResponseTrafficLimitStrategy] = (
        ResetUserTrafficResponseDtoResponseTrafficLimitStrategy.NO_RESET
    )
    last_triggered_threshold: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reset_user_traffic_response_dto_response_last_connected_node_type_0 import (
            ResetUserTrafficResponseDtoResponseLastConnectedNodeType0,
        )

        uuid = str(self.uuid)

        short_uuid = self.short_uuid

        username = self.username

        used_traffic_bytes = self.used_traffic_bytes

        lifetime_used_traffic_bytes = self.lifetime_used_traffic_bytes

        sub_last_user_agent: Union[None, str]
        sub_last_user_agent = self.sub_last_user_agent

        sub_last_opened_at: Union[None, str]
        if isinstance(self.sub_last_opened_at, datetime.datetime):
            sub_last_opened_at = self.sub_last_opened_at.isoformat()
        else:
            sub_last_opened_at = self.sub_last_opened_at

        expire_at = self.expire_at.isoformat()

        online_at: Union[None, str]
        if isinstance(self.online_at, datetime.datetime):
            online_at = self.online_at.isoformat()
        else:
            online_at = self.online_at

        sub_revoked_at: Union[None, str]
        if isinstance(self.sub_revoked_at, datetime.datetime):
            sub_revoked_at = self.sub_revoked_at.isoformat()
        else:
            sub_revoked_at = self.sub_revoked_at

        last_traffic_reset_at: Union[None, str]
        if isinstance(self.last_traffic_reset_at, datetime.datetime):
            last_traffic_reset_at = self.last_traffic_reset_at.isoformat()
        else:
            last_traffic_reset_at = self.last_traffic_reset_at

        trojan_password = self.trojan_password

        vless_uuid = str(self.vless_uuid)

        ss_password = self.ss_password

        description: Union[None, str]
        description = self.description

        tag: Union[None, str]
        tag = self.tag

        telegram_id: Union[None, int]
        telegram_id = self.telegram_id

        email: Union[None, str]
        email = self.email

        hwid_device_limit: Union[None, int]
        hwid_device_limit = self.hwid_device_limit

        first_connected_at: Union[None, str]
        if isinstance(self.first_connected_at, datetime.datetime):
            first_connected_at = self.first_connected_at.isoformat()
        else:
            first_connected_at = self.first_connected_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        active_internal_squads = []
        for active_internal_squads_item_data in self.active_internal_squads:
            active_internal_squads_item = active_internal_squads_item_data.to_dict()
            active_internal_squads.append(active_internal_squads_item)

        subscription_url = self.subscription_url

        last_connected_node: Union[None, dict[str, Any]]
        if isinstance(self.last_connected_node, ResetUserTrafficResponseDtoResponseLastConnectedNodeType0):
            last_connected_node = self.last_connected_node.to_dict()
        else:
            last_connected_node = self.last_connected_node

        happ = self.happ.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        traffic_limit_bytes = self.traffic_limit_bytes

        traffic_limit_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.traffic_limit_strategy, Unset):
            traffic_limit_strategy = self.traffic_limit_strategy.value

        last_triggered_threshold = self.last_triggered_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "shortUuid": short_uuid,
                "username": username,
                "usedTrafficBytes": used_traffic_bytes,
                "lifetimeUsedTrafficBytes": lifetime_used_traffic_bytes,
                "subLastUserAgent": sub_last_user_agent,
                "subLastOpenedAt": sub_last_opened_at,
                "expireAt": expire_at,
                "onlineAt": online_at,
                "subRevokedAt": sub_revoked_at,
                "lastTrafficResetAt": last_traffic_reset_at,
                "trojanPassword": trojan_password,
                "vlessUuid": vless_uuid,
                "ssPassword": ss_password,
                "description": description,
                "tag": tag,
                "telegramId": telegram_id,
                "email": email,
                "hwidDeviceLimit": hwid_device_limit,
                "firstConnectedAt": first_connected_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "activeInternalSquads": active_internal_squads,
                "subscriptionUrl": subscription_url,
                "lastConnectedNode": last_connected_node,
                "happ": happ,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if traffic_limit_bytes is not UNSET:
            field_dict["trafficLimitBytes"] = traffic_limit_bytes
        if traffic_limit_strategy is not UNSET:
            field_dict["trafficLimitStrategy"] = traffic_limit_strategy
        if last_triggered_threshold is not UNSET:
            field_dict["lastTriggeredThreshold"] = last_triggered_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reset_user_traffic_response_dto_response_active_internal_squads_item import (
            ResetUserTrafficResponseDtoResponseActiveInternalSquadsItem,
        )
        from ..models.reset_user_traffic_response_dto_response_happ import ResetUserTrafficResponseDtoResponseHapp
        from ..models.reset_user_traffic_response_dto_response_last_connected_node_type_0 import (
            ResetUserTrafficResponseDtoResponseLastConnectedNodeType0,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        short_uuid = d.pop("shortUuid")

        username = d.pop("username")

        used_traffic_bytes = d.pop("usedTrafficBytes")

        lifetime_used_traffic_bytes = d.pop("lifetimeUsedTrafficBytes")

        def _parse_sub_last_user_agent(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sub_last_user_agent = _parse_sub_last_user_agent(d.pop("subLastUserAgent"))

        def _parse_sub_last_opened_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_last_opened_at_type_0 = isoparse(data)

                return sub_last_opened_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        sub_last_opened_at = _parse_sub_last_opened_at(d.pop("subLastOpenedAt"))

        expire_at = isoparse(d.pop("expireAt"))

        def _parse_online_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                online_at_type_0 = isoparse(data)

                return online_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        online_at = _parse_online_at(d.pop("onlineAt"))

        def _parse_sub_revoked_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_revoked_at_type_0 = isoparse(data)

                return sub_revoked_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        sub_revoked_at = _parse_sub_revoked_at(d.pop("subRevokedAt"))

        def _parse_last_traffic_reset_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_traffic_reset_at_type_0 = isoparse(data)

                return last_traffic_reset_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_traffic_reset_at = _parse_last_traffic_reset_at(d.pop("lastTrafficResetAt"))

        trojan_password = d.pop("trojanPassword")

        vless_uuid = UUID(d.pop("vlessUuid"))

        ss_password = d.pop("ssPassword")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        def _parse_tag(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tag = _parse_tag(d.pop("tag"))

        def _parse_telegram_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        telegram_id = _parse_telegram_id(d.pop("telegramId"))

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        def _parse_hwid_device_limit(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        hwid_device_limit = _parse_hwid_device_limit(d.pop("hwidDeviceLimit"))

        def _parse_first_connected_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_connected_at_type_0 = isoparse(data)

                return first_connected_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        first_connected_at = _parse_first_connected_at(d.pop("firstConnectedAt"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        active_internal_squads = []
        _active_internal_squads = d.pop("activeInternalSquads")
        for active_internal_squads_item_data in _active_internal_squads:
            active_internal_squads_item = ResetUserTrafficResponseDtoResponseActiveInternalSquadsItem.from_dict(
                active_internal_squads_item_data
            )

            active_internal_squads.append(active_internal_squads_item)

        subscription_url = d.pop("subscriptionUrl")

        def _parse_last_connected_node(
            data: object,
        ) -> Union["ResetUserTrafficResponseDtoResponseLastConnectedNodeType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_connected_node_type_0 = ResetUserTrafficResponseDtoResponseLastConnectedNodeType0.from_dict(data)

                return last_connected_node_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ResetUserTrafficResponseDtoResponseLastConnectedNodeType0", None], data)

        last_connected_node = _parse_last_connected_node(d.pop("lastConnectedNode"))

        happ = ResetUserTrafficResponseDtoResponseHapp.from_dict(d.pop("happ"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ResetUserTrafficResponseDtoResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ResetUserTrafficResponseDtoResponseStatus(_status)

        traffic_limit_bytes = d.pop("trafficLimitBytes", UNSET)

        _traffic_limit_strategy = d.pop("trafficLimitStrategy", UNSET)
        traffic_limit_strategy: Union[Unset, ResetUserTrafficResponseDtoResponseTrafficLimitStrategy]
        if isinstance(_traffic_limit_strategy, Unset):
            traffic_limit_strategy = UNSET
        else:
            traffic_limit_strategy = ResetUserTrafficResponseDtoResponseTrafficLimitStrategy(_traffic_limit_strategy)

        last_triggered_threshold = d.pop("lastTriggeredThreshold", UNSET)

        reset_user_traffic_response_dto_response = cls(
            uuid=uuid,
            short_uuid=short_uuid,
            username=username,
            used_traffic_bytes=used_traffic_bytes,
            lifetime_used_traffic_bytes=lifetime_used_traffic_bytes,
            sub_last_user_agent=sub_last_user_agent,
            sub_last_opened_at=sub_last_opened_at,
            expire_at=expire_at,
            online_at=online_at,
            sub_revoked_at=sub_revoked_at,
            last_traffic_reset_at=last_traffic_reset_at,
            trojan_password=trojan_password,
            vless_uuid=vless_uuid,
            ss_password=ss_password,
            description=description,
            tag=tag,
            telegram_id=telegram_id,
            email=email,
            hwid_device_limit=hwid_device_limit,
            first_connected_at=first_connected_at,
            created_at=created_at,
            updated_at=updated_at,
            active_internal_squads=active_internal_squads,
            subscription_url=subscription_url,
            last_connected_node=last_connected_node,
            happ=happ,
            status=status,
            traffic_limit_bytes=traffic_limit_bytes,
            traffic_limit_strategy=traffic_limit_strategy,
            last_triggered_threshold=last_triggered_threshold,
        )

        reset_user_traffic_response_dto_response.additional_properties = d
        return reset_user_traffic_response_dto_response

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
