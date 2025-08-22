import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_config_profiles_response_dto_response_config_profiles_item_inbounds_item import (
        GetConfigProfilesResponseDtoResponseConfigProfilesItemInboundsItem,
    )
    from ..models.get_config_profiles_response_dto_response_config_profiles_item_nodes_item import (
        GetConfigProfilesResponseDtoResponseConfigProfilesItemNodesItem,
    )


T = TypeVar("T", bound="GetConfigProfilesResponseDtoResponseConfigProfilesItem")


@_attrs_define
class GetConfigProfilesResponseDtoResponseConfigProfilesItem:
    """
    Attributes:
        uuid (UUID):
        name (str):
        config (Any):
        inbounds (list['GetConfigProfilesResponseDtoResponseConfigProfilesItemInboundsItem']):
        nodes (list['GetConfigProfilesResponseDtoResponseConfigProfilesItemNodesItem']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    name: str
    config: Any
    inbounds: list["GetConfigProfilesResponseDtoResponseConfigProfilesItemInboundsItem"]
    nodes: list["GetConfigProfilesResponseDtoResponseConfigProfilesItemNodesItem"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        config = self.config

        inbounds = []
        for inbounds_item_data in self.inbounds:
            inbounds_item = inbounds_item_data.to_dict()
            inbounds.append(inbounds_item)

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "config": config,
                "inbounds": inbounds,
                "nodes": nodes,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_config_profiles_response_dto_response_config_profiles_item_inbounds_item import (
            GetConfigProfilesResponseDtoResponseConfigProfilesItemInboundsItem,
        )
        from ..models.get_config_profiles_response_dto_response_config_profiles_item_nodes_item import (
            GetConfigProfilesResponseDtoResponseConfigProfilesItemNodesItem,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        config = d.pop("config")

        inbounds = []
        _inbounds = d.pop("inbounds")
        for inbounds_item_data in _inbounds:
            inbounds_item = GetConfigProfilesResponseDtoResponseConfigProfilesItemInboundsItem.from_dict(
                inbounds_item_data
            )

            inbounds.append(inbounds_item)

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = GetConfigProfilesResponseDtoResponseConfigProfilesItemNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        get_config_profiles_response_dto_response_config_profiles_item = cls(
            uuid=uuid,
            name=name,
            config=config,
            inbounds=inbounds,
            nodes=nodes,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_config_profiles_response_dto_response_config_profiles_item.additional_properties = d
        return get_config_profiles_response_dto_response_config_profiles_item

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
