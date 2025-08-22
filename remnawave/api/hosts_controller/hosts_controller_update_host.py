from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hosts_controller_update_host_response_500 import HostsControllerUpdateHostResponse500
from ...models.update_host_request_dto import UpdateHostRequestDto
from ...models.update_host_response_dto import UpdateHostResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateHostRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/hosts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]:
    if response.status_code == 200:
        response_200 = UpdateHostResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = HostsControllerUpdateHostResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateHostRequestDto,
) -> Response[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]:
    """Update a host

    Args:
        body (UpdateHostRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]
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
    body: UpdateHostRequestDto,
) -> Optional[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]:
    """Update a host

    Args:
        body (UpdateHostRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateHostRequestDto,
) -> Response[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]:
    """Update a host

    Args:
        body (UpdateHostRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateHostRequestDto,
) -> Optional[Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]]:
    """Update a host

    Args:
        body (UpdateHostRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HostsControllerUpdateHostResponse500, UpdateHostResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
