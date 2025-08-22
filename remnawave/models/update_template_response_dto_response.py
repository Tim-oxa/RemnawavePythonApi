from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_template_response_dto_response_template_type import UpdateTemplateResponseDtoResponseTemplateType

T = TypeVar("T", bound="UpdateTemplateResponseDtoResponse")


@_attrs_define
class UpdateTemplateResponseDtoResponse:
    """
    Attributes:
        uuid (UUID):
        template_type (UpdateTemplateResponseDtoResponseTemplateType):
        template_json (Any):
        encoded_template_yaml (Union[None, str]):
    """

    uuid: UUID
    template_type: UpdateTemplateResponseDtoResponseTemplateType
    template_json: Any
    encoded_template_yaml: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        template_type = self.template_type.value

        template_json = self.template_json

        encoded_template_yaml: Union[None, str]
        encoded_template_yaml = self.encoded_template_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "templateType": template_type,
                "templateJson": template_json,
                "encodedTemplateYaml": encoded_template_yaml,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        template_type = UpdateTemplateResponseDtoResponseTemplateType(d.pop("templateType"))

        template_json = d.pop("templateJson")

        def _parse_encoded_template_yaml(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        encoded_template_yaml = _parse_encoded_template_yaml(d.pop("encodedTemplateYaml"))

        update_template_response_dto_response = cls(
            uuid=uuid,
            template_type=template_type,
            template_json=template_json,
            encoded_template_yaml=encoded_template_yaml,
        )

        update_template_response_dto_response.additional_properties = d
        return update_template_response_dto_response

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
