from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetUserUsageByRangeResponseDtoResponseItem")


@_attrs_define
class GetUserUsageByRangeResponseDtoResponseItem:
    """
    Attributes:
        user_uuid (UUID):
        node_uuid (UUID):
        node_name (str):
        country_code (str):
        total (float):
        date (str):
    """

    user_uuid: UUID
    node_uuid: UUID
    node_name: str
    country_code: str
    total: float
    date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_uuid = str(self.user_uuid)

        node_uuid = str(self.node_uuid)

        node_name = self.node_name

        country_code = self.country_code

        total = self.total

        date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "nodeUuid": node_uuid,
                "nodeName": node_name,
                "countryCode": country_code,
                "total": total,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_uuid = UUID(d.pop("userUuid"))

        node_uuid = UUID(d.pop("nodeUuid"))

        node_name = d.pop("nodeName")

        country_code = d.pop("countryCode")

        total = d.pop("total")

        date = d.pop("date")

        get_user_usage_by_range_response_dto_response_item = cls(
            user_uuid=user_uuid,
            node_uuid=node_uuid,
            node_name=node_name,
            country_code=country_code,
            total=total,
            date=date,
        )

        get_user_usage_by_range_response_dto_response_item.additional_properties = d
        return get_user_usage_by_range_response_dto_response_item

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
