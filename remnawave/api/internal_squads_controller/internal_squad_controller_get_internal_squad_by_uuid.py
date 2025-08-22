from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_internal_squad_by_uuid_response_dto import GetInternalSquadByUuidResponseDto
from ...models.internal_squad_controller_get_internal_squad_by_uuid_response_500 import (
    InternalSquadControllerGetInternalSquadByUuidResponse500,
)
from ...types import Response


def _get_kwargs(
    uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/internal-squads/{uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]:
    if response.status_code == 200:
        response_200 = GetInternalSquadByUuidResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = InternalSquadControllerGetInternalSquadByUuidResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]:
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
) -> Response[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]:
    """Get internal squad by uuid

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]
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
) -> Optional[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]:
    """Get internal squad by uuid

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]:
    """Get internal squad by uuid

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]
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
) -> Optional[Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]]:
    """Get internal squad by uuid

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetInternalSquadByUuidResponseDto, InternalSquadControllerGetInternalSquadByUuidResponse500]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
