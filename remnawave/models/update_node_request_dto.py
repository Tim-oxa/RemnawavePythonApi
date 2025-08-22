from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_node_request_dto_config_profile import UpdateNodeRequestDtoConfigProfile


T = TypeVar("T", bound="UpdateNodeRequestDto")


@_attrs_define
class UpdateNodeRequestDto:
    """
    Attributes:
        uuid (UUID):
        name (Union[Unset, str]):
        address (Union[Unset, str]):
        port (Union[Unset, float]):
        is_traffic_tracking_active (Union[Unset, bool]):
        traffic_limit_bytes (Union[Unset, float]):
        notify_percent (Union[Unset, float]):
        traffic_reset_day (Union[Unset, float]):
        country_code (Union[Unset, str]):
        consumption_multiplier (Union[Unset, float]):
        config_profile (Union[Unset, UpdateNodeRequestDtoConfigProfile]):
        provider_uuid (Union[None, UUID, Unset]):
    """

    uuid: UUID
    name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    port: Union[Unset, float] = UNSET
    is_traffic_tracking_active: Union[Unset, bool] = UNSET
    traffic_limit_bytes: Union[Unset, float] = UNSET
    notify_percent: Union[Unset, float] = UNSET
    traffic_reset_day: Union[Unset, float] = UNSET
    country_code: Union[Unset, str] = UNSET
    consumption_multiplier: Union[Unset, float] = UNSET
    config_profile: Union[Unset, "UpdateNodeRequestDtoConfigProfile"] = UNSET
    provider_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        address = self.address

        port = self.port

        is_traffic_tracking_active = self.is_traffic_tracking_active

        traffic_limit_bytes = self.traffic_limit_bytes

        notify_percent = self.notify_percent

        traffic_reset_day = self.traffic_reset_day

        country_code = self.country_code

        consumption_multiplier = self.consumption_multiplier

        config_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config_profile, Unset):
            config_profile = self.config_profile.to_dict()

        provider_uuid: Union[None, Unset, str]
        if isinstance(self.provider_uuid, Unset):
            provider_uuid = UNSET
        elif isinstance(self.provider_uuid, UUID):
            provider_uuid = str(self.provider_uuid)
        else:
            provider_uuid = self.provider_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if is_traffic_tracking_active is not UNSET:
            field_dict["isTrafficTrackingActive"] = is_traffic_tracking_active
        if traffic_limit_bytes is not UNSET:
            field_dict["trafficLimitBytes"] = traffic_limit_bytes
        if notify_percent is not UNSET:
            field_dict["notifyPercent"] = notify_percent
        if traffic_reset_day is not UNSET:
            field_dict["trafficResetDay"] = traffic_reset_day
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if consumption_multiplier is not UNSET:
            field_dict["consumptionMultiplier"] = consumption_multiplier
        if config_profile is not UNSET:
            field_dict["configProfile"] = config_profile
        if provider_uuid is not UNSET:
            field_dict["providerUuid"] = provider_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_node_request_dto_config_profile import UpdateNodeRequestDtoConfigProfile

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        is_traffic_tracking_active = d.pop("isTrafficTrackingActive", UNSET)

        traffic_limit_bytes = d.pop("trafficLimitBytes", UNSET)

        notify_percent = d.pop("notifyPercent", UNSET)

        traffic_reset_day = d.pop("trafficResetDay", UNSET)

        country_code = d.pop("countryCode", UNSET)

        consumption_multiplier = d.pop("consumptionMultiplier", UNSET)

        _config_profile = d.pop("configProfile", UNSET)
        config_profile: Union[Unset, UpdateNodeRequestDtoConfigProfile]
        if isinstance(_config_profile, Unset):
            config_profile = UNSET
        else:
            config_profile = UpdateNodeRequestDtoConfigProfile.from_dict(_config_profile)

        def _parse_provider_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_uuid_type_0 = UUID(data)

                return provider_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        provider_uuid = _parse_provider_uuid(d.pop("providerUuid", UNSET))

        update_node_request_dto = cls(
            uuid=uuid,
            name=name,
            address=address,
            port=port,
            is_traffic_tracking_active=is_traffic_tracking_active,
            traffic_limit_bytes=traffic_limit_bytes,
            notify_percent=notify_percent,
            traffic_reset_day=traffic_reset_day,
            country_code=country_code,
            consumption_multiplier=consumption_multiplier,
            config_profile=config_profile,
            provider_uuid=provider_uuid,
        )

        update_node_request_dto.additional_properties = d
        return update_node_request_dto

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
