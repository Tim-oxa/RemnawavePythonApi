from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_delete_users_by_status_request_dto import BulkDeleteUsersByStatusRequestDto
from ...models.bulk_delete_users_by_status_response_dto import BulkDeleteUsersByStatusResponseDto
from ...models.users_bulk_actions_controller_bulk_delete_users_by_status_response_500 import (
    UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: BulkDeleteUsersByStatusRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/bulk/delete-by-status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]:
    if response.status_code == 200:
        response_200 = BulkDeleteUsersByStatusResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteUsersByStatusRequestDto,
) -> Response[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]:
    """Bulk delete users by status

    Args:
        body (BulkDeleteUsersByStatusRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]
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
    body: BulkDeleteUsersByStatusRequestDto,
) -> Optional[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]:
    """Bulk delete users by status

    Args:
        body (BulkDeleteUsersByStatusRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteUsersByStatusRequestDto,
) -> Response[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]:
    """Bulk delete users by status

    Args:
        body (BulkDeleteUsersByStatusRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteUsersByStatusRequestDto,
) -> Optional[Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]]:
    """Bulk delete users by status

    Args:
        body (BulkDeleteUsersByStatusRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkDeleteUsersByStatusResponseDto, UsersBulkActionsControllerBulkDeleteUsersByStatusResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
