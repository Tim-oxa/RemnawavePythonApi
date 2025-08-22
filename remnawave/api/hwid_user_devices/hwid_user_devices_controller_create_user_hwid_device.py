from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_hwid_device_request_dto import CreateUserHwidDeviceRequestDto
from ...models.create_user_hwid_device_response_dto import CreateUserHwidDeviceResponseDto
from ...models.hwid_user_devices_controller_create_user_hwid_device_response_500 import (
    HwidUserDevicesControllerCreateUserHwidDeviceResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUserHwidDeviceRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/hwid/devices",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]:
    if response.status_code == 200:
        response_200 = CreateUserHwidDeviceResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = HwidUserDevicesControllerCreateUserHwidDeviceResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserHwidDeviceRequestDto,
) -> Response[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]:
    """Create a user HWID device

    Args:
        body (CreateUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]
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
    body: CreateUserHwidDeviceRequestDto,
) -> Optional[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]:
    """Create a user HWID device

    Args:
        body (CreateUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserHwidDeviceRequestDto,
) -> Response[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]:
    """Create a user HWID device

    Args:
        body (CreateUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUserHwidDeviceRequestDto,
) -> Optional[Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]]:
    """Create a user HWID device

    Args:
        body (CreateUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateUserHwidDeviceResponseDto, HwidUserDevicesControllerCreateUserHwidDeviceResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
