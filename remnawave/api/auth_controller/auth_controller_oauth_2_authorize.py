from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_controller_oauth_2_authorize_response_500 import AuthControllerOauth2AuthorizeResponse500
from ...models.o_auth_2_authorize_request_dto import OAuth2AuthorizeRequestDto
from ...types import Response


def _get_kwargs(
    *,
    body: OAuth2AuthorizeRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/oauth2/authorize",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuthControllerOauth2AuthorizeResponse500]:
    if response.status_code == 500:
        response_500 = AuthControllerOauth2AuthorizeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuthControllerOauth2AuthorizeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OAuth2AuthorizeRequestDto,
) -> Response[AuthControllerOauth2AuthorizeResponse500]:
    """Initiate OAuth2 authorization

    Args:
        body (OAuth2AuthorizeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthControllerOauth2AuthorizeResponse500]
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
    client: Union[AuthenticatedClient, Client],
    body: OAuth2AuthorizeRequestDto,
) -> Optional[AuthControllerOauth2AuthorizeResponse500]:
    """Initiate OAuth2 authorization

    Args:
        body (OAuth2AuthorizeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthControllerOauth2AuthorizeResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OAuth2AuthorizeRequestDto,
) -> Response[AuthControllerOauth2AuthorizeResponse500]:
    """Initiate OAuth2 authorization

    Args:
        body (OAuth2AuthorizeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthControllerOauth2AuthorizeResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OAuth2AuthorizeRequestDto,
) -> Optional[AuthControllerOauth2AuthorizeResponse500]:
    """Initiate OAuth2 authorization

    Args:
        body (OAuth2AuthorizeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthControllerOauth2AuthorizeResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
