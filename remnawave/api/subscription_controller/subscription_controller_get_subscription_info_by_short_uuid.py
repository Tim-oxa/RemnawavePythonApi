from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscription_info_response_dto import GetSubscriptionInfoResponseDto
from ...models.subscription_controller_get_subscription_info_by_short_uuid_response_500 import (
    SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500,
)
from ...types import Response


def _get_kwargs(
    short_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/sub/{short_uuid}/info",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]:
    if response.status_code == 200:
        response_200 = GetSubscriptionInfoResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    short_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]:
    """Get Subscription Info by Short UUID

    Args:
        short_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]
    """

    kwargs = _get_kwargs(
        short_uuid=short_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    short_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]:
    """Get Subscription Info by Short UUID

    Args:
        short_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]
    """

    return sync_detailed(
        short_uuid=short_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    short_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]:
    """Get Subscription Info by Short UUID

    Args:
        short_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]
    """

    kwargs = _get_kwargs(
        short_uuid=short_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    short_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]]:
    """Get Subscription Info by Short UUID

    Args:
        short_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSubscriptionInfoResponseDto, SubscriptionControllerGetSubscriptionInfoByShortUuidResponse500]
    """

    return (
        await asyncio_detailed(
            short_uuid=short_uuid,
            client=client,
        )
    ).parsed
