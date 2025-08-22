from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_bandwidth_stats_response_dto_response_bandwidth_calendar_month import (
        GetBandwidthStatsResponseDtoResponseBandwidthCalendarMonth,
    )
    from ..models.get_bandwidth_stats_response_dto_response_bandwidth_current_year import (
        GetBandwidthStatsResponseDtoResponseBandwidthCurrentYear,
    )
    from ..models.get_bandwidth_stats_response_dto_response_bandwidth_last_30_days import (
        GetBandwidthStatsResponseDtoResponseBandwidthLast30Days,
    )
    from ..models.get_bandwidth_stats_response_dto_response_bandwidth_last_seven_days import (
        GetBandwidthStatsResponseDtoResponseBandwidthLastSevenDays,
    )
    from ..models.get_bandwidth_stats_response_dto_response_bandwidth_last_two_days import (
        GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays,
    )


T = TypeVar("T", bound="GetBandwidthStatsResponseDtoResponse")


@_attrs_define
class GetBandwidthStatsResponseDtoResponse:
    """
    Attributes:
        bandwidth_last_two_days (GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays):
        bandwidth_last_seven_days (GetBandwidthStatsResponseDtoResponseBandwidthLastSevenDays):
        bandwidth_last_30_days (GetBandwidthStatsResponseDtoResponseBandwidthLast30Days):
        bandwidth_calendar_month (GetBandwidthStatsResponseDtoResponseBandwidthCalendarMonth):
        bandwidth_current_year (GetBandwidthStatsResponseDtoResponseBandwidthCurrentYear):
    """

    bandwidth_last_two_days: "GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays"
    bandwidth_last_seven_days: "GetBandwidthStatsResponseDtoResponseBandwidthLastSevenDays"
    bandwidth_last_30_days: "GetBandwidthStatsResponseDtoResponseBandwidthLast30Days"
    bandwidth_calendar_month: "GetBandwidthStatsResponseDtoResponseBandwidthCalendarMonth"
    bandwidth_current_year: "GetBandwidthStatsResponseDtoResponseBandwidthCurrentYear"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bandwidth_last_two_days = self.bandwidth_last_two_days.to_dict()

        bandwidth_last_seven_days = self.bandwidth_last_seven_days.to_dict()

        bandwidth_last_30_days = self.bandwidth_last_30_days.to_dict()

        bandwidth_calendar_month = self.bandwidth_calendar_month.to_dict()

        bandwidth_current_year = self.bandwidth_current_year.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bandwidthLastTwoDays": bandwidth_last_two_days,
                "bandwidthLastSevenDays": bandwidth_last_seven_days,
                "bandwidthLast30Days": bandwidth_last_30_days,
                "bandwidthCalendarMonth": bandwidth_calendar_month,
                "bandwidthCurrentYear": bandwidth_current_year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bandwidth_stats_response_dto_response_bandwidth_calendar_month import (
            GetBandwidthStatsResponseDtoResponseBandwidthCalendarMonth,
        )
        from ..models.get_bandwidth_stats_response_dto_response_bandwidth_current_year import (
            GetBandwidthStatsResponseDtoResponseBandwidthCurrentYear,
        )
        from ..models.get_bandwidth_stats_response_dto_response_bandwidth_last_30_days import (
            GetBandwidthStatsResponseDtoResponseBandwidthLast30Days,
        )
        from ..models.get_bandwidth_stats_response_dto_response_bandwidth_last_seven_days import (
            GetBandwidthStatsResponseDtoResponseBandwidthLastSevenDays,
        )
        from ..models.get_bandwidth_stats_response_dto_response_bandwidth_last_two_days import (
            GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays,
        )

        d = dict(src_dict)
        bandwidth_last_two_days = GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays.from_dict(
            d.pop("bandwidthLastTwoDays")
        )

        bandwidth_last_seven_days = GetBandwidthStatsResponseDtoResponseBandwidthLastSevenDays.from_dict(
            d.pop("bandwidthLastSevenDays")
        )

        bandwidth_last_30_days = GetBandwidthStatsResponseDtoResponseBandwidthLast30Days.from_dict(
            d.pop("bandwidthLast30Days")
        )

        bandwidth_calendar_month = GetBandwidthStatsResponseDtoResponseBandwidthCalendarMonth.from_dict(
            d.pop("bandwidthCalendarMonth")
        )

        bandwidth_current_year = GetBandwidthStatsResponseDtoResponseBandwidthCurrentYear.from_dict(
            d.pop("bandwidthCurrentYear")
        )

        get_bandwidth_stats_response_dto_response = cls(
            bandwidth_last_two_days=bandwidth_last_two_days,
            bandwidth_last_seven_days=bandwidth_last_seven_days,
            bandwidth_last_30_days=bandwidth_last_30_days,
            bandwidth_calendar_month=bandwidth_calendar_month,
            bandwidth_current_year=bandwidth_current_year,
        )

        get_bandwidth_stats_response_dto_response.additional_properties = d
        return get_bandwidth_stats_response_dto_response

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
