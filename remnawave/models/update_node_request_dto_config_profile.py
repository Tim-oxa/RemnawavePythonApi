from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateNodeRequestDtoConfigProfile")


@_attrs_define
class UpdateNodeRequestDtoConfigProfile:
    """
    Attributes:
        active_config_profile_uuid (UUID):
        active_inbounds (list[UUID]):
    """

    active_config_profile_uuid: UUID
    active_inbounds: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_config_profile_uuid = str(self.active_config_profile_uuid)

        active_inbounds = []
        for active_inbounds_item_data in self.active_inbounds:
            active_inbounds_item = str(active_inbounds_item_data)
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
        d = dict(src_dict)
        active_config_profile_uuid = UUID(d.pop("activeConfigProfileUuid"))

        active_inbounds = []
        _active_inbounds = d.pop("activeInbounds")
        for active_inbounds_item_data in _active_inbounds:
            active_inbounds_item = UUID(active_inbounds_item_data)

            active_inbounds.append(active_inbounds_item)

        update_node_request_dto_config_profile = cls(
            active_config_profile_uuid=active_config_profile_uuid,
            active_inbounds=active_inbounds,
        )

        update_node_request_dto_config_profile.additional_properties = d
        return update_node_request_dto_config_profile

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
