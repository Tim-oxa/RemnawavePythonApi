import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.create_infra_billing_history_record_response_dto_response_records_item_provider import (
        CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItemProvider,
    )


T = TypeVar("T", bound="CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItem")


@_attrs_define
class CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItem:
    """
    Attributes:
        uuid (UUID):
        provider_uuid (UUID):
        amount (float):
        billed_at (datetime.datetime):
        provider (CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItemProvider):
    """

    uuid: UUID
    provider_uuid: UUID
    amount: float
    billed_at: datetime.datetime
    provider: "CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItemProvider"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        provider_uuid = str(self.provider_uuid)

        amount = self.amount

        billed_at = self.billed_at.isoformat()

        provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "providerUuid": provider_uuid,
                "amount": amount,
                "billedAt": billed_at,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_infra_billing_history_record_response_dto_response_records_item_provider import (
            CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItemProvider,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        provider_uuid = UUID(d.pop("providerUuid"))

        amount = d.pop("amount")

        billed_at = isoparse(d.pop("billedAt"))

        provider = CreateInfraBillingHistoryRecordResponseDtoResponseRecordsItemProvider.from_dict(d.pop("provider"))

        create_infra_billing_history_record_response_dto_response_records_item = cls(
            uuid=uuid,
            provider_uuid=provider_uuid,
            amount=amount,
            billed_at=billed_at,
            provider=provider,
        )

        create_infra_billing_history_record_response_dto_response_records_item.additional_properties = d
        return create_infra_billing_history_record_response_dto_response_records_item

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
