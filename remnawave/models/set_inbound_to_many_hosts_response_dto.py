from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_inbound_to_many_hosts_response_dto_response_item import (
        SetInboundToManyHostsResponseDtoResponseItem,
    )


T = TypeVar("T", bound="SetInboundToManyHostsResponseDto")


@_attrs_define
class SetInboundToManyHostsResponseDto:
    """
    Attributes:
        response (list['SetInboundToManyHostsResponseDtoResponseItem']):
    """

    response: list["SetInboundToManyHostsResponseDtoResponseItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = []
        for response_item_data in self.response:
            response_item = response_item_data.to_dict()
            response.append(response_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_inbound_to_many_hosts_response_dto_response_item import (
            SetInboundToManyHostsResponseDtoResponseItem,
        )

        d = dict(src_dict)
        response = []
        _response = d.pop("response")
        for response_item_data in _response:
            response_item = SetInboundToManyHostsResponseDtoResponseItem.from_dict(response_item_data)

            response.append(response_item)

        set_inbound_to_many_hosts_response_dto = cls(
            response=response,
        )

        set_inbound_to_many_hosts_response_dto.additional_properties = d
        return set_inbound_to_many_hosts_response_dto

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
