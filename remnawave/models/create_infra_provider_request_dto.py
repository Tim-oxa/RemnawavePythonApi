from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInfraProviderRequestDto")


@_attrs_define
class CreateInfraProviderRequestDto:
    """
    Attributes:
        name (str):
        favicon_link (Union[Unset, str]):
        login_url (Union[Unset, str]):
    """

    name: str
    favicon_link: Union[Unset, str] = UNSET
    login_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        favicon_link = self.favicon_link

        login_url = self.login_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if favicon_link is not UNSET:
            field_dict["faviconLink"] = favicon_link
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        favicon_link = d.pop("faviconLink", UNSET)

        login_url = d.pop("loginUrl", UNSET)

        create_infra_provider_request_dto = cls(
            name=name,
            favicon_link=favicon_link,
            login_url=login_url,
        )

        create_infra_provider_request_dto.additional_properties = d
        return create_infra_provider_request_dto

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
