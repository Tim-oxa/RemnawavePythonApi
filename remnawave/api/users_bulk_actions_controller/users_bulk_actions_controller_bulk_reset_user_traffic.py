from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_reset_traffic_users_request_dto import BulkResetTrafficUsersRequestDto
from ...models.bulk_reset_traffic_users_response_dto import BulkResetTrafficUsersResponseDto
from ...models.users_bulk_actions_controller_bulk_reset_user_traffic_response_500 import (
    UsersBulkActionsControllerBulkResetUserTrafficResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: BulkResetTrafficUsersRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/bulk/reset-traffic",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]:
    if response.status_code == 200:
        response_200 = BulkResetTrafficUsersResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = UsersBulkActionsControllerBulkResetUserTrafficResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkResetTrafficUsersRequestDto,
) -> Response[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]:
    """Bulk reset traffic users by UUIDs

    Args:
        body (BulkResetTrafficUsersRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]
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
    body: BulkResetTrafficUsersRequestDto,
) -> Optional[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]:
    """Bulk reset traffic users by UUIDs

    Args:
        body (BulkResetTrafficUsersRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkResetTrafficUsersRequestDto,
) -> Response[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]:
    """Bulk reset traffic users by UUIDs

    Args:
        body (BulkResetTrafficUsersRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkResetTrafficUsersRequestDto,
) -> Optional[Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]]:
    """Bulk reset traffic users by UUIDs

    Args:
        body (BulkResetTrafficUsersRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkResetUserTrafficResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
