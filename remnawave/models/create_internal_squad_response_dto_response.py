import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.create_internal_squad_response_dto_response_inbounds_item import (
        CreateInternalSquadResponseDtoResponseInboundsItem,
    )
    from ..models.create_internal_squad_response_dto_response_info import CreateInternalSquadResponseDtoResponseInfo


T = TypeVar("T", bound="CreateInternalSquadResponseDtoResponse")


@_attrs_define
class CreateInternalSquadResponseDtoResponse:
    """
    Attributes:
        uuid (UUID):
        name (str):
        info (CreateInternalSquadResponseDtoResponseInfo):
        inbounds (list['CreateInternalSquadResponseDtoResponseInboundsItem']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    name: str
    info: "CreateInternalSquadResponseDtoResponseInfo"
    inbounds: list["CreateInternalSquadResponseDtoResponseInboundsItem"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        info = self.info.to_dict()

        inbounds = []
        for inbounds_item_data in self.inbounds:
            inbounds_item = inbounds_item_data.to_dict()
            inbounds.append(inbounds_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "info": info,
                "inbounds": inbounds,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_internal_squad_response_dto_response_inbounds_item import (
            CreateInternalSquadResponseDtoResponseInboundsItem,
        )
        from ..models.create_internal_squad_response_dto_response_info import CreateInternalSquadResponseDtoResponseInfo

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        info = CreateInternalSquadResponseDtoResponseInfo.from_dict(d.pop("info"))

        inbounds = []
        _inbounds = d.pop("inbounds")
        for inbounds_item_data in _inbounds:
            inbounds_item = CreateInternalSquadResponseDtoResponseInboundsItem.from_dict(inbounds_item_data)

            inbounds.append(inbounds_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        create_internal_squad_response_dto_response = cls(
            uuid=uuid,
            name=name,
            info=info,
            inbounds=inbounds,
            created_at=created_at,
            updated_at=updated_at,
        )

        create_internal_squad_response_dto_response.additional_properties = d
        return create_internal_squad_response_dto_response

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
