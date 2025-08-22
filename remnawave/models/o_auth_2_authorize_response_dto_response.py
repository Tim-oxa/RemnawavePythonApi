from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OAuth2AuthorizeResponseDtoResponse")


@_attrs_define
class OAuth2AuthorizeResponseDtoResponse:
    """
    Attributes:
        authorization_url (Union[None, str]):
    """

    authorization_url: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_url: Union[None, str]
        authorization_url = self.authorization_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorizationUrl": authorization_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_authorization_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        authorization_url = _parse_authorization_url(d.pop("authorizationUrl"))

        o_auth_2_authorize_response_dto_response = cls(
            authorization_url=authorization_url,
        )

        o_auth_2_authorize_response_dto_response.additional_properties = d
        return o_auth_2_authorize_response_dto_response

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
