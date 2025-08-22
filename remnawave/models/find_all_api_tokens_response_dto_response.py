from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.find_all_api_tokens_response_dto_response_api_keys_item import (
        FindAllApiTokensResponseDtoResponseApiKeysItem,
    )
    from ..models.find_all_api_tokens_response_dto_response_docs import FindAllApiTokensResponseDtoResponseDocs


T = TypeVar("T", bound="FindAllApiTokensResponseDtoResponse")


@_attrs_define
class FindAllApiTokensResponseDtoResponse:
    """
    Attributes:
        api_keys (list['FindAllApiTokensResponseDtoResponseApiKeysItem']):
        docs (FindAllApiTokensResponseDtoResponseDocs):
    """

    api_keys: list["FindAllApiTokensResponseDtoResponseApiKeysItem"]
    docs: "FindAllApiTokensResponseDtoResponseDocs"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        docs = self.docs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKeys": api_keys,
                "docs": docs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.find_all_api_tokens_response_dto_response_api_keys_item import (
            FindAllApiTokensResponseDtoResponseApiKeysItem,
        )
        from ..models.find_all_api_tokens_response_dto_response_docs import FindAllApiTokensResponseDtoResponseDocs

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("apiKeys")
        for api_keys_item_data in _api_keys:
            api_keys_item = FindAllApiTokensResponseDtoResponseApiKeysItem.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        docs = FindAllApiTokensResponseDtoResponseDocs.from_dict(d.pop("docs"))

        find_all_api_tokens_response_dto_response = cls(
            api_keys=api_keys,
            docs=docs,
        )

        find_all_api_tokens_response_dto_response.additional_properties = d
        return find_all_api_tokens_response_dto_response

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
