from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_item import (
        GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem,
    )


T = TypeVar("T", bound="GetInternalSquadAccessibleNodesResponseDtoResponse")


@_attrs_define
class GetInternalSquadAccessibleNodesResponseDtoResponse:
    """
    Attributes:
        squad_uuid (UUID):
        accessible_nodes (list['GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem']):
    """

    squad_uuid: UUID
    accessible_nodes: list["GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        squad_uuid = str(self.squad_uuid)

        accessible_nodes = []
        for accessible_nodes_item_data in self.accessible_nodes:
            accessible_nodes_item = accessible_nodes_item_data.to_dict()
            accessible_nodes.append(accessible_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "squadUuid": squad_uuid,
                "accessibleNodes": accessible_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_item import (
            GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem,
        )

        d = dict(src_dict)
        squad_uuid = UUID(d.pop("squadUuid"))

        accessible_nodes = []
        _accessible_nodes = d.pop("accessibleNodes")
        for accessible_nodes_item_data in _accessible_nodes:
            accessible_nodes_item = GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesItem.from_dict(
                accessible_nodes_item_data
            )

            accessible_nodes.append(accessible_nodes_item)

        get_internal_squad_accessible_nodes_response_dto_response = cls(
            squad_uuid=squad_uuid,
            accessible_nodes=accessible_nodes,
        )

        get_internal_squad_accessible_nodes_response_dto_response.additional_properties = d
        return get_internal_squad_accessible_nodes_response_dto_response

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
