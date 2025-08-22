from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetUserByTelegramIdResponseDtoResponseItemActiveInternalSquadsItem")


@_attrs_define
class GetUserByTelegramIdResponseDtoResponseItemActiveInternalSquadsItem:
    """
    Attributes:
        uuid (UUID):
        name (str):
    """

    uuid: UUID
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        get_user_by_telegram_id_response_dto_response_item_active_internal_squads_item = cls(
            uuid=uuid,
            name=name,
        )

        get_user_by_telegram_id_response_dto_response_item_active_internal_squads_item.additional_properties = d
        return get_user_by_telegram_id_response_dto_response_item_active_internal_squads_item

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
