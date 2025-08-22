import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UpdateInfraBillingNodeRequestDto")


@_attrs_define
class UpdateInfraBillingNodeRequestDto:
    """
    Attributes:
        uuid (UUID):
        next_billing_at (datetime.datetime):
    """

    uuid: UUID
    next_billing_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        next_billing_at = self.next_billing_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "nextBillingAt": next_billing_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        next_billing_at = isoparse(d.pop("nextBillingAt"))

        update_infra_billing_node_request_dto = cls(
            uuid=uuid,
            next_billing_at=next_billing_at,
        )

        update_infra_billing_node_request_dto.additional_properties = d
        return update_infra_billing_node_request_dto

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
