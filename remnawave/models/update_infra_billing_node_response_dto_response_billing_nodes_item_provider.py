from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider")


@_attrs_define
class UpdateInfraBillingNodeResponseDtoResponseBillingNodesItemProvider:
    """
    Attributes:
        uuid (UUID):
        name (str):
        login_url (Union[None, str]):
        favicon_link (Union[None, str]):
    """

    uuid: UUID
    name: str
    login_url: Union[None, str]
    favicon_link: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        login_url: Union[None, str]
        login_url = self.login_url

        favicon_link: Union[None, str]
        favicon_link = self.favicon_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "loginUrl": login_url,
                "faviconLink": favicon_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        def _parse_login_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        login_url = _parse_login_url(d.pop("loginUrl"))

        def _parse_favicon_link(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        favicon_link = _parse_favicon_link(d.pop("faviconLink"))

        update_infra_billing_node_response_dto_response_billing_nodes_item_provider = cls(
            uuid=uuid,
            name=name,
            login_url=login_url,
            favicon_link=favicon_link,
        )

        update_infra_billing_node_response_dto_response_billing_nodes_item_provider.additional_properties = d
        return update_infra_billing_node_response_dto_response_billing_nodes_item_provider

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
