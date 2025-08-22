from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelegramCallbackRequestDto")


@_attrs_define
class TelegramCallbackRequestDto:
    """
    Attributes:
        id (float):
        first_name (str):
        auth_date (float):
        hash_ (str):
        last_name (Union[Unset, str]):
        username (Union[Unset, str]):
        photo_url (Union[Unset, str]):
    """

    id: float
    first_name: str
    auth_date: float
    hash_: str
    last_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    photo_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        auth_date = self.auth_date

        hash_ = self.hash_

        last_name = self.last_name

        username = self.username

        photo_url = self.photo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "auth_date": auth_date,
                "hash": hash_,
            }
        )
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if username is not UNSET:
            field_dict["username"] = username
        if photo_url is not UNSET:
            field_dict["photo_url"] = photo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("first_name")

        auth_date = d.pop("auth_date")

        hash_ = d.pop("hash")

        last_name = d.pop("last_name", UNSET)

        username = d.pop("username", UNSET)

        photo_url = d.pop("photo_url", UNSET)

        telegram_callback_request_dto = cls(
            id=id,
            first_name=first_name,
            auth_date=auth_date,
            hash_=hash_,
            last_name=last_name,
            username=username,
            photo_url=photo_url,
        )

        telegram_callback_request_dto.additional_properties = d
        return telegram_callback_request_dto

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
