from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_host_response_dto_response_security_layer import UpdateHostResponseDtoResponseSecurityLayer
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_host_response_dto_response_inbound import UpdateHostResponseDtoResponseInbound


T = TypeVar("T", bound="UpdateHostResponseDtoResponse")


@_attrs_define
class UpdateHostResponseDtoResponse:
    """
    Attributes:
        uuid (UUID):
        view_position (int):
        remark (str):
        address (str):
        port (int):
        path (Union[None, str]):
        sni (Union[None, str]):
        host (Union[None, str]):
        alpn (Union[None, str]):
        fingerprint (Union[None, str]):
        x_http_extra_params (Any):
        mux_params (Any):
        sockopt_params (Any):
        inbound (UpdateHostResponseDtoResponseInbound):
        server_description (Union[None, str]):
        tag (Union[None, str]):
        is_disabled (Union[Unset, bool]):  Default: False.
        security_layer (Union[Unset, UpdateHostResponseDtoResponseSecurityLayer]):  Default:
            UpdateHostResponseDtoResponseSecurityLayer.DEFAULT.
        is_hidden (Union[Unset, bool]):  Default: False.
        override_sni_from_address (Union[Unset, bool]):  Default: False.
    """

    uuid: UUID
    view_position: int
    remark: str
    address: str
    port: int
    path: Union[None, str]
    sni: Union[None, str]
    host: Union[None, str]
    alpn: Union[None, str]
    fingerprint: Union[None, str]
    x_http_extra_params: Any
    mux_params: Any
    sockopt_params: Any
    inbound: "UpdateHostResponseDtoResponseInbound"
    server_description: Union[None, str]
    tag: Union[None, str]
    is_disabled: Union[Unset, bool] = False
    security_layer: Union[Unset, UpdateHostResponseDtoResponseSecurityLayer] = (
        UpdateHostResponseDtoResponseSecurityLayer.DEFAULT
    )
    is_hidden: Union[Unset, bool] = False
    override_sni_from_address: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        view_position = self.view_position

        remark = self.remark

        address = self.address

        port = self.port

        path: Union[None, str]
        path = self.path

        sni: Union[None, str]
        sni = self.sni

        host: Union[None, str]
        host = self.host

        alpn: Union[None, str]
        alpn = self.alpn

        fingerprint: Union[None, str]
        fingerprint = self.fingerprint

        x_http_extra_params = self.x_http_extra_params

        mux_params = self.mux_params

        sockopt_params = self.sockopt_params

        inbound = self.inbound.to_dict()

        server_description: Union[None, str]
        server_description = self.server_description

        tag: Union[None, str]
        tag = self.tag

        is_disabled = self.is_disabled

        security_layer: Union[Unset, str] = UNSET
        if not isinstance(self.security_layer, Unset):
            security_layer = self.security_layer.value

        is_hidden = self.is_hidden

        override_sni_from_address = self.override_sni_from_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "viewPosition": view_position,
                "remark": remark,
                "address": address,
                "port": port,
                "path": path,
                "sni": sni,
                "host": host,
                "alpn": alpn,
                "fingerprint": fingerprint,
                "xHttpExtraParams": x_http_extra_params,
                "muxParams": mux_params,
                "sockoptParams": sockopt_params,
                "inbound": inbound,
                "serverDescription": server_description,
                "tag": tag,
            }
        )
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if security_layer is not UNSET:
            field_dict["securityLayer"] = security_layer
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if override_sni_from_address is not UNSET:
            field_dict["overrideSniFromAddress"] = override_sni_from_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_host_response_dto_response_inbound import UpdateHostResponseDtoResponseInbound

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        view_position = d.pop("viewPosition")

        remark = d.pop("remark")

        address = d.pop("address")

        port = d.pop("port")

        def _parse_path(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        path = _parse_path(d.pop("path"))

        def _parse_sni(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sni = _parse_sni(d.pop("sni"))

        def _parse_host(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        host = _parse_host(d.pop("host"))

        def _parse_alpn(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        alpn = _parse_alpn(d.pop("alpn"))

        def _parse_fingerprint(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint"))

        x_http_extra_params = d.pop("xHttpExtraParams")

        mux_params = d.pop("muxParams")

        sockopt_params = d.pop("sockoptParams")

        inbound = UpdateHostResponseDtoResponseInbound.from_dict(d.pop("inbound"))

        def _parse_server_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        server_description = _parse_server_description(d.pop("serverDescription"))

        def _parse_tag(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tag = _parse_tag(d.pop("tag"))

        is_disabled = d.pop("isDisabled", UNSET)

        _security_layer = d.pop("securityLayer", UNSET)
        security_layer: Union[Unset, UpdateHostResponseDtoResponseSecurityLayer]
        if isinstance(_security_layer, Unset):
            security_layer = UNSET
        else:
            security_layer = UpdateHostResponseDtoResponseSecurityLayer(_security_layer)

        is_hidden = d.pop("isHidden", UNSET)

        override_sni_from_address = d.pop("overrideSniFromAddress", UNSET)

        update_host_response_dto_response = cls(
            uuid=uuid,
            view_position=view_position,
            remark=remark,
            address=address,
            port=port,
            path=path,
            sni=sni,
            host=host,
            alpn=alpn,
            fingerprint=fingerprint,
            x_http_extra_params=x_http_extra_params,
            mux_params=mux_params,
            sockopt_params=sockopt_params,
            inbound=inbound,
            server_description=server_description,
            tag=tag,
            is_disabled=is_disabled,
            security_layer=security_layer,
            is_hidden=is_hidden,
            override_sni_from_address=override_sni_from_address,
        )

        update_host_response_dto_response.additional_properties = d
        return update_host_response_dto_response

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
