import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.update_config_profile_response_dto_response_inbounds_item import (
        UpdateConfigProfileResponseDtoResponseInboundsItem,
    )
    from ..models.update_config_profile_response_dto_response_nodes_item import (
        UpdateConfigProfileResponseDtoResponseNodesItem,
    )


T = TypeVar("T", bound="UpdateConfigProfileResponseDtoResponse")


@_attrs_define
class UpdateConfigProfileResponseDtoResponse:
    """
    Attributes:
        uuid (UUID):
        name (str):
        config (Any):
        inbounds (list['UpdateConfigProfileResponseDtoResponseInboundsItem']):
        nodes (list['UpdateConfigProfileResponseDtoResponseNodesItem']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    name: str
    config: Any
    inbounds: list["UpdateConfigProfileResponseDtoResponseInboundsItem"]
    nodes: list["UpdateConfigProfileResponseDtoResponseNodesItem"]
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
        from ..models.update_config_profile_response_dto_response_inbounds_item import (
            UpdateConfigProfileResponseDtoResponseInboundsItem,
        )
        from ..models.update_config_profile_response_dto_response_nodes_item import (
            UpdateConfigProfileResponseDtoResponseNodesItem,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        config = d.pop("config")

        inbounds = []
        _inbounds = d.pop("inbounds")
        for inbounds_item_data in _inbounds:
            inbounds_item = UpdateConfigProfileResponseDtoResponseInboundsItem.from_dict(inbounds_item_data)

            inbounds.append(inbounds_item)

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = UpdateConfigProfileResponseDtoResponseNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        update_config_profile_response_dto_response = cls(
            uuid=uuid,
            name=name,
            config=config,
            inbounds=inbounds,
            nodes=nodes,
            created_at=created_at,
            updated_at=updated_at,
        )

        update_config_profile_response_dto_response.additional_properties = d
        return update_config_profile_response_dto_response

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
