from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscription_settings_request_dto_custom_response_headers import (
        UpdateSubscriptionSettingsRequestDtoCustomResponseHeaders,
    )


T = TypeVar("T", bound="UpdateSubscriptionSettingsRequestDto")


@_attrs_define
class UpdateSubscriptionSettingsRequestDto:
    """
    Attributes:
        uuid (UUID):
        profile_title (Union[Unset, str]):
        support_link (Union[Unset, str]):
        profile_update_interval (Union[Unset, int]):
        is_profile_webpage_url_enabled (Union[Unset, bool]):
        serve_json_at_base_subscription (Union[Unset, bool]):
        add_username_to_base_subscription (Union[Unset, bool]):
        is_show_custom_remarks (Union[Unset, bool]):
        happ_announce (Union[None, Unset, str]):
        happ_routing (Union[None, Unset, str]):
        expired_users_remarks (Union[Unset, list[str]]):
        limited_users_remarks (Union[Unset, list[str]]):
        disabled_users_remarks (Union[Unset, list[str]]):
        custom_response_headers (Union[Unset, UpdateSubscriptionSettingsRequestDtoCustomResponseHeaders]):
        randomize_hosts (Union[Unset, bool]):
    """

    uuid: UUID
    profile_title: Union[Unset, str] = UNSET
    support_link: Union[Unset, str] = UNSET
    profile_update_interval: Union[Unset, int] = UNSET
    is_profile_webpage_url_enabled: Union[Unset, bool] = UNSET
    serve_json_at_base_subscription: Union[Unset, bool] = UNSET
    add_username_to_base_subscription: Union[Unset, bool] = UNSET
    is_show_custom_remarks: Union[Unset, bool] = UNSET
    happ_announce: Union[None, Unset, str] = UNSET
    happ_routing: Union[None, Unset, str] = UNSET
    expired_users_remarks: Union[Unset, list[str]] = UNSET
    limited_users_remarks: Union[Unset, list[str]] = UNSET
    disabled_users_remarks: Union[Unset, list[str]] = UNSET
    custom_response_headers: Union[Unset, "UpdateSubscriptionSettingsRequestDtoCustomResponseHeaders"] = UNSET
    randomize_hosts: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        profile_title = self.profile_title

        support_link = self.support_link

        profile_update_interval = self.profile_update_interval

        is_profile_webpage_url_enabled = self.is_profile_webpage_url_enabled

        serve_json_at_base_subscription = self.serve_json_at_base_subscription

        add_username_to_base_subscription = self.add_username_to_base_subscription

        is_show_custom_remarks = self.is_show_custom_remarks

        happ_announce: Union[None, Unset, str]
        if isinstance(self.happ_announce, Unset):
            happ_announce = UNSET
        else:
            happ_announce = self.happ_announce

        happ_routing: Union[None, Unset, str]
        if isinstance(self.happ_routing, Unset):
            happ_routing = UNSET
        else:
            happ_routing = self.happ_routing

        expired_users_remarks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.expired_users_remarks, Unset):
            expired_users_remarks = self.expired_users_remarks

        limited_users_remarks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.limited_users_remarks, Unset):
            limited_users_remarks = self.limited_users_remarks

        disabled_users_remarks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.disabled_users_remarks, Unset):
            disabled_users_remarks = self.disabled_users_remarks

        custom_response_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_response_headers, Unset):
            custom_response_headers = self.custom_response_headers.to_dict()

        randomize_hosts = self.randomize_hosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if profile_title is not UNSET:
            field_dict["profileTitle"] = profile_title
        if support_link is not UNSET:
            field_dict["supportLink"] = support_link
        if profile_update_interval is not UNSET:
            field_dict["profileUpdateInterval"] = profile_update_interval
        if is_profile_webpage_url_enabled is not UNSET:
            field_dict["isProfileWebpageUrlEnabled"] = is_profile_webpage_url_enabled
        if serve_json_at_base_subscription is not UNSET:
            field_dict["serveJsonAtBaseSubscription"] = serve_json_at_base_subscription
        if add_username_to_base_subscription is not UNSET:
            field_dict["addUsernameToBaseSubscription"] = add_username_to_base_subscription
        if is_show_custom_remarks is not UNSET:
            field_dict["isShowCustomRemarks"] = is_show_custom_remarks
        if happ_announce is not UNSET:
            field_dict["happAnnounce"] = happ_announce
        if happ_routing is not UNSET:
            field_dict["happRouting"] = happ_routing
        if expired_users_remarks is not UNSET:
            field_dict["expiredUsersRemarks"] = expired_users_remarks
        if limited_users_remarks is not UNSET:
            field_dict["limitedUsersRemarks"] = limited_users_remarks
        if disabled_users_remarks is not UNSET:
            field_dict["disabledUsersRemarks"] = disabled_users_remarks
        if custom_response_headers is not UNSET:
            field_dict["customResponseHeaders"] = custom_response_headers
        if randomize_hosts is not UNSET:
            field_dict["randomizeHosts"] = randomize_hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscription_settings_request_dto_custom_response_headers import (
            UpdateSubscriptionSettingsRequestDtoCustomResponseHeaders,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        profile_title = d.pop("profileTitle", UNSET)

        support_link = d.pop("supportLink", UNSET)

        profile_update_interval = d.pop("profileUpdateInterval", UNSET)

        is_profile_webpage_url_enabled = d.pop("isProfileWebpageUrlEnabled", UNSET)

        serve_json_at_base_subscription = d.pop("serveJsonAtBaseSubscription", UNSET)

        add_username_to_base_subscription = d.pop("addUsernameToBaseSubscription", UNSET)

        is_show_custom_remarks = d.pop("isShowCustomRemarks", UNSET)

        def _parse_happ_announce(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        happ_announce = _parse_happ_announce(d.pop("happAnnounce", UNSET))

        def _parse_happ_routing(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        happ_routing = _parse_happ_routing(d.pop("happRouting", UNSET))

        expired_users_remarks = cast(list[str], d.pop("expiredUsersRemarks", UNSET))

        limited_users_remarks = cast(list[str], d.pop("limitedUsersRemarks", UNSET))

        disabled_users_remarks = cast(list[str], d.pop("disabledUsersRemarks", UNSET))

        _custom_response_headers = d.pop("customResponseHeaders", UNSET)
        custom_response_headers: Union[Unset, UpdateSubscriptionSettingsRequestDtoCustomResponseHeaders]
        if isinstance(_custom_response_headers, Unset):
            custom_response_headers = UNSET
        else:
            custom_response_headers = UpdateSubscriptionSettingsRequestDtoCustomResponseHeaders.from_dict(
                _custom_response_headers
            )

        randomize_hosts = d.pop("randomizeHosts", UNSET)

        update_subscription_settings_request_dto = cls(
            uuid=uuid,
            profile_title=profile_title,
            support_link=support_link,
            profile_update_interval=profile_update_interval,
            is_profile_webpage_url_enabled=is_profile_webpage_url_enabled,
            serve_json_at_base_subscription=serve_json_at_base_subscription,
            add_username_to_base_subscription=add_username_to_base_subscription,
            is_show_custom_remarks=is_show_custom_remarks,
            happ_announce=happ_announce,
            happ_routing=happ_routing,
            expired_users_remarks=expired_users_remarks,
            limited_users_remarks=limited_users_remarks,
            disabled_users_remarks=disabled_users_remarks,
            custom_response_headers=custom_response_headers,
            randomize_hosts=randomize_hosts,
        )

        update_subscription_settings_request_dto.additional_properties = d
        return update_subscription_settings_request_dto

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
