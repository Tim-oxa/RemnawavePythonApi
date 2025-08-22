from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReorderNodeRequestDtoNodesItem")


@_attrs_define
class ReorderNodeRequestDtoNodesItem:
    """
    Attributes:
        view_position (int):
        uuid (UUID):
    """

    view_position: int
    uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view_position = self.view_position

        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "viewPosition": view_position,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        view_position = d.pop("viewPosition")

        uuid = UUID(d.pop("uuid"))

        reorder_node_request_dto_nodes_item = cls(
            view_position=view_position,
            uuid=uuid,
        )

        reorder_node_request_dto_nodes_item.additional_properties = d
        return reorder_node_request_dto_nodes_item

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
