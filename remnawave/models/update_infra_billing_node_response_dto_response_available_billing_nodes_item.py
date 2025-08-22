from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem")


@_attrs_define
class UpdateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem:
    """
    Attributes:
        uuid (UUID):
        name (str):
        country_code (str):
    """

    uuid: UUID
    name: str
    country_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "countryCode": country_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        country_code = d.pop("countryCode")

        update_infra_billing_node_response_dto_response_available_billing_nodes_item = cls(
            uuid=uuid,
            name=name,
            country_code=country_code,
        )

        update_infra_billing_node_response_dto_response_available_billing_nodes_item.additional_properties = d
        return update_infra_billing_node_response_dto_response_available_billing_nodes_item

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
