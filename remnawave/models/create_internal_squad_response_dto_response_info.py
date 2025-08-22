from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateInternalSquadResponseDtoResponseInfo")


@_attrs_define
class CreateInternalSquadResponseDtoResponseInfo:
    """
    Attributes:
        members_count (float):
        inbounds_count (float):
    """

    members_count: float
    inbounds_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members_count = self.members_count

        inbounds_count = self.inbounds_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "membersCount": members_count,
                "inboundsCount": inbounds_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        members_count = d.pop("membersCount")

        inbounds_count = d.pop("inboundsCount")

        create_internal_squad_response_dto_response_info = cls(
            members_count=members_count,
            inbounds_count=inbounds_count,
        )

        create_internal_squad_response_dto_response_info.additional_properties = d
        return create_internal_squad_response_dto_response_info

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
