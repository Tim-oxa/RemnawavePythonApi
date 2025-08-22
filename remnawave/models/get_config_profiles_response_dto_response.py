from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_config_profiles_response_dto_response_config_profiles_item import (
        GetConfigProfilesResponseDtoResponseConfigProfilesItem,
    )


T = TypeVar("T", bound="GetConfigProfilesResponseDtoResponse")


@_attrs_define
class GetConfigProfilesResponseDtoResponse:
    """
    Attributes:
        total (float):
        config_profiles (list['GetConfigProfilesResponseDtoResponseConfigProfilesItem']):
    """

    total: float
    config_profiles: list["GetConfigProfilesResponseDtoResponseConfigProfilesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        config_profiles = []
        for config_profiles_item_data in self.config_profiles:
            config_profiles_item = config_profiles_item_data.to_dict()
            config_profiles.append(config_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "configProfiles": config_profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_config_profiles_response_dto_response_config_profiles_item import (
            GetConfigProfilesResponseDtoResponseConfigProfilesItem,
        )

        d = dict(src_dict)
        total = d.pop("total")

        config_profiles = []
        _config_profiles = d.pop("configProfiles")
        for config_profiles_item_data in _config_profiles:
            config_profiles_item = GetConfigProfilesResponseDtoResponseConfigProfilesItem.from_dict(
                config_profiles_item_data
            )

            config_profiles.append(config_profiles_item)

        get_config_profiles_response_dto_response = cls(
            total=total,
            config_profiles=config_profiles,
        )

        get_config_profiles_response_dto_response.additional_properties = d
        return get_config_profiles_response_dto_response

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
