from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_all_subscriptions_response_dto_response_subscriptions_item_ss_conf_links import (
        GetAllSubscriptionsResponseDtoResponseSubscriptionsItemSsConfLinks,
    )
    from ..models.get_all_subscriptions_response_dto_response_subscriptions_item_user import (
        GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser,
    )


T = TypeVar("T", bound="GetAllSubscriptionsResponseDtoResponseSubscriptionsItem")


@_attrs_define
class GetAllSubscriptionsResponseDtoResponseSubscriptionsItem:
    """
    Attributes:
        is_found (bool):
        user (GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser):
        links (list[str]):
        ss_conf_links (GetAllSubscriptionsResponseDtoResponseSubscriptionsItemSsConfLinks):
        subscription_url (str):
    """

    is_found: bool
    user: "GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser"
    links: list[str]
    ss_conf_links: "GetAllSubscriptionsResponseDtoResponseSubscriptionsItemSsConfLinks"
    subscription_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_found = self.is_found

        user = self.user.to_dict()

        links = self.links

        ss_conf_links = self.ss_conf_links.to_dict()

        subscription_url = self.subscription_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isFound": is_found,
                "user": user,
                "links": links,
                "ssConfLinks": ss_conf_links,
                "subscriptionUrl": subscription_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_subscriptions_response_dto_response_subscriptions_item_ss_conf_links import (
            GetAllSubscriptionsResponseDtoResponseSubscriptionsItemSsConfLinks,
        )
        from ..models.get_all_subscriptions_response_dto_response_subscriptions_item_user import (
            GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser,
        )

        d = dict(src_dict)
        is_found = d.pop("isFound")

        user = GetAllSubscriptionsResponseDtoResponseSubscriptionsItemUser.from_dict(d.pop("user"))

        links = cast(list[str], d.pop("links"))

        ss_conf_links = GetAllSubscriptionsResponseDtoResponseSubscriptionsItemSsConfLinks.from_dict(
            d.pop("ssConfLinks")
        )

        subscription_url = d.pop("subscriptionUrl")

        get_all_subscriptions_response_dto_response_subscriptions_item = cls(
            is_found=is_found,
            user=user,
            links=links,
            ss_conf_links=ss_conf_links,
            subscription_url=subscription_url,
        )

        get_all_subscriptions_response_dto_response_subscriptions_item.additional_properties = d
        return get_all_subscriptions_response_dto_response_subscriptions_item

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
