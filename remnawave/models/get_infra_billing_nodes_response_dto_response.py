from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_infra_billing_nodes_response_dto_response_available_billing_nodes_item import (
        GetInfraBillingNodesResponseDtoResponseAvailableBillingNodesItem,
    )
    from ..models.get_infra_billing_nodes_response_dto_response_billing_nodes_item import (
        GetInfraBillingNodesResponseDtoResponseBillingNodesItem,
    )
    from ..models.get_infra_billing_nodes_response_dto_response_stats import (
        GetInfraBillingNodesResponseDtoResponseStats,
    )


T = TypeVar("T", bound="GetInfraBillingNodesResponseDtoResponse")


@_attrs_define
class GetInfraBillingNodesResponseDtoResponse:
    """
    Attributes:
        total_billing_nodes (float):
        billing_nodes (list['GetInfraBillingNodesResponseDtoResponseBillingNodesItem']):
        available_billing_nodes (list['GetInfraBillingNodesResponseDtoResponseAvailableBillingNodesItem']):
        total_available_billing_nodes (float):
        stats (GetInfraBillingNodesResponseDtoResponseStats):
    """

    total_billing_nodes: float
    billing_nodes: list["GetInfraBillingNodesResponseDtoResponseBillingNodesItem"]
    available_billing_nodes: list["GetInfraBillingNodesResponseDtoResponseAvailableBillingNodesItem"]
    total_available_billing_nodes: float
    stats: "GetInfraBillingNodesResponseDtoResponseStats"
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
        from ..models.get_infra_billing_nodes_response_dto_response_available_billing_nodes_item import (
            GetInfraBillingNodesResponseDtoResponseAvailableBillingNodesItem,
        )
        from ..models.get_infra_billing_nodes_response_dto_response_billing_nodes_item import (
            GetInfraBillingNodesResponseDtoResponseBillingNodesItem,
        )
        from ..models.get_infra_billing_nodes_response_dto_response_stats import (
            GetInfraBillingNodesResponseDtoResponseStats,
        )

        d = dict(src_dict)
        total_billing_nodes = d.pop("totalBillingNodes")

        billing_nodes = []
        _billing_nodes = d.pop("billingNodes")
        for billing_nodes_item_data in _billing_nodes:
            billing_nodes_item = GetInfraBillingNodesResponseDtoResponseBillingNodesItem.from_dict(
                billing_nodes_item_data
            )

            billing_nodes.append(billing_nodes_item)

        available_billing_nodes = []
        _available_billing_nodes = d.pop("availableBillingNodes")
        for available_billing_nodes_item_data in _available_billing_nodes:
            available_billing_nodes_item = GetInfraBillingNodesResponseDtoResponseAvailableBillingNodesItem.from_dict(
                available_billing_nodes_item_data
            )

            available_billing_nodes.append(available_billing_nodes_item)

        total_available_billing_nodes = d.pop("totalAvailableBillingNodes")

        stats = GetInfraBillingNodesResponseDtoResponseStats.from_dict(d.pop("stats"))

        get_infra_billing_nodes_response_dto_response = cls(
            total_billing_nodes=total_billing_nodes,
            billing_nodes=billing_nodes,
            available_billing_nodes=available_billing_nodes,
            total_available_billing_nodes=total_available_billing_nodes,
            stats=stats,
        )

        get_infra_billing_nodes_response_dto_response.additional_properties = d
        return get_infra_billing_nodes_response_dto_response

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
