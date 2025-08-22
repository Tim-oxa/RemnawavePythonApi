from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetInfraProviderByUuidResponseDtoResponseBillingHistory")


@_attrs_define
class GetInfraProviderByUuidResponseDtoResponseBillingHistory:
    """
    Attributes:
        total_amount (float):
        total_bills (float):
    """

    total_amount: float
    total_bills: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_amount = self.total_amount

        total_bills = self.total_bills

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalAmount": total_amount,
                "totalBills": total_bills,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_amount = d.pop("totalAmount")

        total_bills = d.pop("totalBills")

        get_infra_provider_by_uuid_response_dto_response_billing_history = cls(
            total_amount=total_amount,
            total_bills=total_bills,
        )

        get_infra_provider_by_uuid_response_dto_response_billing_history.additional_properties = d
        return get_infra_provider_by_uuid_response_dto_response_billing_history

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
