import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionsControllerGetSubscriptionByUsernameResponse404")


@_attrs_define
class SubscriptionsControllerGetSubscriptionByUsernameResponse404:
    """
    Attributes:
        timestamp (Union[Unset, datetime.datetime]):
        path (Union[Unset, str]):
        message (Union[Unset, str]):
        error_code (Union[Unset, str]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    path: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    error_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        path = self.path

        message = self.message

        error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if path is not UNSET:
            field_dict["path"] = path
        if message is not UNSET:
            field_dict["message"] = message
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        path = d.pop("path", UNSET)

        message = d.pop("message", UNSET)

        error_code = d.pop("errorCode", UNSET)

        subscriptions_controller_get_subscription_by_username_response_404 = cls(
            timestamp=timestamp,
            path=path,
            message=message,
            error_code=error_code,
        )

        subscriptions_controller_get_subscription_by_username_response_404.additional_properties = d
        return subscriptions_controller_get_subscription_by_username_response_404

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
