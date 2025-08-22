from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_tokens_controller_find_all_response_500 import ApiTokensControllerFindAllResponse500
from ...models.find_all_api_tokens_response_dto import FindAllApiTokensResponseDto
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tokens",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]:
    if response.status_code == 200:
        response_200 = FindAllApiTokensResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = ApiTokensControllerFindAllResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]:
    r"""Get all API tokens

     This endpoint is forbidden to use via \"API-key\". It can only be used with admin JWT-token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]:
    r"""Get all API tokens

     This endpoint is forbidden to use via \"API-key\". It can only be used with admin JWT-token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]:
    r"""Get all API tokens

     This endpoint is forbidden to use via \"API-key\". It can only be used with admin JWT-token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]]:
    r"""Get all API tokens

     This endpoint is forbidden to use via \"API-key\". It can only be used with admin JWT-token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTokensControllerFindAllResponse500, FindAllApiTokensResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
