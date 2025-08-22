from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_user_subscription_body_dto import RevokeUserSubscriptionBodyDto
from ...models.revoke_user_subscription_response_dto import RevokeUserSubscriptionResponseDto
from ...models.users_controller_revoke_user_subscription_response_500 import (
    UsersControllerRevokeUserSubscriptionResponse500,
)
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    body: RevokeUserSubscriptionBodyDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/users/{uuid}/actions/revoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]:
    if response.status_code == 200:
        response_200 = RevokeUserSubscriptionResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = UsersControllerRevokeUserSubscriptionResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]:
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
    body: RevokeUserSubscriptionBodyDto,
) -> Response[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]:
    """Revoke user subscription

    Args:
        uuid (str):
        body (RevokeUserSubscriptionBodyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: RevokeUserSubscriptionBodyDto,
) -> Optional[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]:
    """Revoke user subscription

    Args:
        uuid (str):
        body (RevokeUserSubscriptionBodyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: RevokeUserSubscriptionBodyDto,
) -> Response[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]:
    """Revoke user subscription

    Args:
        uuid (str):
        body (RevokeUserSubscriptionBodyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: RevokeUserSubscriptionBodyDto,
) -> Optional[Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]]:
    """Revoke user subscription

    Args:
        uuid (str):
        body (RevokeUserSubscriptionBodyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RevokeUserSubscriptionResponseDto, UsersControllerRevokeUserSubscriptionResponse500]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
