from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteInfraBillingHistoryRecordByUuidResponseDtoResponseRecordsItemProvider")


@_attrs_define
class DeleteInfraBillingHistoryRecordByUuidResponseDtoResponseRecordsItemProvider:
    """
    Attributes:
        uuid (UUID):
        name (str):
        favicon_link (Union[None, str]):
    """

    uuid: UUID
    name: str
    favicon_link: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        favicon_link: Union[None, str]
        favicon_link = self.favicon_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "faviconLink": favicon_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        def _parse_favicon_link(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        favicon_link = _parse_favicon_link(d.pop("faviconLink"))

        delete_infra_billing_history_record_by_uuid_response_dto_response_records_item_provider = cls(
            uuid=uuid,
            name=name,
            favicon_link=favicon_link,
        )

        delete_infra_billing_history_record_by_uuid_response_dto_response_records_item_provider.additional_properties = d
        return delete_infra_billing_history_record_by_uuid_response_dto_response_records_item_provider

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
