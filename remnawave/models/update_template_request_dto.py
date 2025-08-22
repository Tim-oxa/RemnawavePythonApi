from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_template_request_dto_template_type import UpdateTemplateRequestDtoTemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_template_request_dto_template_json import UpdateTemplateRequestDtoTemplateJson


T = TypeVar("T", bound="UpdateTemplateRequestDto")


@_attrs_define
class UpdateTemplateRequestDto:
    """
    Attributes:
        template_type (UpdateTemplateRequestDtoTemplateType):
        template_json (Union[Unset, UpdateTemplateRequestDtoTemplateJson]):
        encoded_template_yaml (Union[Unset, str]):
    """

    template_type: UpdateTemplateRequestDtoTemplateType
    template_json: Union[Unset, "UpdateTemplateRequestDtoTemplateJson"] = UNSET
    encoded_template_yaml: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_type = self.template_type.value

        template_json: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_json, Unset):
            template_json = self.template_json.to_dict()

        encoded_template_yaml = self.encoded_template_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateType": template_type,
            }
        )
        if template_json is not UNSET:
            field_dict["templateJson"] = template_json
        if encoded_template_yaml is not UNSET:
            field_dict["encodedTemplateYaml"] = encoded_template_yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_template_request_dto_template_json import UpdateTemplateRequestDtoTemplateJson

        d = dict(src_dict)
        template_type = UpdateTemplateRequestDtoTemplateType(d.pop("templateType"))

        _template_json = d.pop("templateJson", UNSET)
        template_json: Union[Unset, UpdateTemplateRequestDtoTemplateJson]
        if isinstance(_template_json, Unset):
            template_json = UNSET
        else:
            template_json = UpdateTemplateRequestDtoTemplateJson.from_dict(_template_json)

        encoded_template_yaml = d.pop("encodedTemplateYaml", UNSET)

        update_template_request_dto = cls(
            template_type=template_type,
            template_json=template_json,
            encoded_template_yaml=encoded_template_yaml,
        )

        update_template_request_dto.additional_properties = d
        return update_template_request_dto

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
