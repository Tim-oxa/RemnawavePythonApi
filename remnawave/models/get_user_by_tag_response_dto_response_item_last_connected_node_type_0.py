import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetUserByTagResponseDtoResponseItemLastConnectedNodeType0")


@_attrs_define
class GetUserByTagResponseDtoResponseItemLastConnectedNodeType0:
    """
    Attributes:
        connected_at (datetime.datetime):
        node_name (str):
        country_code (str):
    """

    connected_at: datetime.datetime
    node_name: str
    country_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_at = self.connected_at.isoformat()

        node_name = self.node_name

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectedAt": connected_at,
                "nodeName": node_name,
                "countryCode": country_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected_at = isoparse(d.pop("connectedAt"))

        node_name = d.pop("nodeName")

        country_code = d.pop("countryCode")

        get_user_by_tag_response_dto_response_item_last_connected_node_type_0 = cls(
            connected_at=connected_at,
            node_name=node_name,
            country_code=country_code,
        )

        get_user_by_tag_response_dto_response_item_last_connected_node_type_0.additional_properties = d
        return get_user_by_tag_response_dto_response_item_last_connected_node_type_0

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
