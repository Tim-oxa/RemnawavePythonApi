from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_status_response_dto_response_oauth_2_providers import GetStatusResponseDtoResponseOauth2Providers


T = TypeVar("T", bound="GetStatusResponseDtoResponseOauth2")


@_attrs_define
class GetStatusResponseDtoResponseOauth2:
    """
    Attributes:
        providers (GetStatusResponseDtoResponseOauth2Providers):
    """

    providers: "GetStatusResponseDtoResponseOauth2Providers"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers = self.providers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_status_response_dto_response_oauth_2_providers import (
            GetStatusResponseDtoResponseOauth2Providers,
        )

        d = dict(src_dict)
        providers = GetStatusResponseDtoResponseOauth2Providers.from_dict(d.pop("providers"))

        get_status_response_dto_response_oauth_2 = cls(
            providers=providers,
        )

        get_status_response_dto_response_oauth_2.additional_properties = d
        return get_status_response_dto_response_oauth_2

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
