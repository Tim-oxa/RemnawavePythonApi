from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_tokens_controller_create_response_500 import ApiTokensControllerCreateResponse500
from ...models.create_api_token_request_dto import CreateApiTokenRequestDto
from ...models.create_api_token_response_dto import CreateApiTokenResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: CreateApiTokenRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]:
    if response.status_code == 201:
        response_201 = CreateApiTokenResponseDto.from_dict(response.json())

        return response_201
    if response.status_code == 500:
        response_500 = ApiTokensControllerCreateResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateApiTokenRequestDto,
) -> Response[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]:
    r"""Create a new API token

     This endpoint is forbidden to use via \"API-key\". It can only be used with an admin JWT-token.

    Args:
        body (CreateApiTokenRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]
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
    body: CreateApiTokenRequestDto,
) -> Optional[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]:
    r"""Create a new API token

     This endpoint is forbidden to use via \"API-key\". It can only be used with an admin JWT-token.

    Args:
        body (CreateApiTokenRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateApiTokenRequestDto,
) -> Response[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]:
    r"""Create a new API token

     This endpoint is forbidden to use via \"API-key\". It can only be used with an admin JWT-token.

    Args:
        body (CreateApiTokenRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateApiTokenRequestDto,
) -> Optional[Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]]:
    r"""Create a new API token

     This endpoint is forbidden to use via \"API-key\". It can only be used with an admin JWT-token.

    Args:
        body (CreateApiTokenRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTokensControllerCreateResponse500, CreateApiTokenResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
