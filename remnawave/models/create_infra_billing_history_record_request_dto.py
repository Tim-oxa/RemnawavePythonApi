import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CreateInfraBillingHistoryRecordRequestDto")


@_attrs_define
class CreateInfraBillingHistoryRecordRequestDto:
    """
    Attributes:
        provider_uuid (UUID):
        amount (float):
        billed_at (datetime.datetime): Billing date. Format: 2025-01-17T15:38:45.065Z
    """

    provider_uuid: UUID
    amount: float
    billed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_uuid = str(self.provider_uuid)

        amount = self.amount

        billed_at = self.billed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerUuid": provider_uuid,
                "amount": amount,
                "billedAt": billed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_uuid = UUID(d.pop("providerUuid"))

        amount = d.pop("amount")

        billed_at = isoparse(d.pop("billedAt"))

        create_infra_billing_history_record_request_dto = cls(
            provider_uuid=provider_uuid,
            amount=amount,
            billed_at=billed_at,
        )

        create_infra_billing_history_record_request_dto.additional_properties = d
        return create_infra_billing_history_record_request_dto

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
