from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_user_accessible_nodes_response_dto_response_active_nodes_item_active_squads_item import (
        GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem,
    )


T = TypeVar("T", bound="GetUserAccessibleNodesResponseDtoResponseActiveNodesItem")


@_attrs_define
class GetUserAccessibleNodesResponseDtoResponseActiveNodesItem:
    """
    Attributes:
        uuid (UUID):
        node_name (str):
        country_code (str):
        config_profile_uuid (UUID):
        config_profile_name (str):
        active_squads (list['GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem']):
    """

    uuid: UUID
    node_name: str
    country_code: str
    config_profile_uuid: UUID
    config_profile_name: str
    active_squads: list["GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        node_name = self.node_name

        country_code = self.country_code

        config_profile_uuid = str(self.config_profile_uuid)

        config_profile_name = self.config_profile_name

        active_squads = []
        for active_squads_item_data in self.active_squads:
            active_squads_item = active_squads_item_data.to_dict()
            active_squads.append(active_squads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "nodeName": node_name,
                "countryCode": country_code,
                "configProfileUuid": config_profile_uuid,
                "configProfileName": config_profile_name,
                "activeSquads": active_squads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_user_accessible_nodes_response_dto_response_active_nodes_item_active_squads_item import (
            GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        node_name = d.pop("nodeName")

        country_code = d.pop("countryCode")

        config_profile_uuid = UUID(d.pop("configProfileUuid"))

        config_profile_name = d.pop("configProfileName")

        active_squads = []
        _active_squads = d.pop("activeSquads")
        for active_squads_item_data in _active_squads:
            active_squads_item = GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem.from_dict(
                active_squads_item_data
            )

            active_squads.append(active_squads_item)

        get_user_accessible_nodes_response_dto_response_active_nodes_item = cls(
            uuid=uuid,
            node_name=node_name,
            country_code=country_code,
            config_profile_uuid=config_profile_uuid,
            config_profile_name=config_profile_name,
            active_squads=active_squads,
        )

        get_user_accessible_nodes_response_dto_response_active_nodes_item.additional_properties = d
        return get_user_accessible_nodes_response_dto_response_active_nodes_item

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
