from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetNodesUsageByRangeResponseDtoResponseItem")


@_attrs_define
class GetNodesUsageByRangeResponseDtoResponseItem:
    """
    Attributes:
        node_uuid (UUID):
        node_name (str):
        node_country_code (str):
        total (float):
        total_download (float):
        total_upload (float):
        human_readable_total (str):
        human_readable_total_download (str):
        human_readable_total_upload (str):
        date (str):
    """

    node_uuid: UUID
    node_name: str
    node_country_code: str
    total: float
    total_download: float
    total_upload: float
    human_readable_total: str
    human_readable_total_download: str
    human_readable_total_upload: str
    date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = str(self.node_uuid)

        node_name = self.node_name

        node_country_code = self.node_country_code

        total = self.total

        total_download = self.total_download

        total_upload = self.total_upload

        human_readable_total = self.human_readable_total

        human_readable_total_download = self.human_readable_total_download

        human_readable_total_upload = self.human_readable_total_upload

        date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeUuid": node_uuid,
                "nodeName": node_name,
                "nodeCountryCode": node_country_code,
                "total": total,
                "totalDownload": total_download,
                "totalUpload": total_upload,
                "humanReadableTotal": human_readable_total,
                "humanReadableTotalDownload": human_readable_total_download,
                "humanReadableTotalUpload": human_readable_total_upload,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_uuid = UUID(d.pop("nodeUuid"))

        node_name = d.pop("nodeName")

        node_country_code = d.pop("nodeCountryCode")

        total = d.pop("total")

        total_download = d.pop("totalDownload")

        total_upload = d.pop("totalUpload")

        human_readable_total = d.pop("humanReadableTotal")

        human_readable_total_download = d.pop("humanReadableTotalDownload")

        human_readable_total_upload = d.pop("humanReadableTotalUpload")

        date = d.pop("date")

        get_nodes_usage_by_range_response_dto_response_item = cls(
            node_uuid=node_uuid,
            node_name=node_name,
            node_country_code=node_country_code,
            total=total,
            total_download=total_download,
            total_upload=total_upload,
            human_readable_total=human_readable_total,
            human_readable_total_download=human_readable_total_download,
            human_readable_total_upload=human_readable_total_upload,
            date=date,
        )

        get_nodes_usage_by_range_response_dto_response_item.additional_properties = d
        return get_nodes_usage_by_range_response_dto_response_item

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
