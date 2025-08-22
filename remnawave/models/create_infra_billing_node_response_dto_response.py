from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_infra_billing_node_response_dto_response_available_billing_nodes_item import (
        CreateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem,
    )
    from ..models.create_infra_billing_node_response_dto_response_billing_nodes_item import (
        CreateInfraBillingNodeResponseDtoResponseBillingNodesItem,
    )
    from ..models.create_infra_billing_node_response_dto_response_stats import (
        CreateInfraBillingNodeResponseDtoResponseStats,
    )


T = TypeVar("T", bound="CreateInfraBillingNodeResponseDtoResponse")


@_attrs_define
class CreateInfraBillingNodeResponseDtoResponse:
    """
    Attributes:
        total_billing_nodes (float):
        billing_nodes (list['CreateInfraBillingNodeResponseDtoResponseBillingNodesItem']):
        available_billing_nodes (list['CreateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem']):
        total_available_billing_nodes (float):
        stats (CreateInfraBillingNodeResponseDtoResponseStats):
    """

    total_billing_nodes: float
    billing_nodes: list["CreateInfraBillingNodeResponseDtoResponseBillingNodesItem"]
    available_billing_nodes: list["CreateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem"]
    total_available_billing_nodes: float
    stats: "CreateInfraBillingNodeResponseDtoResponseStats"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_billing_nodes = self.total_billing_nodes

        billing_nodes = []
        for billing_nodes_item_data in self.billing_nodes:
            billing_nodes_item = billing_nodes_item_data.to_dict()
            billing_nodes.append(billing_nodes_item)

        available_billing_nodes = []
        for available_billing_nodes_item_data in self.available_billing_nodes:
            available_billing_nodes_item = available_billing_nodes_item_data.to_dict()
            available_billing_nodes.append(available_billing_nodes_item)

        total_available_billing_nodes = self.total_available_billing_nodes

        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalBillingNodes": total_billing_nodes,
                "billingNodes": billing_nodes,
                "availableBillingNodes": available_billing_nodes,
                "totalAvailableBillingNodes": total_available_billing_nodes,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_infra_billing_node_response_dto_response_available_billing_nodes_item import (
            CreateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem,
        )
        from ..models.create_infra_billing_node_response_dto_response_billing_nodes_item import (
            CreateInfraBillingNodeResponseDtoResponseBillingNodesItem,
        )
        from ..models.create_infra_billing_node_response_dto_response_stats import (
            CreateInfraBillingNodeResponseDtoResponseStats,
        )

        d = dict(src_dict)
        total_billing_nodes = d.pop("totalBillingNodes")

        billing_nodes = []
        _billing_nodes = d.pop("billingNodes")
        for billing_nodes_item_data in _billing_nodes:
            billing_nodes_item = CreateInfraBillingNodeResponseDtoResponseBillingNodesItem.from_dict(
                billing_nodes_item_data
            )

            billing_nodes.append(billing_nodes_item)

        available_billing_nodes = []
        _available_billing_nodes = d.pop("availableBillingNodes")
        for available_billing_nodes_item_data in _available_billing_nodes:
            available_billing_nodes_item = CreateInfraBillingNodeResponseDtoResponseAvailableBillingNodesItem.from_dict(
                available_billing_nodes_item_data
            )

            available_billing_nodes.append(available_billing_nodes_item)

        total_available_billing_nodes = d.pop("totalAvailableBillingNodes")

        stats = CreateInfraBillingNodeResponseDtoResponseStats.from_dict(d.pop("stats"))

        create_infra_billing_node_response_dto_response = cls(
            total_billing_nodes=total_billing_nodes,
            billing_nodes=billing_nodes,
            available_billing_nodes=available_billing_nodes,
            total_available_billing_nodes=total_available_billing_nodes,
            stats=stats,
        )

        create_infra_billing_node_response_dto_response.additional_properties = d
        return create_infra_billing_node_response_dto_response

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
