import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FindAllApiTokensResponseDtoResponseApiKeysItem")


@_attrs_define
class FindAllApiTokensResponseDtoResponseApiKeysItem:
    """
    Attributes:
        uuid (UUID):
        token (str):
        token_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    token: str
    token_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        token = self.token

        token_name = self.token_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "token": token,
                "tokenName": token_name,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        token = d.pop("token")

        token_name = d.pop("tokenName")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        find_all_api_tokens_response_dto_response_api_keys_item = cls(
            uuid=uuid,
            token=token,
            token_name=token_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        find_all_api_tokens_response_dto_response_api_keys_item.additional_properties = d
        return find_all_api_tokens_response_dto_response_api_keys_item

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
