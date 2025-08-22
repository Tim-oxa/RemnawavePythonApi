from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data_raw_inbound_type_0 import (
        GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0,
    )


T = TypeVar("T", bound="GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData")


@_attrs_define
class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbData:
    """
    Attributes:
        raw_inbound (Union['GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0', None]):
        inbound_tag (str):
        uuid (str):
        config_profile_uuid (Union[None, str]):
        config_profile_inbound_uuid (Union[None, str]):
        is_disabled (bool):
        view_position (float):
        remark (str):
        is_hidden (bool):
        tag (Union[None, str]):
    """

    raw_inbound: Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0", None]
    inbound_tag: str
    uuid: str
    config_profile_uuid: Union[None, str]
    config_profile_inbound_uuid: Union[None, str]
    is_disabled: bool
    view_position: float
    remark: str
    is_hidden: bool
    tag: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data_raw_inbound_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0,
        )

        raw_inbound: Union[None, dict[str, Any]]
        if isinstance(
            self.raw_inbound, GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0
        ):
            raw_inbound = self.raw_inbound.to_dict()
        else:
            raw_inbound = self.raw_inbound

        inbound_tag = self.inbound_tag

        uuid = self.uuid

        config_profile_uuid: Union[None, str]
        config_profile_uuid = self.config_profile_uuid

        config_profile_inbound_uuid: Union[None, str]
        config_profile_inbound_uuid = self.config_profile_inbound_uuid

        is_disabled = self.is_disabled

        view_position = self.view_position

        remark = self.remark

        is_hidden = self.is_hidden

        tag: Union[None, str]
        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rawInbound": raw_inbound,
                "inboundTag": inbound_tag,
                "uuid": uuid,
                "configProfileUuid": config_profile_uuid,
                "configProfileInboundUuid": config_profile_inbound_uuid,
                "isDisabled": is_disabled,
                "viewPosition": view_position,
                "remark": remark,
                "isHidden": is_hidden,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data_raw_inbound_type_0 import (
            GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0,
        )

        d = dict(src_dict)

        def _parse_raw_inbound(
            data: object,
        ) -> Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_inbound_type_0 = (
                    GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0.from_dict(data)
                )

                return raw_inbound_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsItemDbDataRawInboundType0", None], data
            )

        raw_inbound = _parse_raw_inbound(d.pop("rawInbound"))

        inbound_tag = d.pop("inboundTag")

        uuid = d.pop("uuid")

        def _parse_config_profile_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        config_profile_uuid = _parse_config_profile_uuid(d.pop("configProfileUuid"))

        def _parse_config_profile_inbound_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        config_profile_inbound_uuid = _parse_config_profile_inbound_uuid(d.pop("configProfileInboundUuid"))

        is_disabled = d.pop("isDisabled")

        view_position = d.pop("viewPosition")

        remark = d.pop("remark")

        is_hidden = d.pop("isHidden")

        def _parse_tag(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tag = _parse_tag(d.pop("tag"))

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data = cls(
            raw_inbound=raw_inbound,
            inbound_tag=inbound_tag,
            uuid=uuid,
            config_profile_uuid=config_profile_uuid,
            config_profile_inbound_uuid=config_profile_inbound_uuid,
            is_disabled=is_disabled,
            view_position=view_position,
            remark=remark,
            is_hidden=is_hidden,
            tag=tag,
        )

        get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data.additional_properties = d
        return get_raw_subscription_by_short_uuid_response_dto_response_raw_hosts_item_db_data

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
