from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetNodesRealtimeUsageResponseDtoResponseItem")


@_attrs_define
class GetNodesRealtimeUsageResponseDtoResponseItem:
    """
    Attributes:
        node_uuid (UUID):
        node_name (str):
        country_code (str):
        download_bytes (float):
        upload_bytes (float):
        total_bytes (float):
        download_speed_bps (float):
        upload_speed_bps (float):
        total_speed_bps (float):
    """

    node_uuid: UUID
    node_name: str
    country_code: str
    download_bytes: float
    upload_bytes: float
    total_bytes: float
    download_speed_bps: float
    upload_speed_bps: float
    total_speed_bps: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = str(self.node_uuid)

        node_name = self.node_name

        country_code = self.country_code

        download_bytes = self.download_bytes

        upload_bytes = self.upload_bytes

        total_bytes = self.total_bytes

        download_speed_bps = self.download_speed_bps

        upload_speed_bps = self.upload_speed_bps

        total_speed_bps = self.total_speed_bps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeUuid": node_uuid,
                "nodeName": node_name,
                "countryCode": country_code,
                "downloadBytes": download_bytes,
                "uploadBytes": upload_bytes,
                "totalBytes": total_bytes,
                "downloadSpeedBps": download_speed_bps,
                "uploadSpeedBps": upload_speed_bps,
                "totalSpeedBps": total_speed_bps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_uuid = UUID(d.pop("nodeUuid"))

        node_name = d.pop("nodeName")

        country_code = d.pop("countryCode")

        download_bytes = d.pop("downloadBytes")

        upload_bytes = d.pop("uploadBytes")

        total_bytes = d.pop("totalBytes")

        download_speed_bps = d.pop("downloadSpeedBps")

        upload_speed_bps = d.pop("uploadSpeedBps")

        total_speed_bps = d.pop("totalSpeedBps")

        get_nodes_realtime_usage_response_dto_response_item = cls(
            node_uuid=node_uuid,
            node_name=node_name,
            country_code=country_code,
            download_bytes=download_bytes,
            upload_bytes=upload_bytes,
            total_bytes=total_bytes,
            download_speed_bps=download_speed_bps,
            upload_speed_bps=upload_speed_bps,
            total_speed_bps=total_speed_bps,
        )

        get_nodes_realtime_usage_response_dto_response_item.additional_properties = d
        return get_nodes_realtime_usage_response_dto_response_item

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
