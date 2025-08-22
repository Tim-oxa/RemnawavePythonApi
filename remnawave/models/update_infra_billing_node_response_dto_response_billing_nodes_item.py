import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.update_infra_billing_node_response_dto_response_billing_nodes_item_node import (
        UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemNode,
    )
    from ..models.update_infra_billing_node_response_dto_response_billing_nodes_item_provider import (
        UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider,
    )


T = TypeVar("T", bound="UpdateInfraBillingNodeResponseDtoResponseBillingNodesItem")


@_attrs_define
class UpdateInfraBillingNodeResponseDtoResponseBillingNodesItem:
    """
    Attributes:
        uuid (UUID):
        node_uuid (UUID):
        provider_uuid (UUID):
        provider (UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider):
        node (UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemNode):
        next_billing_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    node_uuid: UUID
    provider_uuid: UUID
    provider: "UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider"
    node: "UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemNode"
    next_billing_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        node_uuid = str(self.node_uuid)

        provider_uuid = str(self.provider_uuid)

        provider = self.provider.to_dict()

        node = self.node.to_dict()

        next_billing_at = self.next_billing_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "nodeUuid": node_uuid,
                "providerUuid": provider_uuid,
                "provider": provider,
                "node": node,
                "nextBillingAt": next_billing_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_infra_billing_node_response_dto_response_billing_nodes_item_node import (
            UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemNode,
        )
        from ..models.update_infra_billing_node_response_dto_response_billing_nodes_item_provider import (
            UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        node_uuid = UUID(d.pop("nodeUuid"))

        provider_uuid = UUID(d.pop("providerUuid"))

        provider = UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider.from_dict(d.pop("provider"))

        node = UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemNode.from_dict(d.pop("node"))

        next_billing_at = isoparse(d.pop("nextBillingAt"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        update_infra_billing_node_response_dto_response_billing_nodes_item = cls(
            uuid=uuid,
            node_uuid=node_uuid,
            provider_uuid=provider_uuid,
            provider=provider,
            node=node,
            next_billing_at=next_billing_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        update_infra_billing_node_response_dto_response_billing_nodes_item.additional_properties = d
        return update_infra_billing_node_response_dto_response_billing_nodes_item

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
