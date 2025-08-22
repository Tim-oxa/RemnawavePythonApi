from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_squad_controller_remove_users_from_internal_squad_response_500 import (
    InternalSquadControllerRemoveUsersFromInternalSquadResponse500,
)
from ...models.remove_users_from_internal_squad_response_dto import RemoveUsersFromInternalSquadResponseDto
from ...types import Response


def _get_kwargs(
    uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/internal-squads/{uuid}/bulk-actions/remove-users",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
]:
    if response.status_code == 200:
        response_200 = RemoveUsersFromInternalSquadResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = InternalSquadControllerRemoveUsersFromInternalSquadResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
]:
    """Delete users from internal squad

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
]:
    """Delete users from internal squad

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
]:
    """Delete users from internal squad

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
]:
    """Delete users from internal squad

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InternalSquadControllerRemoveUsersFromInternalSquadResponse500, RemoveUsersFromInternalSquadResponseDto]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
