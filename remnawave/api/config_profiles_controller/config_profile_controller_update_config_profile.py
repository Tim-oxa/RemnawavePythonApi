from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_profile_controller_update_config_profile_response_500 import (
    ConfigProfileControllerUpdateConfigProfileResponse500,
)
from ...models.update_config_profile_request_dto import UpdateConfigProfileRequestDto
from ...models.update_config_profile_response_dto import UpdateConfigProfileResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateConfigProfileRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/config-profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]:
    if response.status_code == 200:
        response_200 = UpdateConfigProfileResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = ConfigProfileControllerUpdateConfigProfileResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateConfigProfileRequestDto,
) -> Response[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]:
    """Update Core Config in specific config profile

    Args:
        body (UpdateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]
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
    body: UpdateConfigProfileRequestDto,
) -> Optional[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]:
    """Update Core Config in specific config profile

    Args:
        body (UpdateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateConfigProfileRequestDto,
) -> Response[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]:
    """Update Core Config in specific config profile

    Args:
        body (UpdateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateConfigProfileRequestDto,
) -> Optional[Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]]:
    """Update Core Config in specific config profile

    Args:
        body (UpdateConfigProfileRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConfigProfileControllerUpdateConfigProfileResponse500, UpdateConfigProfileResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
