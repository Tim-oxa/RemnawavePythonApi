from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_subscriptions_response_dto import GetAllSubscriptionsResponseDto
from ...models.subscriptions_controller_get_all_subscriptions_response_500 import (
    SubscriptionsControllerGetAllSubscriptionsResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    size: Union[Unset, float] = UNSET,
    start: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["size"] = size

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]:
    if response.status_code == 200:
        response_200 = GetAllSubscriptionsResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = SubscriptionsControllerGetAllSubscriptionsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, float] = UNSET,
    start: Union[Unset, float] = UNSET,
) -> Response[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]:
    """Get all subscriptions

    Args:
        size (Union[Unset, float]):  Example: 25.
        start (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]
    """

    kwargs = _get_kwargs(
        size=size,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, float] = UNSET,
    start: Union[Unset, float] = UNSET,
) -> Optional[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]:
    """Get all subscriptions

    Args:
        size (Union[Unset, float]):  Example: 25.
        start (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]
    """

    return sync_detailed(
        client=client,
        size=size,
        start=start,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, float] = UNSET,
    start: Union[Unset, float] = UNSET,
) -> Response[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]:
    """Get all subscriptions

    Args:
        size (Union[Unset, float]):  Example: 25.
        start (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]
    """

    kwargs = _get_kwargs(
        size=size,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, float] = UNSET,
    start: Union[Unset, float] = UNSET,
) -> Optional[Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]]:
    """Get all subscriptions

    Args:
        size (Union[Unset, float]):  Example: 25.
        start (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetAllSubscriptionsResponseDto, SubscriptionsControllerGetAllSubscriptionsResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            size=size,
            start=start,
        )
    ).parsed
