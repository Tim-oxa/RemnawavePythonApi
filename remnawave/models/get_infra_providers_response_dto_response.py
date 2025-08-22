from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_infra_providers_response_dto_response_providers_item import (
        GetInfraProvidersResponseDtoResponseProvidersItem,
    )


T = TypeVar("T", bound="GetInfraProvidersResponseDtoResponse")


@_attrs_define
class GetInfraProvidersResponseDtoResponse:
    """
    Attributes:
        total (float):
        providers (list['GetInfraProvidersResponseDtoResponseProvidersItem']):
    """

    total: float
    providers: list["GetInfraProvidersResponseDtoResponseProvidersItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_infra_providers_response_dto_response_providers_item import (
            GetInfraProvidersResponseDtoResponseProvidersItem,
        )

        d = dict(src_dict)
        total = d.pop("total")

        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = GetInfraProvidersResponseDtoResponseProvidersItem.from_dict(providers_item_data)

            providers.append(providers_item)

        get_infra_providers_response_dto_response = cls(
            total=total,
            providers=providers,
        )

        get_infra_providers_response_dto_response.additional_properties = d
        return get_infra_providers_response_dto_response

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
