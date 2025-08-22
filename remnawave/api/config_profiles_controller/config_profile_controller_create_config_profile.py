from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_profile_controller_create_config_profile_response_500 import (
    ConfigProfileControllerCreateConfigProfileResponse500,
)
from ...models.create_config_profile_request_dto import CreateConfigProfileRequestDto
from ...models.create_config_profile_response_dto import CreateConfigProfileResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: CreateConfigProfileRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/config-profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]:
    if response.status_code == 201:
        response_201 = CreateConfigProfileResponseDto.from_dict(response.json())

        return response_201
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = ConfigProfileControllerCreateConfigProfileResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateConfigProfileRequestDto,
) -> Response[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]:
    """Create config profile

    Args:
        body (CreateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]
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
    body: CreateConfigProfileRequestDto,
) -> Optional[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]:
    """Create config profile

    Args:
        body (CreateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateConfigProfileRequestDto,
) -> Response[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]:
    """Create config profile

    Args:
        body (CreateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateConfigProfileRequestDto,
) -> Optional[Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]]:
    """Create config profile

    Args:
        body (CreateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConfigProfileControllerCreateConfigProfileResponse500, CreateConfigProfileResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
