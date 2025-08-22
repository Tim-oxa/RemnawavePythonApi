from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FindAllApiTokensResponseDtoResponseDocs")


@_attrs_define
class FindAllApiTokensResponseDtoResponseDocs:
    """
    Attributes:
        is_docs_enabled (bool):
        scalar_path (Union[None, str]):
        swagger_path (Union[None, str]):
    """

    is_docs_enabled: bool
    scalar_path: Union[None, str]
    swagger_path: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_docs_enabled = self.is_docs_enabled

        scalar_path: Union[None, str]
        scalar_path = self.scalar_path

        swagger_path: Union[None, str]
        swagger_path = self.swagger_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isDocsEnabled": is_docs_enabled,
                "scalarPath": scalar_path,
                "swaggerPath": swagger_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_docs_enabled = d.pop("isDocsEnabled")

        def _parse_scalar_path(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        scalar_path = _parse_scalar_path(d.pop("scalarPath"))

        def _parse_swagger_path(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        swagger_path = _parse_swagger_path(d.pop("swaggerPath"))

        find_all_api_tokens_response_dto_response_docs = cls(
            is_docs_enabled=is_docs_enabled,
            scalar_path=scalar_path,
            swagger_path=swagger_path,
        )

        find_all_api_tokens_response_dto_response_docs.additional_properties = d
        return find_all_api_tokens_response_dto_response_docs

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
