from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_additional_params_type_0 import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_mux_params_type_0 import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_protocol_options_type_0 import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_sockopt_params_type_0 import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0,
    )
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_x_http_extra_params_type_0 import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0,
    )


T = TypeVar("T", bound="GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem")


@_attrs_define
class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItem:
    """
    Attributes:
        address (Union[None, Unset, str]):
        alpn (Union[None, Unset, str]):
        fingerprint (Union[None, Unset, str]):
        host (Union[None, Unset, str]):
        network (Union[None, Unset, str]):
        password (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        public_key (Union[None, Unset, str]):
        port (Union[None, Unset, float]):
        protocol (Union[None, Unset, str]):
        remark (Union[None, Unset, str]):
        short_id (Union[None, Unset, str]):
        sni (Union[None, Unset, str]):
        spider_x (Union[None, Unset, str]):
        tls (Union[None, Unset, str]):
        header_type (Union[None, Unset, str]):
        additional_params (Union['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0',
            None, Unset]):
        x_http_extra_params (Union['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0',
            None, Unset]):
        mux_params (Union['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0', None, Unset]):
        sockopt_params (Union['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0', None,
            Unset]):
        server_description (Union[None, Unset, str]):
        flow (Union[None, Unset, str]):
        protocol_options (Union['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0',
            None, Unset]):
        db_data (Union[Unset, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData]):
    """

    address: Union[None, Unset, str] = UNSET
    alpn: Union[None, Unset, str] = UNSET
    fingerprint: Union[None, Unset, str] = UNSET
    host: Union[None, Unset, str] = UNSET
    network: Union[None, Unset, str] = UNSET
    password: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    public_key: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, float] = UNSET
    protocol: Union[None, Unset, str] = UNSET
    remark: Union[None, Unset, str] = UNSET
    short_id: Union[None, Unset, str] = UNSET
    sni: Union[None, Unset, str] = UNSET
    spider_x: Union[None, Unset, str] = UNSET
    tls: Union[None, Unset, str] = UNSET
    header_type: Union[None, Unset, str] = UNSET
    additional_params: Union[
        "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0", None, Unset
    ] = UNSET
    x_http_extra_params: Union[
        "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0", None, Unset
    ] = UNSET
    mux_params: Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0", None, Unset] = UNSET
    sockopt_params: Union[
        "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0", None, Unset
    ] = UNSET
    server_description: Union[None, Unset, str] = UNSET
    flow: Union[None, Unset, str] = UNSET
    protocol_options: Union[
        "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0", None, Unset
    ] = UNSET
    db_data: Union[Unset, "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_additional_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_mux_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_protocol_options_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_sockopt_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_x_http_extra_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0,
        )

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        alpn: Union[None, Unset, str]
        if isinstance(self.alpn, Unset):
            alpn = UNSET
        else:
            alpn = self.alpn

        fingerprint: Union[None, Unset, str]
        if isinstance(self.fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = self.fingerprint

        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        network: Union[None, Unset, str]
        if isinstance(self.network, Unset):
            network = UNSET
        else:
            network = self.network

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        public_key: Union[None, Unset, str]
        if isinstance(self.public_key, Unset):
            public_key = UNSET
        else:
            public_key = self.public_key

        port: Union[None, Unset, float]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        protocol: Union[None, Unset, str]
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        remark: Union[None, Unset, str]
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        short_id: Union[None, Unset, str]
        if isinstance(self.short_id, Unset):
            short_id = UNSET
        else:
            short_id = self.short_id

        sni: Union[None, Unset, str]
        if isinstance(self.sni, Unset):
            sni = UNSET
        else:
            sni = self.sni

        spider_x: Union[None, Unset, str]
        if isinstance(self.spider_x, Unset):
            spider_x = UNSET
        else:
            spider_x = self.spider_x

        tls: Union[None, Unset, str]
        if isinstance(self.tls, Unset):
            tls = UNSET
        else:
            tls = self.tls

        header_type: Union[None, Unset, str]
        if isinstance(self.header_type, Unset):
            header_type = UNSET
        else:
            header_type = self.header_type

        additional_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.additional_params, Unset):
            additional_params = UNSET
        elif isinstance(
            self.additional_params, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0
        ):
            additional_params = self.additional_params.to_dict()
        else:
            additional_params = self.additional_params

        x_http_extra_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.x_http_extra_params, Unset):
            x_http_extra_params = UNSET
        elif isinstance(
            self.x_http_extra_params, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0
        ):
            x_http_extra_params = self.x_http_extra_params.to_dict()
        else:
            x_http_extra_params = self.x_http_extra_params

        mux_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.mux_params, Unset):
            mux_params = UNSET
        elif isinstance(self.mux_params, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0):
            mux_params = self.mux_params.to_dict()
        else:
            mux_params = self.mux_params

        sockopt_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.sockopt_params, Unset):
            sockopt_params = UNSET
        elif isinstance(
            self.sockopt_params, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0
        ):
            sockopt_params = self.sockopt_params.to_dict()
        else:
            sockopt_params = self.sockopt_params

        server_description: Union[None, Unset, str]
        if isinstance(self.server_description, Unset):
            server_description = UNSET
        else:
            server_description = self.server_description

        flow: Union[None, Unset, str]
        if isinstance(self.flow, Unset):
            flow = UNSET
        else:
            flow = self.flow

        protocol_options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.protocol_options, Unset):
            protocol_options = UNSET
        elif isinstance(
            self.protocol_options, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0
        ):
            protocol_options = self.protocol_options.to_dict()
        else:
            protocol_options = self.protocol_options

        db_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.db_data, Unset):
            db_data = self.db_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if alpn is not UNSET:
            field_dict["alpn"] = alpn
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if host is not UNSET:
            field_dict["host"] = host
        if network is not UNSET:
            field_dict["network"] = network
        if password is not UNSET:
            field_dict["password"] = password
        if path is not UNSET:
            field_dict["path"] = path
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if remark is not UNSET:
            field_dict["remark"] = remark
        if short_id is not UNSET:
            field_dict["shortId"] = short_id
        if sni is not UNSET:
            field_dict["sni"] = sni
        if spider_x is not UNSET:
            field_dict["spiderX"] = spider_x
        if tls is not UNSET:
            field_dict["tls"] = tls
        if header_type is not UNSET:
            field_dict["headerType"] = header_type
        if additional_params is not UNSET:
            field_dict["additionalParams"] = additional_params
        if x_http_extra_params is not UNSET:
            field_dict["xHttpExtraParams"] = x_http_extra_params
        if mux_params is not UNSET:
            field_dict["muxParams"] = mux_params
        if sockopt_params is not UNSET:
            field_dict["sockoptParams"] = sockopt_params
        if server_description is not UNSET:
            field_dict["serverDescription"] = server_description
        if flow is not UNSET:
            field_dict["flow"] = flow
        if protocol_options is not UNSET:
            field_dict["protocolOptions"] = protocol_options
        if db_data is not UNSET:
            field_dict["dbData"] = db_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_additional_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_mux_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_protocol_options_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_sockopt_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0,
        )
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_x_http_extra_params_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0,
        )

        d = dict(src_dict)

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_alpn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alpn = _parse_alpn(d.pop("alpn", UNSET))

        def _parse_fingerprint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint", UNSET))

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_network(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        network = _parse_network(d.pop("network", UNSET))

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_public_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        public_key = _parse_public_key(d.pop("publicKey", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_remark(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remark = _parse_remark(d.pop("remark", UNSET))

        def _parse_short_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_id = _parse_short_id(d.pop("shortId", UNSET))

        def _parse_sni(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sni = _parse_sni(d.pop("sni", UNSET))

        def _parse_spider_x(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        spider_x = _parse_spider_x(d.pop("spiderX", UNSET))

        def _parse_tls(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tls = _parse_tls(d.pop("tls", UNSET))

        def _parse_header_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        header_type = _parse_header_type(d.pop("headerType", UNSET))

        def _parse_additional_params(
            data: object,
        ) -> Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_params_type_0 = (
                    GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0.from_dict(data)
                )

                return additional_params_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemAdditionalParamsType0", None, Unset],
                data,
            )

        additional_params = _parse_additional_params(d.pop("additionalParams", UNSET))

        def _parse_x_http_extra_params(
            data: object,
        ) -> Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                x_http_extra_params_type_0 = (
                    GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0.from_dict(data)
                )

                return x_http_extra_params_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemXHttpExtraParamsType0", None, Unset],
                data,
            )

        x_http_extra_params = _parse_x_http_extra_params(d.pop("xHttpExtraParams", UNSET))

        def _parse_mux_params(
            data: object,
        ) -> Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mux_params_type_0 = (
                    GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0.from_dict(data)
                )

                return mux_params_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemMuxParamsType0", None, Unset], data
            )

        mux_params = _parse_mux_params(d.pop("muxParams", UNSET))

        def _parse_sockopt_params(
            data: object,
        ) -> Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sockopt_params_type_0 = (
                    GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0.from_dict(data)
                )

                return sockopt_params_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemSockoptParamsType0", None, Unset],
                data,
            )

        sockopt_params = _parse_sockopt_params(d.pop("sockoptParams", UNSET))

        def _parse_server_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        server_description = _parse_server_description(d.pop("serverDescription", UNSET))

        def _parse_flow(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        flow = _parse_flow(d.pop("flow", UNSET))

        def _parse_protocol_options(
            data: object,
        ) -> Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                protocol_options_type_0 = (
                    GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0.from_dict(data)
                )

                return protocol_options_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemProtocolOptionsType0", None, Unset],
                data,
            )

        protocol_options = _parse_protocol_options(d.pop("protocolOptions", UNSET))

        _db_data = d.pop("dbData", UNSET)
        db_data: Union[Unset, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData]
        if isinstance(_db_data, Unset):
            db_data = UNSET
        else:
            db_data = GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData.from_dict(_db_data)

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item = cls(
            address=address,
            alpn=alpn,
            fingerprint=fingerprint,
            host=host,
            network=network,
            password=password,
            path=path,
            public_key=public_key,
            port=port,
            protocol=protocol,
            remark=remark,
            short_id=short_id,
            sni=sni,
            spider_x=spider_x,
            tls=tls,
            header_type=header_type,
            additional_params=additional_params,
            x_http_extra_params=x_http_extra_params,
            mux_params=mux_params,
            sockopt_params=sockopt_params,
            server_description=server_description,
            flow=flow,
            protocol_options=protocol_options,
            db_data=db_data,
        )

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item.additional_properties = d
        return get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item

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
