from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateInfraProviderRequestDto")


@_attrs_define
class UpdateInfraProviderRequestDto:
    """
    Attributes:
        uuid (UUID):
        name (Union[Unset, str]):
        favicon_link (Union[None, Unset, str]):
        login_url (Union[None, Unset, str]):
    """

    uuid: UUID
    name: Union[Unset, str] = UNSET
    favicon_link: Union[None, Unset, str] = UNSET
    login_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        favicon_link: Union[None, Unset, str]
        if isinstance(self.favicon_link, Unset):
            favicon_link = UNSET
        else:
            favicon_link = self.favicon_link

        login_url: Union[None, Unset, str]
        if isinstance(self.login_url, Unset):
            login_url = UNSET
        else:
            login_url = self.login_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if favicon_link is not UNSET:
            field_dict["faviconLink"] = favicon_link
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name", UNSET)

        def _parse_favicon_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        favicon_link = _parse_favicon_link(d.pop("faviconLink", UNSET))

        def _parse_login_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        login_url = _parse_login_url(d.pop("loginUrl", UNSET))

        update_infra_provider_request_dto = cls(
            uuid=uuid,
            name=name,
            favicon_link=favicon_link,
            login_url=login_url,
        )

        update_infra_provider_request_dto.additional_properties = d
        return update_infra_provider_request_dto

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
