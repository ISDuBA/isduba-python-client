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
    from ..models.tempstore_entry import TempstoreEntry


T = TypeVar("T", bound="WebOverviewTempDocumentsTempDocuments")


@_attrs_define
class WebOverviewTempDocumentsTempDocuments:
    """
    Attributes:
        files (Union[Unset, list['TempstoreEntry']]):
        free (Union[Unset, int]):
    """

    files: Union[Unset, list["TempstoreEntry"]] = UNSET
    free: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        free = self.free

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if free is not UNSET:
            field_dict["free"] = free

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tempstore_entry import TempstoreEntry

        d = dict(src_dict)
        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = TempstoreEntry.from_dict(files_item_data)

            files.append(files_item)

        free = d.pop("free", UNSET)

        web_overview_temp_documents_temp_documents = cls(
            files=files,
            free=free,
        )

        web_overview_temp_documents_temp_documents.additional_properties = d
        return web_overview_temp_documents_temp_documents

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
