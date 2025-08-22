from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_raw_subscription_by_short_uuid_response_dto import GetRawSubscriptionByShortUuidResponseDto
from ...models.subscription_controller_get_raw_subscription_by_short_uuid_response_500 import (
    SubscriptionControllerGetRawSubscriptionByShortUuidResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    short_uuid: str,
    *,
    with_disabled_hosts: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["withDisabledHosts"] = with_disabled_hosts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/sub/{short_uuid}/raw",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
]:
    if response.status_code == 200:
        response_200 = GetRawSubscriptionByShortUuidResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = SubscriptionControllerGetRawSubscriptionByShortUuidResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    short_uuid: str,
    *,
    client: AuthenticatedClient,
    with_disabled_hosts: Union[Unset, bool] = UNSET,
) -> Response[
    Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
]:
    """Get Raw Subscription by Short UUID

    Args:
        short_uuid (str):
        with_disabled_hosts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]]
    """

    kwargs = _get_kwargs(
        short_uuid=short_uuid,
        with_disabled_hosts=with_disabled_hosts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    short_uuid: str,
    *,
    client: AuthenticatedClient,
    with_disabled_hosts: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
]:
    """Get Raw Subscription by Short UUID

    Args:
        short_uuid (str):
        with_disabled_hosts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
    """

    return sync_detailed(
        short_uuid=short_uuid,
        client=client,
        with_disabled_hosts=with_disabled_hosts,
    ).parsed


async def asyncio_detailed(
    short_uuid: str,
    *,
    client: AuthenticatedClient,
    with_disabled_hosts: Union[Unset, bool] = UNSET,
) -> Response[
    Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
]:
    """Get Raw Subscription by Short UUID

    Args:
        short_uuid (str):
        with_disabled_hosts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]]
    """

    kwargs = _get_kwargs(
        short_uuid=short_uuid,
        with_disabled_hosts=with_disabled_hosts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    short_uuid: str,
    *,
    client: AuthenticatedClient,
    with_disabled_hosts: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
]:
    """Get Raw Subscription by Short UUID

    Args:
        short_uuid (str):
        with_disabled_hosts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRawSubscriptionByShortUuidResponseDto, SubscriptionControllerGetRawSubscriptionByShortUuidResponse500]
    """

    return (
        await asyncio_detailed(
            short_uuid=short_uuid,
            client=client,
            with_disabled_hosts=with_disabled_hosts,
        )
    ).parsed
