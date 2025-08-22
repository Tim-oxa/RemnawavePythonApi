from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteInfraProviderByUuidResponseDtoResponse")


@_attrs_define
class DeleteInfraProviderByUuidResponseDtoResponse:
    """
    Attributes:
        is_deleted (bool):
    """

    is_deleted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_deleted = self.is_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isDeleted": is_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_deleted = d.pop("isDeleted")

        delete_infra_provider_by_uuid_response_dto_response = cls(
            is_deleted=is_deleted,
        )

        delete_infra_provider_by_uuid_response_dto_response.additional_properties = d
        return delete_infra_provider_by_uuid_response_dto_response

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
