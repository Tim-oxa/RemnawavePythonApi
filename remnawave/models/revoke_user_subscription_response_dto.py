from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.revoke_user_subscription_response_dto_response import RevokeUserSubscriptionResponseDtoResponse


T = TypeVar("T", bound="RevokeUserSubscriptionResponseDto")


@_attrs_define
class RevokeUserSubscriptionResponseDto:
    """
    Attributes:
        response (RevokeUserSubscriptionResponseDtoResponse):
    """

    response: "RevokeUserSubscriptionResponseDtoResponse"
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
        from ..models.revoke_user_subscription_response_dto_response import RevokeUserSubscriptionResponseDtoResponse

        d = dict(src_dict)
        response = RevokeUserSubscriptionResponseDtoResponse.from_dict(d.pop("response"))

        revoke_user_subscription_response_dto = cls(
            response=response,
        )

        revoke_user_subscription_response_dto.additional_properties = d
        return revoke_user_subscription_response_dto

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
