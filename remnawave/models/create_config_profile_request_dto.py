from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_config_profile_request_dto_config import CreateConfigProfileRequestDtoConfig


T = TypeVar("T", bound="CreateConfigProfileRequestDto")


@_attrs_define
class CreateConfigProfileRequestDto:
    """
    Attributes:
        name (str):
        config (CreateConfigProfileRequestDtoConfig):
    """

    name: str
    config: "CreateConfigProfileRequestDtoConfig"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_config_profile_request_dto_config import CreateConfigProfileRequestDtoConfig

        d = dict(src_dict)
        name = d.pop("name")

        config = CreateConfigProfileRequestDtoConfig.from_dict(d.pop("config"))

        create_config_profile_request_dto = cls(
            name=name,
            config=config,
        )

        create_config_profile_request_dto.additional_properties = d
        return create_config_profile_request_dto

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
