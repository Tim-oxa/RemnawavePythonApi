from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem")


@_attrs_define
class GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem:
    """
    Attributes:
        uuid (UUID):
        node_name (str):
        country_code (str):
        config_profile_uuid (UUID):
        config_profile_name (str):
        active_inbounds (list[str]):
    """

    uuid: UUID
    node_name: str
    country_code: str
    config_profile_uuid: UUID
    config_profile_name: str
    active_inbounds: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        node_name = self.node_name

        country_code = self.country_code

        config_profile_uuid = str(self.config_profile_uuid)

        config_profile_name = self.config_profile_name

        active_inbounds = self.active_inbounds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "nodeName": node_name,
                "countryCode": country_code,
                "configProfileUuid": config_profile_uuid,
                "configProfileName": config_profile_name,
                "activeInbounds": active_inbounds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        node_name = d.pop("nodeName")

        country_code = d.pop("countryCode")

        config_profile_uuid = UUID(d.pop("configProfileUuid"))

        config_profile_name = d.pop("configProfileName")

        active_inbounds = cast(list[str], d.pop("activeInbounds"))

        get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_item = cls(
            uuid=uuid,
            node_name=node_name,
            country_code=country_code,
            config_profile_uuid=config_profile_uuid,
            config_profile_name=config_profile_name,
            active_inbounds=active_inbounds,
        )

        get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_item.additional_properties = d
        return get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_item

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
