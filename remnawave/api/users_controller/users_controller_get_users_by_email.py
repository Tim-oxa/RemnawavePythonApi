from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_by_email_response_dto import GetUserByEmailResponseDto
from ...models.users_controller_get_users_by_email_response_500 import UsersControllerGetUsersByEmailResponse500
from ...types import Response


def _get_kwargs(
    email: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/users/by-email/{email}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]:
    if response.status_code == 200:
        response_200 = GetUserByEmailResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = UsersControllerGetUsersByEmailResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]:
    """Get users by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]:
    """Get users by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]
    """

    return sync_detailed(
        email=email,
        client=client,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]:
    """Get users by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]]:
    """Get users by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserByEmailResponseDto, UsersControllerGetUsersByEmailResponse500]
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
        )
    ).parsed
