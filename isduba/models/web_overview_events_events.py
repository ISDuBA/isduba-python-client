# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.web_overview_events_events_events_item import WebOverviewEventsEventsEventsItem


T = TypeVar("T", bound="WebOverviewEventsEvents")


@_attrs_define
class WebOverviewEventsEvents:
    """
    Attributes:
        count (Union[Unset, int]):
        events (Union[Unset, list['WebOverviewEventsEventsEventsItem']]):
    """

    count: Union[Unset, int] = UNSET
    events: Union[Unset, list["WebOverviewEventsEventsEventsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_overview_events_events_events_item import WebOverviewEventsEventsEventsItem

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebOverviewEventsEventsEventsItem.from_dict(events_item_data)

            events.append(events_item)

        web_overview_events_events = cls(
            count=count,
            events=events,
        )

        web_overview_events_events.additional_properties = d
        return web_overview_events_events

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
