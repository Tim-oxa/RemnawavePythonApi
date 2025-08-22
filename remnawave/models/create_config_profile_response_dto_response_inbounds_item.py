from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateConfigProfileResponseDtoResponseInboundsItem")


@_attrs_define
class CreateConfigProfileResponseDtoResponseInboundsItem:
    """
    Attributes:
        uuid (UUID):
        profile_uuid (UUID):
        tag (str):
        type_ (str):
        network (Union[None, str]):
        security (Union[None, str]):
        port (Union[None, float]):
        raw_inbound (Any):
    """

    uuid: UUID
    profile_uuid: UUID
    tag: str
    type_: str
    network: Union[None, str]
    security: Union[None, str]
    port: Union[None, float]
    raw_inbound: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        profile_uuid = str(self.profile_uuid)

        tag = self.tag

        type_ = self.type_

        network: Union[None, str]
        network = self.network

        security: Union[None, str]
        security = self.security

        port: Union[None, float]
        port = self.port

        raw_inbound = self.raw_inbound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "profileUuid": profile_uuid,
                "tag": tag,
                "type": type_,
                "network": network,
                "security": security,
                "port": port,
                "rawInbound": raw_inbound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        profile_uuid = UUID(d.pop("profileUuid"))

        tag = d.pop("tag")

        type_ = d.pop("type")

        def _parse_network(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        network = _parse_network(d.pop("network"))

        def _parse_security(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        security = _parse_security(d.pop("security"))

        def _parse_port(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        port = _parse_port(d.pop("port"))

        raw_inbound = d.pop("rawInbound")

        create_config_profile_response_dto_response_inbounds_item = cls(
            uuid=uuid,
            profile_uuid=profile_uuid,
            tag=tag,
            type_=type_,
            network=network,
            security=security,
            port=port,
            raw_inbound=raw_inbound,
        )

        create_config_profile_response_dto_response_inbounds_item.additional_properties = d
        return create_config_profile_response_dto_response_inbounds_item

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
