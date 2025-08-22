from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_nodes_metrics_response_dto_response_nodes_item_inbounds_stats_item import (
        GetNodesMetricsResponseDtoResponseNodesItemInboundsStatsItem,
    )
    from ..models.get_nodes_metrics_response_dto_response_nodes_item_outbounds_stats_item import (
        GetNodesMetricsResponseDtoResponseNodesItemOutboundsStatsItem,
    )


T = TypeVar("T", bound="GetNodesMetricsResponseDtoResponseNodesItem")


@_attrs_define
class GetNodesMetricsResponseDtoResponseNodesItem:
    """
    Attributes:
        node_uuid (str):
        node_name (str):
        country_emoji (str):
        provider_name (str):
        users_online (float):
        inbounds_stats (list['GetNodesMetricsResponseDtoResponseNodesItemInboundsStatsItem']):
        outbounds_stats (list['GetNodesMetricsResponseDtoResponseNodesItemOutboundsStatsItem']):
    """

    node_uuid: str
    node_name: str
    country_emoji: str
    provider_name: str
    users_online: float
    inbounds_stats: list["GetNodesMetricsResponseDtoResponseNodesItemInboundsStatsItem"]
    outbounds_stats: list["GetNodesMetricsResponseDtoResponseNodesItemOutboundsStatsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = self.node_uuid

        node_name = self.node_name

        country_emoji = self.country_emoji

        provider_name = self.provider_name

        users_online = self.users_online

        inbounds_stats = []
        for inbounds_stats_item_data in self.inbounds_stats:
            inbounds_stats_item = inbounds_stats_item_data.to_dict()
            inbounds_stats.append(inbounds_stats_item)

        outbounds_stats = []
        for outbounds_stats_item_data in self.outbounds_stats:
            outbounds_stats_item = outbounds_stats_item_data.to_dict()
            outbounds_stats.append(outbounds_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeUuid": node_uuid,
                "nodeName": node_name,
                "countryEmoji": country_emoji,
                "providerName": provider_name,
                "usersOnline": users_online,
                "inboundsStats": inbounds_stats,
                "outboundsStats": outbounds_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_nodes_metrics_response_dto_response_nodes_item_inbounds_stats_item import (
            GetNodesMetricsResponseDtoResponseNodesItemInboundsStatsItem,
        )
        from ..models.get_nodes_metrics_response_dto_response_nodes_item_outbounds_stats_item import (
            GetNodesMetricsResponseDtoResponseNodesItemOutboundsStatsItem,
        )

        d = dict(src_dict)
        node_uuid = d.pop("nodeUuid")

        node_name = d.pop("nodeName")

        country_emoji = d.pop("countryEmoji")

        provider_name = d.pop("providerName")

        users_online = d.pop("usersOnline")

        inbounds_stats = []
        _inbounds_stats = d.pop("inboundsStats")
        for inbounds_stats_item_data in _inbounds_stats:
            inbounds_stats_item = GetNodesMetricsResponseDtoResponseNodesItemInboundsStatsItem.from_dict(
                inbounds_stats_item_data
            )

            inbounds_stats.append(inbounds_stats_item)

        outbounds_stats = []
        _outbounds_stats = d.pop("outboundsStats")
        for outbounds_stats_item_data in _outbounds_stats:
            outbounds_stats_item = GetNodesMetricsResponseDtoResponseNodesItemOutboundsStatsItem.from_dict(
                outbounds_stats_item_data
            )

            outbounds_stats.append(outbounds_stats_item)

        get_nodes_metrics_response_dto_response_nodes_item = cls(
            node_uuid=node_uuid,
            node_name=node_name,
            country_emoji=country_emoji,
            provider_name=provider_name,
            users_online=users_online,
            inbounds_stats=inbounds_stats,
            outbounds_stats=outbounds_stats,
        )

        get_nodes_metrics_response_dto_response_nodes_item.additional_properties = d
        return get_nodes_metrics_response_dto_response_nodes_item

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
