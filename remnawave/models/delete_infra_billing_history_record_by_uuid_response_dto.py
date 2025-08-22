from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delete_infra_billing_history_record_by_uuid_response_dto_response import (
        DeleteInfraBillingHistoryRecordByUuidResponseDtoResponse,
    )


T = TypeVar("T", bound="DeleteInfraBillingHistoryRecordByUuidResponseDto")


@_attrs_define
class DeleteInfraBillingHistoryRecordByUuidResponseDto:
    """
    Attributes:
        response (DeleteInfraBillingHistoryRecordByUuidResponseDtoResponse):
    """

    response: "DeleteInfraBillingHistoryRecordByUuidResponseDtoResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response.to_dict()

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
        from ..models.delete_infra_billing_history_record_by_uuid_response_dto_response import (
            DeleteInfraBillingHistoryRecordByUuidResponseDtoResponse,
        )

        d = dict(src_dict)
        response = DeleteInfraBillingHistoryRecordByUuidResponseDtoResponse.from_dict(d.pop("response"))

        delete_infra_billing_history_record_by_uuid_response_dto = cls(
            response=response,
        )

        delete_infra_billing_history_record_by_uuid_response_dto.additional_properties = d
        return delete_infra_billing_history_record_by_uuid_response_dto

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
