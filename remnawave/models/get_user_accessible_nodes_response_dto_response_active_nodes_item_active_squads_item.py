from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem")


@_attrs_define
class GetUserAccessibleNodesResponseDtoResponseActiveNodesItemActiveSquadsItem:
    """
    Attributes:
        squad_name (str):
        active_inbounds (list[str]):
    """

    squad_name: str
    active_inbounds: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        squad_name = self.squad_name

        active_inbounds = self.active_inbounds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "squadName": squad_name,
                "activeInbounds": active_inbounds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        squad_name = d.pop("squadName")

        active_inbounds = cast(list[str], d.pop("activeInbounds"))

        get_user_accessible_nodes_response_dto_response_active_nodes_item_active_squads_item = cls(
            squad_name=squad_name,
            active_inbounds=active_inbounds,
        )

        get_user_accessible_nodes_response_dto_response_active_nodes_item_active_squads_item.additional_properties = d
        return get_user_accessible_nodes_response_dto_response_active_nodes_item_active_squads_item

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
