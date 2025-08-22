from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_internal_squad_request_dto import CreateInternalSquadRequestDto
from ...models.create_internal_squad_response_dto import CreateInternalSquadResponseDto
from ...models.internal_squad_controller_create_internal_squad_response_500 import (
    InternalSquadControllerCreateInternalSquadResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CreateInternalSquadRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/internal-squads",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]:
    if response.status_code == 201:
        response_201 = CreateInternalSquadResponseDto.from_dict(response.json())

        return response_201
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = InternalSquadControllerCreateInternalSquadResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInternalSquadRequestDto,
) -> Response[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]:
    """Create internal squad

    Args:
        body (CreateInternalSquadRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]
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
    body: CreateInternalSquadRequestDto,
) -> Optional[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]:
    """Create internal squad

    Args:
        body (CreateInternalSquadRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInternalSquadRequestDto,
) -> Response[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]:
    """Create internal squad

    Args:
        body (CreateInternalSquadRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInternalSquadRequestDto,
) -> Optional[Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]]:
    """Create internal squad

    Args:
        body (CreateInternalSquadRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateInternalSquadResponseDto, InternalSquadControllerCreateInternalSquadResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
