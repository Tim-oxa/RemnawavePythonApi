from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_hwid_device_request_dto import DeleteUserHwidDeviceRequestDto
from ...models.delete_user_hwid_device_response_dto import DeleteUserHwidDeviceResponseDto
from ...models.hwid_user_devices_controller_delete_user_hwid_device_response_500 import (
    HwidUserDevicesControllerDeleteUserHwidDeviceResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteUserHwidDeviceRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/hwid/devices/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]:
    if response.status_code == 200:
        response_200 = DeleteUserHwidDeviceResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = HwidUserDevicesControllerDeleteUserHwidDeviceResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteUserHwidDeviceRequestDto,
) -> Response[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]:
    """Delete a user HWID device

    Args:
        body (DeleteUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]
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
    body: DeleteUserHwidDeviceRequestDto,
) -> Optional[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]:
    """Delete a user HWID device

    Args:
        body (DeleteUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteUserHwidDeviceRequestDto,
) -> Response[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]:
    """Delete a user HWID device

    Args:
        body (DeleteUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DeleteUserHwidDeviceRequestDto,
) -> Optional[Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]]:
    """Delete a user HWID device

    Args:
        body (DeleteUserHwidDeviceRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteUserHwidDeviceResponseDto, HwidUserDevicesControllerDeleteUserHwidDeviceResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
