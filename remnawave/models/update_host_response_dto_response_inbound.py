from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateHostResponseDtoResponseInbound")


@_attrs_define
class UpdateHostResponseDtoResponseInbound:
    """
    Attributes:
        config_profile_uuid (Union[None, UUID]):
        config_profile_inbound_uuid (Union[None, UUID]):
    """

    config_profile_uuid: Union[None, UUID]
    config_profile_inbound_uuid: Union[None, UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_profile_uuid: Union[None, str]
        if isinstance(self.config_profile_uuid, UUID):
            config_profile_uuid = str(self.config_profile_uuid)
        else:
            config_profile_uuid = self.config_profile_uuid

        config_profile_inbound_uuid: Union[None, str]
        if isinstance(self.config_profile_inbound_uuid, UUID):
            config_profile_inbound_uuid = str(self.config_profile_inbound_uuid)
        else:
            config_profile_inbound_uuid = self.config_profile_inbound_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configProfileUuid": config_profile_uuid,
                "configProfileInboundUuid": config_profile_inbound_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_config_profile_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                config_profile_uuid_type_0 = UUID(data)

                return config_profile_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        config_profile_uuid = _parse_config_profile_uuid(d.pop("configProfileUuid"))

        def _parse_config_profile_inbound_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                config_profile_inbound_uuid_type_0 = UUID(data)

                return config_profile_inbound_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        config_profile_inbound_uuid = _parse_config_profile_inbound_uuid(d.pop("configProfileInboundUuid"))

        update_host_response_dto_response_inbound = cls(
            config_profile_uuid=config_profile_uuid,
            config_profile_inbound_uuid=config_profile_inbound_uuid,
        )

        update_host_response_dto_response_inbound.additional_properties = d
        return update_host_response_dto_response_inbound

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
