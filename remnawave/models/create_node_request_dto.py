from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_node_request_dto_config_profile import CreateNodeRequestDtoConfigProfile


T = TypeVar("T", bound="CreateNodeRequestDto")


@_attrs_define
class CreateNodeRequestDto:
    """
    Attributes:
        name (str):
        address (str):
        config_profile (CreateNodeRequestDtoConfigProfile):
        port (Union[Unset, int]):
        is_traffic_tracking_active (Union[Unset, bool]):  Default: False.
        traffic_limit_bytes (Union[Unset, int]):
        notify_percent (Union[Unset, int]):
        traffic_reset_day (Union[Unset, int]):
        country_code (Union[Unset, str]):  Default: 'XX'.
        consumption_multiplier (Union[Unset, float]):
        provider_uuid (Union[None, UUID, Unset]):
    """

    name: str
    address: str
    config_profile: "CreateNodeRequestDtoConfigProfile"
    port: Union[Unset, int] = UNSET
    is_traffic_tracking_active: Union[Unset, bool] = False
    traffic_limit_bytes: Union[Unset, int] = UNSET
    notify_percent: Union[Unset, int] = UNSET
    traffic_reset_day: Union[Unset, int] = UNSET
    country_code: Union[Unset, str] = "XX"
    consumption_multiplier: Union[Unset, float] = UNSET
    provider_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        config_profile = self.config_profile.to_dict()

        port = self.port

        is_traffic_tracking_active = self.is_traffic_tracking_active

        traffic_limit_bytes = self.traffic_limit_bytes

        notify_percent = self.notify_percent

        traffic_reset_day = self.traffic_reset_day

        country_code = self.country_code

        consumption_multiplier = self.consumption_multiplier

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
                "name": name,
                "address": address,
                "configProfile": config_profile,
            }
        )
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
        if provider_uuid is not UNSET:
            field_dict["providerUuid"] = provider_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_node_request_dto_config_profile import CreateNodeRequestDtoConfigProfile

        d = dict(src_dict)
        name = d.pop("name")

        address = d.pop("address")

        config_profile = CreateNodeRequestDtoConfigProfile.from_dict(d.pop("configProfile"))

        port = d.pop("port", UNSET)

        is_traffic_tracking_active = d.pop("isTrafficTrackingActive", UNSET)

        traffic_limit_bytes = d.pop("trafficLimitBytes", UNSET)

        notify_percent = d.pop("notifyPercent", UNSET)

        traffic_reset_day = d.pop("trafficResetDay", UNSET)

        country_code = d.pop("countryCode", UNSET)

        consumption_multiplier = d.pop("consumptionMultiplier", UNSET)

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

        create_node_request_dto = cls(
            name=name,
            address=address,
            config_profile=config_profile,
            port=port,
            is_traffic_tracking_active=is_traffic_tracking_active,
            traffic_limit_bytes=traffic_limit_bytes,
            notify_percent=notify_percent,
            traffic_reset_day=traffic_reset_day,
            country_code=country_code,
            consumption_multiplier=consumption_multiplier,
            provider_uuid=provider_uuid,
        )

        create_node_request_dto.additional_properties = d
        return create_node_request_dto

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
