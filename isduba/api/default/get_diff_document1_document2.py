# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_diff_document_1_document_2_response_200 import GetDiffDocument1Document2Response200
from ...models.models_error import ModelsError
from ...types import Response


def _get_kwargs(
    document1: str,
    document2: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/diff/{document1}/{document2}",
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]:
    if response.status_code == 200:
        response_200 = GetDiffDocument1Document2Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ModelsError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = ModelsError.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ModelsError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    document1: str,
    document2: str,
    *,
    client: Client,
) -> Response[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]:
    """Returns a diff.

     Returns a diff between two documents.

    Args:
        document1 (str):
        document2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]
    """

    kwargs = _get_kwargs(
        document1=document1,
        document2=document2,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    document1: str,
    document2: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]:
    """Returns a diff.

     Returns a diff between two documents.

    Args:
        document1 (str):
        document2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDiffDocument1Document2Response200, ModelsError]
    """

    return sync_detailed(
        document1=document1,
        document2=document2,
        client=client,
    ).parsed


async def asyncio_detailed(
    document1: str,
    document2: str,
    *,
    client: Client,
) -> Response[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]:
    """Returns a diff.

     Returns a diff between two documents.

    Args:
        document1 (str):
        document2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]
    """

    kwargs = _get_kwargs(
        document1=document1,
        document2=document2,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    document1: str,
    document2: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetDiffDocument1Document2Response200, ModelsError]]:
    """Returns a diff.

     Returns a diff between two documents.

    Args:
        document1 (str):
        document2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDiffDocument1Document2Response200, ModelsError]
    """

    return (
        await asyncio_detailed(
            document1=document1,
            document2=document2,
            client=client,
        )
    ).parsed
