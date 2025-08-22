from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_status_response_dto_response_oauth_2 import GetStatusResponseDtoResponseOauth2
    from ..models.get_status_response_dto_response_tg_auth_type_0 import GetStatusResponseDtoResponseTgAuthType0


T = TypeVar("T", bound="GetStatusResponseDtoResponse")


@_attrs_define
class GetStatusResponseDtoResponse:
    """
    Attributes:
        is_login_allowed (bool):
        is_register_allowed (bool):
        tg_auth (Union['GetStatusResponseDtoResponseTgAuthType0', None]):
        oauth2 (GetStatusResponseDtoResponseOauth2):
    """

    is_login_allowed: bool
    is_register_allowed: bool
    tg_auth: Union["GetStatusResponseDtoResponseTgAuthType0", None]
    oauth2: "GetStatusResponseDtoResponseOauth2"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_status_response_dto_response_tg_auth_type_0 import GetStatusResponseDtoResponseTgAuthType0

        is_login_allowed = self.is_login_allowed

        is_register_allowed = self.is_register_allowed

        tg_auth: Union[None, dict[str, Any]]
        if isinstance(self.tg_auth, GetStatusResponseDtoResponseTgAuthType0):
            tg_auth = self.tg_auth.to_dict()
        else:
            tg_auth = self.tg_auth

        oauth2 = self.oauth2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isLoginAllowed": is_login_allowed,
                "isRegisterAllowed": is_register_allowed,
                "tgAuth": tg_auth,
                "oauth2": oauth2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_status_response_dto_response_oauth_2 import GetStatusResponseDtoResponseOauth2
        from ..models.get_status_response_dto_response_tg_auth_type_0 import GetStatusResponseDtoResponseTgAuthType0

        d = dict(src_dict)
        is_login_allowed = d.pop("isLoginAllowed")

        is_register_allowed = d.pop("isRegisterAllowed")

        def _parse_tg_auth(data: object) -> Union["GetStatusResponseDtoResponseTgAuthType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tg_auth_type_0 = GetStatusResponseDtoResponseTgAuthType0.from_dict(data)

                return tg_auth_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetStatusResponseDtoResponseTgAuthType0", None], data)

        tg_auth = _parse_tg_auth(d.pop("tgAuth"))

        oauth2 = GetStatusResponseDtoResponseOauth2.from_dict(d.pop("oauth2"))

        get_status_response_dto_response = cls(
            is_login_allowed=is_login_allowed,
            is_register_allowed=is_register_allowed,
            tg_auth=tg_auth,
            oauth2=oauth2,
        )

        get_status_response_dto_response.additional_properties = d
        return get_status_response_dto_response

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
