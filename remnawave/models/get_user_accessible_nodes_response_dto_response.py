from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_user_accessible_nodes_response_dto_response_active_nodes_item import (
        GetUserAccessibleNodesResponseDtoResponseActiveNodesItem,
    )


T = TypeVar("T", bound="GetUserAccessibleNodesResponseDtoResponse")


@_attrs_define
class GetUserAccessibleNodesResponseDtoResponse:
    """
    Attributes:
        user_uuid (UUID):
        active_nodes (list['GetUserAccessibleNodesResponseDtoResponseActiveNodesItem']):
    """

    user_uuid: UUID
    active_nodes: list["GetUserAccessibleNodesResponseDtoResponseActiveNodesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_uuid = str(self.user_uuid)

        active_nodes = []
        for active_nodes_item_data in self.active_nodes:
            active_nodes_item = active_nodes_item_data.to_dict()
            active_nodes.append(active_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "activeNodes": active_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_user_accessible_nodes_response_dto_response_active_nodes_item import (
            GetUserAccessibleNodesResponseDtoResponseActiveNodesItem,
        )

        d = dict(src_dict)
        user_uuid = UUID(d.pop("userUuid"))

        active_nodes = []
        _active_nodes = d.pop("activeNodes")
        for active_nodes_item_data in _active_nodes:
            active_nodes_item = GetUserAccessibleNodesResponseDtoResponseActiveNodesItem.from_dict(
                active_nodes_item_data
            )

            active_nodes.append(active_nodes_item)

        get_user_accessible_nodes_response_dto_response = cls(
            user_uuid=user_uuid,
            active_nodes=active_nodes,
        )

        get_user_accessible_nodes_response_dto_response.additional_properties = d
        return get_user_accessible_nodes_response_dto_response

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
