from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.enable_user_response_dto_response import EnableUserResponseDtoResponse


T = TypeVar("T", bound="EnableUserResponseDto")


@_attrs_define
class EnableUserResponseDto:
    """
    Attributes:
        response (EnableUserResponseDtoResponse):
    """

    response: "EnableUserResponseDtoResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enable_user_response_dto_response import EnableUserResponseDtoResponse

        d = dict(src_dict)
        response = EnableUserResponseDtoResponse.from_dict(d.pop("response"))

        enable_user_response_dto = cls(
            response=response,
        )

        enable_user_response_dto.additional_properties = d
        return enable_user_response_dto

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
