import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.reorder_node_response_dto_response_item_config_profile import (
        ReorderNodeResponseDtoResponseItemConfigProfile,
    )
    from ..models.reorder_node_response_dto_response_item_provider_type_0 import (
        ReorderNodeResponseDtoResponseItemProviderType0,
    )


T = TypeVar("T", bound="ReorderNodeResponseDtoResponseItem")


@_attrs_define
class ReorderNodeResponseDtoResponseItem:
    """
    Attributes:
        uuid (UUID):
        name (str):
        address (str):
        port (Union[None, int]):
        is_connected (bool):
        is_disabled (bool):
        is_connecting (bool):
        is_node_online (bool):
        is_xray_running (bool):
        last_status_change (Union[None, datetime.datetime]):
        last_status_message (Union[None, str]):
        xray_version (Union[None, str]):
        node_version (Union[None, str]):
        xray_uptime (str):
        is_traffic_tracking_active (bool):
        traffic_reset_day (Union[None, int]):
        traffic_limit_bytes (Union[None, float]):
        traffic_used_bytes (Union[None, float]):
        notify_percent (Union[None, int]):
        users_online (Union[None, int]):
        view_position (int):
        country_code (str):
        consumption_multiplier (float):
        cpu_count (Union[None, int]):
        cpu_model (Union[None, str]):
        total_ram (Union[None, str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        config_profile (ReorderNodeResponseDtoResponseItemConfigProfile):
        provider_uuid (Union[None, UUID]):
        provider (Union['ReorderNodeResponseDtoResponseItemProviderType0', None]):
    """

    uuid: UUID
    name: str
    address: str
    port: Union[None, int]
    is_connected: bool
    is_disabled: bool
    is_connecting: bool
    is_node_online: bool
    is_xray_running: bool
    last_status_change: Union[None, datetime.datetime]
    last_status_message: Union[None, str]
    xray_version: Union[None, str]
    node_version: Union[None, str]
    xray_uptime: str
    is_traffic_tracking_active: bool
    traffic_reset_day: Union[None, int]
    traffic_limit_bytes: Union[None, float]
    traffic_used_bytes: Union[None, float]
    notify_percent: Union[None, int]
    users_online: Union[None, int]
    view_position: int
    country_code: str
    consumption_multiplier: float
    cpu_count: Union[None, int]
    cpu_model: Union[None, str]
    total_ram: Union[None, str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    config_profile: "ReorderNodeResponseDtoResponseItemConfigProfile"
    provider_uuid: Union[None, UUID]
    provider: Union["ReorderNodeResponseDtoResponseItemProviderType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reorder_node_response_dto_response_item_provider_type_0 import (
            ReorderNodeResponseDtoResponseItemProviderType0,
        )

        uuid = str(self.uuid)

        name = self.name

        address = self.address

        port: Union[None, int]
        port = self.port

        is_connected = self.is_connected

        is_disabled = self.is_disabled

        is_connecting = self.is_connecting

        is_node_online = self.is_node_online

        is_xray_running = self.is_xray_running

        last_status_change: Union[None, str]
        if isinstance(self.last_status_change, datetime.datetime):
            last_status_change = self.last_status_change.isoformat()
        else:
            last_status_change = self.last_status_change

        last_status_message: Union[None, str]
        last_status_message = self.last_status_message

        xray_version: Union[None, str]
        xray_version = self.xray_version

        node_version: Union[None, str]
        node_version = self.node_version

        xray_uptime = self.xray_uptime

        is_traffic_tracking_active = self.is_traffic_tracking_active

        traffic_reset_day: Union[None, int]
        traffic_reset_day = self.traffic_reset_day

        traffic_limit_bytes: Union[None, float]
        traffic_limit_bytes = self.traffic_limit_bytes

        traffic_used_bytes: Union[None, float]
        traffic_used_bytes = self.traffic_used_bytes

        notify_percent: Union[None, int]
        notify_percent = self.notify_percent

        users_online: Union[None, int]
        users_online = self.users_online

        view_position = self.view_position

        country_code = self.country_code

        consumption_multiplier = self.consumption_multiplier

        cpu_count: Union[None, int]
        cpu_count = self.cpu_count

        cpu_model: Union[None, str]
        cpu_model = self.cpu_model

        total_ram: Union[None, str]
        total_ram = self.total_ram

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        config_profile = self.config_profile.to_dict()

        provider_uuid: Union[None, str]
        if isinstance(self.provider_uuid, UUID):
            provider_uuid = str(self.provider_uuid)
        else:
            provider_uuid = self.provider_uuid

        provider: Union[None, dict[str, Any]]
        if isinstance(self.provider, ReorderNodeResponseDtoResponseItemProviderType0):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "address": address,
                "port": port,
                "isConnected": is_connected,
                "isDisabled": is_disabled,
                "isConnecting": is_connecting,
                "isNodeOnline": is_node_online,
                "isXrayRunning": is_xray_running,
                "lastStatusChange": last_status_change,
                "lastStatusMessage": last_status_message,
                "xrayVersion": xray_version,
                "nodeVersion": node_version,
                "xrayUptime": xray_uptime,
                "isTrafficTrackingActive": is_traffic_tracking_active,
                "trafficResetDay": traffic_reset_day,
                "trafficLimitBytes": traffic_limit_bytes,
                "trafficUsedBytes": traffic_used_bytes,
                "notifyPercent": notify_percent,
                "usersOnline": users_online,
                "viewPosition": view_position,
                "countryCode": country_code,
                "consumptionMultiplier": consumption_multiplier,
                "cpuCount": cpu_count,
                "cpuModel": cpu_model,
                "totalRam": total_ram,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "configProfile": config_profile,
                "providerUuid": provider_uuid,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_node_response_dto_response_item_config_profile import (
            ReorderNodeResponseDtoResponseItemConfigProfile,
        )
        from ..models.reorder_node_response_dto_response_item_provider_type_0 import (
            ReorderNodeResponseDtoResponseItemProviderType0,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        address = d.pop("address")

        def _parse_port(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        port = _parse_port(d.pop("port"))

        is_connected = d.pop("isConnected")

        is_disabled = d.pop("isDisabled")

        is_connecting = d.pop("isConnecting")

        is_node_online = d.pop("isNodeOnline")

        is_xray_running = d.pop("isXrayRunning")

        def _parse_last_status_change(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_status_change_type_0 = isoparse(data)

                return last_status_change_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_status_change = _parse_last_status_change(d.pop("lastStatusChange"))

        def _parse_last_status_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_status_message = _parse_last_status_message(d.pop("lastStatusMessage"))

        def _parse_xray_version(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        xray_version = _parse_xray_version(d.pop("xrayVersion"))

        def _parse_node_version(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        node_version = _parse_node_version(d.pop("nodeVersion"))

        xray_uptime = d.pop("xrayUptime")

        is_traffic_tracking_active = d.pop("isTrafficTrackingActive")

        def _parse_traffic_reset_day(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        traffic_reset_day = _parse_traffic_reset_day(d.pop("trafficResetDay"))

        def _parse_traffic_limit_bytes(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        traffic_limit_bytes = _parse_traffic_limit_bytes(d.pop("trafficLimitBytes"))

        def _parse_traffic_used_bytes(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        traffic_used_bytes = _parse_traffic_used_bytes(d.pop("trafficUsedBytes"))

        def _parse_notify_percent(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        notify_percent = _parse_notify_percent(d.pop("notifyPercent"))

        def _parse_users_online(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        users_online = _parse_users_online(d.pop("usersOnline"))

        view_position = d.pop("viewPosition")

        country_code = d.pop("countryCode")

        consumption_multiplier = d.pop("consumptionMultiplier")

        def _parse_cpu_count(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        cpu_count = _parse_cpu_count(d.pop("cpuCount"))

        def _parse_cpu_model(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        cpu_model = _parse_cpu_model(d.pop("cpuModel"))

        def _parse_total_ram(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        total_ram = _parse_total_ram(d.pop("totalRam"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        config_profile = ReorderNodeResponseDtoResponseItemConfigProfile.from_dict(d.pop("configProfile"))

        def _parse_provider_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_uuid_type_0 = UUID(data)

                return provider_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        provider_uuid = _parse_provider_uuid(d.pop("providerUuid"))

        def _parse_provider(data: object) -> Union["ReorderNodeResponseDtoResponseItemProviderType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_0 = ReorderNodeResponseDtoResponseItemProviderType0.from_dict(data)

                return provider_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReorderNodeResponseDtoResponseItemProviderType0", None], data)

        provider = _parse_provider(d.pop("provider"))

        reorder_node_response_dto_response_item = cls(
            uuid=uuid,
            name=name,
            address=address,
            port=port,
            is_connected=is_connected,
            is_disabled=is_disabled,
            is_connecting=is_connecting,
            is_node_online=is_node_online,
            is_xray_running=is_xray_running,
            last_status_change=last_status_change,
            last_status_message=last_status_message,
            xray_version=xray_version,
            node_version=node_version,
            xray_uptime=xray_uptime,
            is_traffic_tracking_active=is_traffic_tracking_active,
            traffic_reset_day=traffic_reset_day,
            traffic_limit_bytes=traffic_limit_bytes,
            traffic_used_bytes=traffic_used_bytes,
            notify_percent=notify_percent,
            users_online=users_online,
            view_position=view_position,
            country_code=country_code,
            consumption_multiplier=consumption_multiplier,
            cpu_count=cpu_count,
            cpu_model=cpu_model,
            total_ram=total_ram,
            created_at=created_at,
            updated_at=updated_at,
            config_profile=config_profile,
            provider_uuid=provider_uuid,
            provider=provider,
        )

        reorder_node_response_dto_response_item.additional_properties = d
        return reorder_node_response_dto_response_item

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
