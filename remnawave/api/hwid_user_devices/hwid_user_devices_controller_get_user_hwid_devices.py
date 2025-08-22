from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_hwid_devices_response_dto import GetUserHwidDevicesResponseDto
from ...models.hwid_user_devices_controller_get_user_hwid_devices_response_500 import (
    HwidUserDevicesControllerGetUserHwidDevicesResponse500,
)
from ...types import Response


def _get_kwargs(
    user_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/hwid/devices/{user_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]:
    if response.status_code == 200:
        response_200 = GetUserHwidDevicesResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = HwidUserDevicesControllerGetUserHwidDevicesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]:
    """Get user HWID devices

    Args:
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]:
    """Get user HWID devices

    Args:
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]
    """

    return sync_detailed(
        user_uuid=user_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]:
    """Get user HWID devices

    Args:
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]]:
    """Get user HWID devices

    Args:
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUserHwidDevicesResponseDto, HwidUserDevicesControllerGetUserHwidDevicesResponse500]
    """

    return (
        await asyncio_detailed(
            user_uuid=user_uuid,
            client=client,
        )
    ).parsed
