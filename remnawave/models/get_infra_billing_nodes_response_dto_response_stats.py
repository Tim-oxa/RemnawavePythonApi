from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInfraBillingNodesResponseDtoResponseStats")


@_attrs_define
class GetInfraBillingNodesResponseDtoResponseStats:
    """
    Attributes:
        upcoming_nodes_count (float):
        current_month_payments (float):
        total_spent (float):
    """

    upcoming_nodes_count: float
    current_month_payments: float
    total_spent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upcoming_nodes_count = self.upcoming_nodes_count

        current_month_payments = self.current_month_payments

        total_spent = self.total_spent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upcomingNodesCount": upcoming_nodes_count,
                "currentMonthPayments": current_month_payments,
                "totalSpent": total_spent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upcoming_nodes_count = d.pop("upcomingNodesCount")

        current_month_payments = d.pop("currentMonthPayments")

        total_spent = d.pop("totalSpent")

        get_infra_billing_nodes_response_dto_response_stats = cls(
            upcoming_nodes_count=upcoming_nodes_count,
            current_month_payments=current_month_payments,
            total_spent=total_spent,
        )

        get_infra_billing_nodes_response_dto_response_stats.additional_properties = d
        return get_infra_billing_nodes_response_dto_response_stats

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
