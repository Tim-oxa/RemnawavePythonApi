from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_config_profile_request_dto_config import UpdateConfigProfileRequestDtoConfig


T = TypeVar("T", bound="UpdateConfigProfileRequestDto")


@_attrs_define
class UpdateConfigProfileRequestDto:
    """
    Attributes:
        uuid (UUID):
        name (Union[Unset, str]):
        config (Union[Unset, UpdateConfigProfileRequestDtoConfig]):
    """

    uuid: UUID
    name: Union[Unset, str] = UNSET
    config: Union[Unset, "UpdateConfigProfileRequestDtoConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_config_profile_request_dto_config import UpdateConfigProfileRequestDtoConfig

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, UpdateConfigProfileRequestDtoConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = UpdateConfigProfileRequestDtoConfig.from_dict(_config)

        update_config_profile_request_dto = cls(
            uuid=uuid,
            name=name,
            config=config,
        )

        update_config_profile_request_dto.additional_properties = d
        return update_config_profile_request_dto

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
