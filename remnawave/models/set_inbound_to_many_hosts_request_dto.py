from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetInboundToManyHostsRequestDto")


@_attrs_define
class SetInboundToManyHostsRequestDto:
    """
    Attributes:
        uuids (list[UUID]):
        config_profile_uuid (UUID):
        config_profile_inbound_uuid (UUID):
    """

    uuids: list[UUID]
    config_profile_uuid: UUID
    config_profile_inbound_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuids = []
        for uuids_item_data in self.uuids:
            uuids_item = str(uuids_item_data)
            uuids.append(uuids_item)

        config_profile_uuid = str(self.config_profile_uuid)

        config_profile_inbound_uuid = str(self.config_profile_inbound_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuids": uuids,
                "configProfileUuid": config_profile_uuid,
                "configProfileInboundUuid": config_profile_inbound_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuids = []
        _uuids = d.pop("uuids")
        for uuids_item_data in _uuids:
            uuids_item = UUID(uuids_item_data)

            uuids.append(uuids_item)

        config_profile_uuid = UUID(d.pop("configProfileUuid"))

        config_profile_inbound_uuid = UUID(d.pop("configProfileInboundUuid"))

        set_inbound_to_many_hosts_request_dto = cls(
            uuids=uuids,
            config_profile_uuid=config_profile_uuid,
            config_profile_inbound_uuid=config_profile_inbound_uuid,
        )

        set_inbound_to_many_hosts_request_dto.additional_properties = d
        return set_inbound_to_many_hosts_request_dto

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
