from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_host_request_dto_alpn import CreateHostRequestDtoAlpn
from ..models.create_host_request_dto_fingerprint import CreateHostRequestDtoFingerprint
from ..models.create_host_request_dto_security_layer import CreateHostRequestDtoSecurityLayer
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_host_request_dto_inbound import CreateHostRequestDtoInbound


T = TypeVar("T", bound="CreateHostRequestDto")


@_attrs_define
class CreateHostRequestDto:
    """
    Attributes:
        inbound (CreateHostRequestDtoInbound):
        remark (str):
        address (str):
        port (int):
        path (Union[Unset, str]):
        sni (Union[Unset, str]):
        host (Union[Unset, str]):
        alpn (Union[Unset, CreateHostRequestDtoAlpn]):
        fingerprint (Union[Unset, CreateHostRequestDtoFingerprint]):
        is_disabled (Union[Unset, bool]):  Default: False.
        security_layer (Union[Unset, CreateHostRequestDtoSecurityLayer]):  Default:
            CreateHostRequestDtoSecurityLayer.DEFAULT.
        x_http_extra_params (Union[Unset, Any]):
        mux_params (Union[Unset, Any]):
        sockopt_params (Union[Unset, Any]):
        server_description (Union[None, Unset, str]):
        tag (Union[None, Unset, str]): Optional. Host tag for categorization. Max 32 characters, uppercase letters,
            numbers, underscores and colons are allowed.
        is_hidden (Union[Unset, bool]):  Default: False.
        override_sni_from_address (Union[Unset, bool]):  Default: False.
    """

    inbound: "CreateHostRequestDtoInbound"
    remark: str
    address: str
    port: int
    path: Union[Unset, str] = UNSET
    sni: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    alpn: Union[Unset, CreateHostRequestDtoAlpn] = UNSET
    fingerprint: Union[Unset, CreateHostRequestDtoFingerprint] = UNSET
    is_disabled: Union[Unset, bool] = False
    security_layer: Union[Unset, CreateHostRequestDtoSecurityLayer] = CreateHostRequestDtoSecurityLayer.DEFAULT
    x_http_extra_params: Union[Unset, Any] = UNSET
    mux_params: Union[Unset, Any] = UNSET
    sockopt_params: Union[Unset, Any] = UNSET
    server_description: Union[None, Unset, str] = UNSET
    tag: Union[None, Unset, str] = UNSET
    is_hidden: Union[Unset, bool] = False
    override_sni_from_address: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound = self.inbound.to_dict()

        remark = self.remark

        address = self.address

        port = self.port

        path = self.path

        sni = self.sni

        host = self.host

        alpn: Union[Unset, str] = UNSET
        if not isinstance(self.alpn, Unset):
            alpn = self.alpn.value

        fingerprint: Union[Unset, str] = UNSET
        if not isinstance(self.fingerprint, Unset):
            fingerprint = self.fingerprint.value

        is_disabled = self.is_disabled

        security_layer: Union[Unset, str] = UNSET
        if not isinstance(self.security_layer, Unset):
            security_layer = self.security_layer.value

        x_http_extra_params = self.x_http_extra_params

        mux_params = self.mux_params

        sockopt_params = self.sockopt_params

        server_description: Union[None, Unset, str]
        if isinstance(self.server_description, Unset):
            server_description = UNSET
        else:
            server_description = self.server_description

        tag: Union[None, Unset, str]
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        is_hidden = self.is_hidden

        override_sni_from_address = self.override_sni_from_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inbound": inbound,
                "remark": remark,
                "address": address,
                "port": port,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if sni is not UNSET:
            field_dict["sni"] = sni
        if host is not UNSET:
            field_dict["host"] = host
        if alpn is not UNSET:
            field_dict["alpn"] = alpn
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if security_layer is not UNSET:
            field_dict["securityLayer"] = security_layer
        if x_http_extra_params is not UNSET:
            field_dict["xHttpExtraParams"] = x_http_extra_params
        if mux_params is not UNSET:
            field_dict["muxParams"] = mux_params
        if sockopt_params is not UNSET:
            field_dict["sockoptParams"] = sockopt_params
        if server_description is not UNSET:
            field_dict["serverDescription"] = server_description
        if tag is not UNSET:
            field_dict["tag"] = tag
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if override_sni_from_address is not UNSET:
            field_dict["overrideSniFromAddress"] = override_sni_from_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_host_request_dto_inbound import CreateHostRequestDtoInbound

        d = dict(src_dict)
        inbound = CreateHostRequestDtoInbound.from_dict(d.pop("inbound"))

        remark = d.pop("remark")

        address = d.pop("address")

        port = d.pop("port")

        path = d.pop("path", UNSET)

        sni = d.pop("sni", UNSET)

        host = d.pop("host", UNSET)

        _alpn = d.pop("alpn", UNSET)
        alpn: Union[Unset, CreateHostRequestDtoAlpn]
        if isinstance(_alpn, Unset):
            alpn = UNSET
        else:
            alpn = CreateHostRequestDtoAlpn(_alpn)

        _fingerprint = d.pop("fingerprint", UNSET)
        fingerprint: Union[Unset, CreateHostRequestDtoFingerprint]
        if isinstance(_fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = CreateHostRequestDtoFingerprint(_fingerprint)

        is_disabled = d.pop("isDisabled", UNSET)

        _security_layer = d.pop("securityLayer", UNSET)
        security_layer: Union[Unset, CreateHostRequestDtoSecurityLayer]
        if isinstance(_security_layer, Unset):
            security_layer = UNSET
        else:
            security_layer = CreateHostRequestDtoSecurityLayer(_security_layer)

        x_http_extra_params = d.pop("xHttpExtraParams", UNSET)

        mux_params = d.pop("muxParams", UNSET)

        sockopt_params = d.pop("sockoptParams", UNSET)

        def _parse_server_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        server_description = _parse_server_description(d.pop("serverDescription", UNSET))

        def _parse_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag = _parse_tag(d.pop("tag", UNSET))

        is_hidden = d.pop("isHidden", UNSET)

        override_sni_from_address = d.pop("overrideSniFromAddress", UNSET)

        create_host_request_dto = cls(
            inbound=inbound,
            remark=remark,
            address=address,
            port=port,
            path=path,
            sni=sni,
            host=host,
            alpn=alpn,
            fingerprint=fingerprint,
            is_disabled=is_disabled,
            security_layer=security_layer,
            x_http_extra_params=x_http_extra_params,
            mux_params=mux_params,
            sockopt_params=sockopt_params,
            server_description=server_description,
            tag=tag,
            is_hidden=is_hidden,
            override_sni_from_address=override_sni_from_address,
        )

        create_host_request_dto.additional_properties = d
        return create_host_request_dto

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
