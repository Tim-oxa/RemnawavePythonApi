from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_by_username_response_dto import GetUserByUsernameResponseDto
from ...models.users_controller_get_user_by_username_response_500 import UsersControllerGetUserByUsernameResponse500
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/users/by-username/{username}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]:
    if response.status_code == 200:
        response_200 = GetUserByUsernameResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = UsersControllerGetUserByUsernameResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]:
    """Get user by username

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]:
    """Get user by username

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]:
    """Get user by username

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]]:
    """Get user by username

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserByUsernameResponseDto, UsersControllerGetUserByUsernameResponse500]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
