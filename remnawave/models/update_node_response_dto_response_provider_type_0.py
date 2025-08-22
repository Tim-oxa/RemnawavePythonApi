import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UpdateNodeResponseDtoResponseProviderType0")


@_attrs_define
class UpdateNodeResponseDtoResponseProviderType0:
    """
    Attributes:
        uuid (UUID):
        name (str):
        favicon_link (Union[None, str]):
        login_url (Union[None, str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    name: str
    favicon_link: Union[None, str]
    login_url: Union[None, str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
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
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        update_node_response_dto_response_provider_type_0 = cls(
            uuid=uuid,
            name=name,
            favicon_link=favicon_link,
            login_url=login_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        update_node_response_dto_response_provider_type_0.additional_properties = d
        return update_node_response_dto_response_provider_type_0

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
