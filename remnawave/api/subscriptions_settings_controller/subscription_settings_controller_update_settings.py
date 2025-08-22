from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscription_settings_controller_update_settings_response_500 import (
    SubscriptionSettingsControllerUpdateSettingsResponse500,
)
from ...models.update_subscription_settings_request_dto import UpdateSubscriptionSettingsRequestDto
from ...models.update_subscription_settings_response_dto import UpdateSubscriptionSettingsResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateSubscriptionSettingsRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/subscription-settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]:
    if response.status_code == 200:
        response_200 = UpdateSubscriptionSettingsResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = SubscriptionSettingsControllerUpdateSettingsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateSubscriptionSettingsRequestDto,
) -> Response[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]:
    """Update subscription settings

    Args:
        body (UpdateSubscriptionSettingsRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateSubscriptionSettingsRequestDto,
) -> Optional[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]:
    """Update subscription settings

    Args:
        body (UpdateSubscriptionSettingsRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateSubscriptionSettingsRequestDto,
) -> Response[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]:
    """Update subscription settings

    Args:
        body (UpdateSubscriptionSettingsRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateSubscriptionSettingsRequestDto,
) -> Optional[Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]]:
    """Update subscription settings

    Args:
        body (UpdateSubscriptionSettingsRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SubscriptionSettingsControllerUpdateSettingsResponse500, UpdateSubscriptionSettingsResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
