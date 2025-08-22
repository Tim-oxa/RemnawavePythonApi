import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_infra_providers_response_dto_response_providers_item_billing_history import (
        GetInfraProvidersResponseDtoResponseProvidersItemBillingHistory,
    )
    from ..models.get_infra_providers_response_dto_response_providers_item_billing_nodes_item import (
        GetInfraProvidersResponseDtoResponseProvidersItemBillingNodesItem,
    )


T = TypeVar("T", bound="GetInfraProvidersResponseDtoResponseProvidersItem")


@_attrs_define
class GetInfraProvidersResponseDtoResponseProvidersItem:
    """
    Attributes:
        uuid (UUID):
        name (str):
        favicon_link (Union[None, str]):
        login_url (Union[None, str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        billing_history (GetInfraProvidersResponseDtoResponseProvidersItemBillingHistory):
        billing_nodes (list['GetInfraProvidersResponseDtoResponseProvidersItemBillingNodesItem']):
    """

    uuid: UUID
    name: str
    favicon_link: Union[None, str]
    login_url: Union[None, str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    billing_history: "GetInfraProvidersResponseDtoResponseProvidersItemBillingHistory"
    billing_nodes: list["GetInfraProvidersResponseDtoResponseProvidersItemBillingNodesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        favicon_link: Union[None, str]
        favicon_link = self.favicon_link

        login_url: Union[None, str]
        login_url = self.login_url

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        billing_history = self.billing_history.to_dict()

        billing_nodes = []
        for billing_nodes_item_data in self.billing_nodes:
            billing_nodes_item = billing_nodes_item_data.to_dict()
            billing_nodes.append(billing_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "faviconLink": favicon_link,
                "loginUrl": login_url,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "billingHistory": billing_history,
                "billingNodes": billing_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_infra_providers_response_dto_response_providers_item_billing_history import (
            GetInfraProvidersResponseDtoResponseProvidersItemBillingHistory,
        )
        from ..models.get_infra_providers_response_dto_response_providers_item_billing_nodes_item import (
            GetInfraProvidersResponseDtoResponseProvidersItemBillingNodesItem,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        def _parse_favicon_link(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        favicon_link = _parse_favicon_link(d.pop("faviconLink"))

        def _parse_login_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        login_url = _parse_login_url(d.pop("loginUrl"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        billing_history = GetInfraProvidersResponseDtoResponseProvidersItemBillingHistory.from_dict(
            d.pop("billingHistory")
        )

        billing_nodes = []
        _billing_nodes = d.pop("billingNodes")
        for billing_nodes_item_data in _billing_nodes:
            billing_nodes_item = GetInfraProvidersResponseDtoResponseProvidersItemBillingNodesItem.from_dict(
                billing_nodes_item_data
            )

            billing_nodes.append(billing_nodes_item)

        get_infra_providers_response_dto_response_providers_item = cls(
            uuid=uuid,
            name=name,
            favicon_link=favicon_link,
            login_url=login_url,
            created_at=created_at,
            updated_at=updated_at,
            billing_history=billing_history,
            billing_nodes=billing_nodes,
        )

        get_infra_providers_response_dto_response_providers_item.additional_properties = d
        return get_infra_providers_response_dto_response_providers_item

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
