from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_stats_response_dto_response_cpu import GetStatsResponseDtoResponseCpu
    from ..models.get_stats_response_dto_response_memory import GetStatsResponseDtoResponseMemory
    from ..models.get_stats_response_dto_response_nodes import GetStatsResponseDtoResponseNodes
    from ..models.get_stats_response_dto_response_online_stats import GetStatsResponseDtoResponseOnlineStats
    from ..models.get_stats_response_dto_response_users import GetStatsResponseDtoResponseUsers


T = TypeVar("T", bound="GetStatsResponseDtoResponse")


@_attrs_define
class GetStatsResponseDtoResponse:
    """
    Attributes:
        cpu (GetStatsResponseDtoResponseCpu):
        memory (GetStatsResponseDtoResponseMemory):
        uptime (float):
        timestamp (float):
        users (GetStatsResponseDtoResponseUsers):
        online_stats (GetStatsResponseDtoResponseOnlineStats):
        nodes (GetStatsResponseDtoResponseNodes):
    """

    cpu: "GetStatsResponseDtoResponseCpu"
    memory: "GetStatsResponseDtoResponseMemory"
    uptime: float
    timestamp: float
    users: "GetStatsResponseDtoResponseUsers"
    online_stats: "GetStatsResponseDtoResponseOnlineStats"
    nodes: "GetStatsResponseDtoResponseNodes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        uptime = self.uptime

        timestamp = self.timestamp

        users = self.users.to_dict()

        online_stats = self.online_stats.to_dict()

        nodes = self.nodes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu": cpu,
                "memory": memory,
                "uptime": uptime,
                "timestamp": timestamp,
                "users": users,
                "onlineStats": online_stats,
                "nodes": nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_stats_response_dto_response_cpu import GetStatsResponseDtoResponseCpu
        from ..models.get_stats_response_dto_response_memory import GetStatsResponseDtoResponseMemory
        from ..models.get_stats_response_dto_response_nodes import GetStatsResponseDtoResponseNodes
        from ..models.get_stats_response_dto_response_online_stats import GetStatsResponseDtoResponseOnlineStats
        from ..models.get_stats_response_dto_response_users import GetStatsResponseDtoResponseUsers

        d = dict(src_dict)
        cpu = GetStatsResponseDtoResponseCpu.from_dict(d.pop("cpu"))

        memory = GetStatsResponseDtoResponseMemory.from_dict(d.pop("memory"))

        uptime = d.pop("uptime")

        timestamp = d.pop("timestamp")

        users = GetStatsResponseDtoResponseUsers.from_dict(d.pop("users"))

        online_stats = GetStatsResponseDtoResponseOnlineStats.from_dict(d.pop("onlineStats"))

        nodes = GetStatsResponseDtoResponseNodes.from_dict(d.pop("nodes"))

        get_stats_response_dto_response = cls(
            cpu=cpu,
            memory=memory,
            uptime=uptime,
            timestamp=timestamp,
            users=users,
            online_stats=online_stats,
            nodes=nodes,
        )

        get_stats_response_dto_response.additional_properties = d
        return get_stats_response_dto_response

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
