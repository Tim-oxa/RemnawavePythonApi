import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_all_subscriptions_response_dto_response_subscriptions_item_user_traffic_limit_strategy import (
    GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserTrafficLimitStrategy,
)
from ..models.get_all_subscriptions_response_dto_response_subscriptions_item_user_user_status import (
    GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserUserStatus,
)

T = TypeVar("T", bound="GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser")


@_attrs_define
class GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser:
    """
    Attributes:
        short_uuid (str):
        days_left (float):
        traffic_used (str):
        traffic_limit (str):
        username (str):
        expires_at (datetime.datetime):
        is_active (bool):
        user_status (GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserUserStatus):
        traffic_limit_strategy (GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserTrafficLimitStrategy):
    """

    short_uuid: str
    days_left: float
    traffic_used: str
    traffic_limit: str
    username: str
    expires_at: datetime.datetime
    is_active: bool
    user_status: GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserUserStatus
    traffic_limit_strategy: GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserTrafficLimitStrategy
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        short_uuid = self.short_uuid

        days_left = self.days_left

        traffic_used = self.traffic_used

        traffic_limit = self.traffic_limit

        username = self.username

        expires_at = self.expires_at.isoformat()

        is_active = self.is_active

        user_status = self.user_status.value

        traffic_limit_strategy = self.traffic_limit_strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shortUuid": short_uuid,
                "daysLeft": days_left,
                "trafficUsed": traffic_used,
                "trafficLimit": traffic_limit,
                "username": username,
                "expiresAt": expires_at,
                "isActive": is_active,
                "userStatus": user_status,
                "trafficLimitStrategy": traffic_limit_strategy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        short_uuid = d.pop("shortUuid")

        days_left = d.pop("daysLeft")

        traffic_used = d.pop("trafficUsed")

        traffic_limit = d.pop("trafficLimit")

        username = d.pop("username")

        expires_at = isoparse(d.pop("expiresAt"))

        is_active = d.pop("isActive")

        user_status = GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserUserStatus(d.pop("userStatus"))

        traffic_limit_strategy = GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUserTrafficLimitStrategy(
            d.pop("trafficLimitStrategy")
        )

        get_all_subscriptions_response_dto_response_subscriptions_item_user = cls(
            short_uuid=short_uuid,
            days_left=days_left,
            traffic_used=traffic_used,
            traffic_limit=traffic_limit,
            username=username,
            expires_at=expires_at,
            is_active=is_active,
            user_status=user_status,
            traffic_limit_strategy=traffic_limit_strategy,
        )

        get_all_subscriptions_response_dto_response_subscriptions_item_user.additional_properties = d
        return get_all_subscriptions_response_dto_response_subscriptions_item_user

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
