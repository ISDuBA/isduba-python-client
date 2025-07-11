# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.models_error import ModelsError
from ...models.web_overview_events_events import WebOverviewEventsEvents
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ModelsError, WebOverviewEventsEvents]]:
    if response.status_code == 200:
        response_200 = WebOverviewEventsEvents.from_dict(response.json())

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
) -> Response[Union[Any, ModelsError, WebOverviewEventsEvents]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ModelsError, WebOverviewEventsEvents]]:
    """Returns a list of events.

     Returns all events that match the specified query.

    Args:
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, WebOverviewEventsEvents]]
    """

    kwargs = _get_kwargs(
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ModelsError, WebOverviewEventsEvents]]:
    """Returns a list of events.

     Returns all events that match the specified query.

    Args:
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, WebOverviewEventsEvents]
    """

    return sync_detailed(
        client=client,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ModelsError, WebOverviewEventsEvents]]:
    """Returns a list of events.

     Returns all events that match the specified query.

    Args:
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, WebOverviewEventsEvents]]
    """

    kwargs = _get_kwargs(
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ModelsError, WebOverviewEventsEvents]]:
    """Returns a list of events.

     Returns all events that match the specified query.

    Args:
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, WebOverviewEventsEvents]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
        )
    ).parsed
