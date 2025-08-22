import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInfraBillingNodeRequestDto")


@_attrs_define
class CreateInfraBillingNodeRequestDto:
    """
    Attributes:
        provider_uuid (UUID):
        node_uuid (UUID):
        next_billing_at (Union[Unset, datetime.datetime]): Next billing date. Format: 2025-01-17T15:38:45.065Z
    """

    provider_uuid: UUID
    node_uuid: UUID
    next_billing_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_uuid = str(self.provider_uuid)

        node_uuid = str(self.node_uuid)

        next_billing_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_billing_at, Unset):
            next_billing_at = self.next_billing_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerUuid": provider_uuid,
                "nodeUuid": node_uuid,
            }
        )
        if next_billing_at is not UNSET:
            field_dict["nextBillingAt"] = next_billing_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_uuid = UUID(d.pop("providerUuid"))

        node_uuid = UUID(d.pop("nodeUuid"))

        _next_billing_at = d.pop("nextBillingAt", UNSET)
        next_billing_at: Union[Unset, datetime.datetime]
        if isinstance(_next_billing_at, Unset):
            next_billing_at = UNSET
        else:
            next_billing_at = isoparse(_next_billing_at)

        create_infra_billing_node_request_dto = cls(
            provider_uuid=provider_uuid,
            node_uuid=node_uuid,
            next_billing_at=next_billing_at,
        )

        create_infra_billing_node_request_dto.additional_properties = d
        return create_infra_billing_node_request_dto

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
