from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateInternalSquadRequestDto")


@_attrs_define
class UpdateInternalSquadRequestDto:
    """
    Attributes:
        uuid (UUID):
        name (Union[Unset, str]):
        inbounds (Union[Unset, list[UUID]]):
    """

    uuid: UUID
    name: Union[Unset, str] = UNSET
    inbounds: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        inbounds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inbounds, Unset):
            inbounds = []
            for inbounds_item_data in self.inbounds:
                inbounds_item = str(inbounds_item_data)
                inbounds.append(inbounds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if inbounds is not UNSET:
            field_dict["inbounds"] = inbounds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name", UNSET)

        inbounds = []
        _inbounds = d.pop("inbounds", UNSET)
        for inbounds_item_data in _inbounds or []:
            inbounds_item = UUID(inbounds_item_data)

            inbounds.append(inbounds_item)

        update_internal_squad_request_dto = cls(
            uuid=uuid,
            name=name,
            inbounds=inbounds,
        )

        update_internal_squad_request_dto.additional_properties = d
        return update_internal_squad_request_dto

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
