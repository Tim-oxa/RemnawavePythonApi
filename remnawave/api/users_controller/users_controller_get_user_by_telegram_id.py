from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_by_telegram_id_response_dto import GetUserByTelegramIdResponseDto
from ...models.users_controller_get_user_by_telegram_id_response_500 import (
    UsersControllerGetUserByTelegramIdResponse500,
)
from ...types import Response


def _get_kwargs(
    telegram_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/users/by-telegram-id/{telegram_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]:
    if response.status_code == 200:
        response_200 = GetUserByTelegramIdResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = UsersControllerGetUserByTelegramIdResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    telegram_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]:
    """Get users by telegram ID

    Args:
        telegram_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]
    """

    kwargs = _get_kwargs(
        telegram_id=telegram_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    telegram_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]:
    """Get users by telegram ID

    Args:
        telegram_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]
    """

    return sync_detailed(
        telegram_id=telegram_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    telegram_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]:
    """Get users by telegram ID

    Args:
        telegram_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]
    """

    kwargs = _get_kwargs(
        telegram_id=telegram_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    telegram_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]]:
    """Get users by telegram ID

    Args:
        telegram_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserByTelegramIdResponseDto, UsersControllerGetUserByTelegramIdResponse500]
    """

    return (
        await asyncio_detailed(
            telegram_id=telegram_id,
            client=client,
        )
    ).parsed
