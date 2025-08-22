from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_internal_squads_response_dto_response_internal_squads_item import (
        GetInternalSquadsResponseDtoResponseInternalSquadsItem,
    )


T = TypeVar("T", bound="GetInternalSquadsResponseDtoResponse")


@_attrs_define
class GetInternalSquadsResponseDtoResponse:
    """
    Attributes:
        total (float):
        internal_squads (list['GetInternalSquadsResponseDtoResponseInternalSquadsItem']):
    """

    total: float
    internal_squads: list["GetInternalSquadsResponseDtoResponseInternalSquadsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        internal_squads = []
        for internal_squads_item_data in self.internal_squads:
            internal_squads_item = internal_squads_item_data.to_dict()
            internal_squads.append(internal_squads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "internalSquads": internal_squads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_internal_squads_response_dto_response_internal_squads_item import (
            GetInternalSquadsResponseDtoResponseInternalSquadsItem,
        )

        d = dict(src_dict)
        total = d.pop("total")

        internal_squads = []
        _internal_squads = d.pop("internalSquads")
        for internal_squads_item_data in _internal_squads:
            internal_squads_item = GetInternalSquadsResponseDtoResponseInternalSquadsItem.from_dict(
                internal_squads_item_data
            )

            internal_squads.append(internal_squads_item)

        get_internal_squads_response_dto_response = cls(
            total=total,
            internal_squads=internal_squads,
        )

        get_internal_squads_response_dto_response.additional_properties = d
        return get_internal_squads_response_dto_response

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
