from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateInfraProviderResponseDtoResponseBillingNodesItem")


@_attrs_define
class CreateInfraProviderResponseDtoResponseBillingNodesItem:
    """
    Attributes:
        node_uuid (UUID):
        name (str):
        country_code (str):
    """

    node_uuid: UUID
    name: str
    country_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = str(self.node_uuid)

        name = self.name

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeUuid": node_uuid,
                "name": name,
                "countryCode": country_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_uuid = UUID(d.pop("nodeUuid"))

        name = d.pop("name")

        country_code = d.pop("countryCode")

        create_infra_provider_response_dto_response_billing_nodes_item = cls(
            node_uuid=node_uuid,
            name=name,
            country_code=country_code,
        )

        create_infra_provider_response_dto_response_billing_nodes_item.additional_properties = d
        return create_infra_provider_response_dto_response_billing_nodes_item

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
