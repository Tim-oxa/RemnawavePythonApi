from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_all_inbounds_response_dto_response_inbounds_item import (
        GetAllInboundsResponseDtoResponseInboundsItem,
    )


T = TypeVar("T", bound="GetAllInboundsResponseDtoResponse")


@_attrs_define
class GetAllInboundsResponseDtoResponse:
    """
    Attributes:
        total (float):
        inbounds (list['GetAllInboundsResponseDtoResponseInboundsItem']):
    """

    total: float
    inbounds: list["GetAllInboundsResponseDtoResponseInboundsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        inbounds = []
        for inbounds_item_data in self.inbounds:
            inbounds_item = inbounds_item_data.to_dict()
            inbounds.append(inbounds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "inbounds": inbounds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_inbounds_response_dto_response_inbounds_item import (
            GetAllInboundsResponseDtoResponseInboundsItem,
        )

        d = dict(src_dict)
        total = d.pop("total")

        inbounds = []
        _inbounds = d.pop("inbounds")
        for inbounds_item_data in _inbounds:
            inbounds_item = GetAllInboundsResponseDtoResponseInboundsItem.from_dict(inbounds_item_data)

            inbounds.append(inbounds_item)

        get_all_inbounds_response_dto_response = cls(
            total=total,
            inbounds=inbounds,
        )

        get_all_inbounds_response_dto_response.additional_properties = d
        return get_all_inbounds_response_dto_response

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
