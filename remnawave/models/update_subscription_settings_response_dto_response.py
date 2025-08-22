import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.update_subscription_settings_response_dto_response_custom_response_headers_type_0 import (
        UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0,
    )


T = TypeVar("T", bound="UpdateSubscriptionSettingsResponseDtoResponse")


@_attrs_define
class UpdateSubscriptionSettingsResponseDtoResponse:
    """
    Attributes:
        uuid (UUID):
        profile_title (str):
        support_link (str):
        profile_update_interval (int):
        is_profile_webpage_url_enabled (bool):
        serve_json_at_base_subscription (bool):
        add_username_to_base_subscription (bool):
        is_show_custom_remarks (bool):
        happ_announce (Union[None, str]):
        happ_routing (Union[None, str]):
        expired_users_remarks (list[str]):
        limited_users_remarks (list[str]):
        disabled_users_remarks (list[str]):
        custom_response_headers (Union['UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0',
            None]):
        randomize_hosts (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    uuid: UUID
    profile_title: str
    support_link: str
    profile_update_interval: int
    is_profile_webpage_url_enabled: bool
    serve_json_at_base_subscription: bool
    add_username_to_base_subscription: bool
    is_show_custom_remarks: bool
    happ_announce: Union[None, str]
    happ_routing: Union[None, str]
    expired_users_remarks: list[str]
    limited_users_remarks: list[str]
    disabled_users_remarks: list[str]
    custom_response_headers: Union["UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0", None]
    randomize_hosts: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_subscription_settings_response_dto_response_custom_response_headers_type_0 import (
            UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0,
        )

        uuid = str(self.uuid)

        profile_title = self.profile_title

        support_link = self.support_link

        profile_update_interval = self.profile_update_interval

        is_profile_webpage_url_enabled = self.is_profile_webpage_url_enabled

        serve_json_at_base_subscription = self.serve_json_at_base_subscription

        add_username_to_base_subscription = self.add_username_to_base_subscription

        is_show_custom_remarks = self.is_show_custom_remarks

        happ_announce: Union[None, str]
        happ_announce = self.happ_announce

        happ_routing: Union[None, str]
        happ_routing = self.happ_routing

        expired_users_remarks = self.expired_users_remarks

        limited_users_remarks = self.limited_users_remarks

        disabled_users_remarks = self.disabled_users_remarks

        custom_response_headers: Union[None, dict[str, Any]]
        if isinstance(
            self.custom_response_headers, UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0
        ):
            custom_response_headers = self.custom_response_headers.to_dict()
        else:
            custom_response_headers = self.custom_response_headers

        randomize_hosts = self.randomize_hosts

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "profileTitle": profile_title,
                "supportLink": support_link,
                "profileUpdateInterval": profile_update_interval,
                "isProfileWebpageUrlEnabled": is_profile_webpage_url_enabled,
                "serveJsonAtBaseSubscription": serve_json_at_base_subscription,
                "addUsernameToBaseSubscription": add_username_to_base_subscription,
                "isShowCustomRemarks": is_show_custom_remarks,
                "happAnnounce": happ_announce,
                "happRouting": happ_routing,
                "expiredUsersRemarks": expired_users_remarks,
                "limitedUsersRemarks": limited_users_remarks,
                "disabledUsersRemarks": disabled_users_remarks,
                "customResponseHeaders": custom_response_headers,
                "randomizeHosts": randomize_hosts,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscription_settings_response_dto_response_custom_response_headers_type_0 import (
            UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0,
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        profile_title = d.pop("profileTitle")

        support_link = d.pop("supportLink")

        profile_update_interval = d.pop("profileUpdateInterval")

        is_profile_webpage_url_enabled = d.pop("isProfileWebpageUrlEnabled")

        serve_json_at_base_subscription = d.pop("serveJsonAtBaseSubscription")

        add_username_to_base_subscription = d.pop("addUsernameToBaseSubscription")

        is_show_custom_remarks = d.pop("isShowCustomRemarks")

        def _parse_happ_announce(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        happ_announce = _parse_happ_announce(d.pop("happAnnounce"))

        def _parse_happ_routing(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        happ_routing = _parse_happ_routing(d.pop("happRouting"))

        expired_users_remarks = cast(list[str], d.pop("expiredUsersRemarks"))

        limited_users_remarks = cast(list[str], d.pop("limitedUsersRemarks"))

        disabled_users_remarks = cast(list[str], d.pop("disabledUsersRemarks"))

        def _parse_custom_response_headers(
            data: object,
        ) -> Union["UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_response_headers_type_0 = (
                    UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0.from_dict(data)
                )

                return custom_response_headers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateSubscriptionSettingsResponseDtoResponseCustomResponseHeadersType0", None], data)

        custom_response_headers = _parse_custom_response_headers(d.pop("customResponseHeaders"))

        randomize_hosts = d.pop("randomizeHosts")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        update_subscription_settings_response_dto_response = cls(
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
            created_at=created_at,
            updated_at=updated_at,
        )

        update_subscription_settings_response_dto_response.additional_properties = d
        return update_subscription_settings_response_dto_response

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
