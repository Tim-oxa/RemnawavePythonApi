from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.disable_node_response_dto_response_config_profile_active_inbounds_item import (
        DisableNodeResponseDtoResponseConfigProfileActiveInboundsItem,
    )


T = TypeVar("T", bound="DisableNodeResponseDtoResponseConfigProfile")


@_attrs_define
class DisableNodeResponseDtoResponseConfigProfile:
    """
    Attributes:
        active_config_profile_uuid (Union[None, UUID]):
        active_inbounds (list['DisableNodeResponseDtoResponseConfigProfileActiveInboundsItem']):
    """

    active_config_profile_uuid: Union[None, UUID]
    active_inbounds: list["DisableNodeResponseDtoResponseConfigProfileActiveInboundsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_config_profile_uuid: Union[None, str]
        if isinstance(self.active_config_profile_uuid, UUID):
            active_config_profile_uuid = str(self.active_config_profile_uuid)
        else:
            active_config_profile_uuid = self.active_config_profile_uuid

        active_inbounds = []
        for active_inbounds_item_data in self.active_inbounds:
            active_inbounds_item = active_inbounds_item_data.to_dict()
            active_inbounds.append(active_inbounds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activeConfigProfileUuid": active_config_profile_uuid,
                "activeInbounds": active_inbounds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disable_node_response_dto_response_config_profile_active_inbounds_item import (
            DisableNodeResponseDtoResponseConfigProfileActiveInboundsItem,
        )

        d = dict(src_dict)

        def _parse_active_config_profile_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_config_profile_uuid_type_0 = UUID(data)

                return active_config_profile_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        active_config_profile_uuid = _parse_active_config_profile_uuid(d.pop("activeConfigProfileUuid"))

        active_inbounds = []
        _active_inbounds = d.pop("activeInbounds")
        for active_inbounds_item_data in _active_inbounds:
            active_inbounds_item = DisableNodeResponseDtoResponseConfigProfileActiveInboundsItem.from_dict(
                active_inbounds_item_data
            )

            active_inbounds.append(active_inbounds_item)

        disable_node_response_dto_response_config_profile = cls(
            active_config_profile_uuid=active_config_profile_uuid,
            active_inbounds=active_inbounds,
        )

        disable_node_response_dto_response_config_profile.additional_properties = d
        return disable_node_response_dto_response_config_profile

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
