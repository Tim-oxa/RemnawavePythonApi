from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_all_reset_traffic_users_response_dto import BulkAllResetTrafficUsersResponseDto
from ...models.users_bulk_actions_controller_bulk_all_reset_user_traffic_response_500 import (
    UsersBulkActionsControllerBulkAllResetUserTrafficResponse500,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/bulk/all/reset-traffic",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]:
    if response.status_code == 200:
        response_200 = BulkAllResetTrafficUsersResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = UsersBulkActionsControllerBulkAllResetUserTrafficResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]:
    """Bulk Reset All Users Traffic

     Bulk reset all users traffic

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]:
    """Bulk Reset All Users Traffic

     Bulk reset all users traffic

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]:
    """Bulk Reset All Users Traffic

     Bulk reset all users traffic

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]]:
    """Bulk Reset All Users Traffic

     Bulk reset all users traffic

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkAllResetTrafficUsersResponseDto, UsersBulkActionsControllerBulkAllResetUserTrafficResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
