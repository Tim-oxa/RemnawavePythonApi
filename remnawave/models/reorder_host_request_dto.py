from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reorder_host_request_dto_hosts_item import ReorderHostRequestDtoHostsItem


T = TypeVar("T", bound="ReorderHostRequestDto")


@_attrs_define
class ReorderHostRequestDto:
    """
    Attributes:
        hosts (list['ReorderHostRequestDtoHostsItem']):
    """

    hosts: list["ReorderHostRequestDtoHostsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosts = []
        for hosts_item_data in self.hosts:
            hosts_item = hosts_item_data.to_dict()
            hosts.append(hosts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosts": hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_host_request_dto_hosts_item import ReorderHostRequestDtoHostsItem

        d = dict(src_dict)
        hosts = []
        _hosts = d.pop("hosts")
        for hosts_item_data in _hosts:
            hosts_item = ReorderHostRequestDtoHostsItem.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        reorder_host_request_dto = cls(
            hosts=hosts,
        )

        reorder_host_request_dto.additional_properties = d
        return reorder_host_request_dto

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
