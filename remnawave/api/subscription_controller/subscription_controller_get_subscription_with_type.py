from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    short_uuid: str,
    type_: str,
    encoded_tag: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/sub/outline/{short_uuid}/{type_}/{encoded_tag}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    short_uuid: str,
    type_: str,
    encoded_tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """
    Args:
        short_uuid (str):
        type_ (str):  Example: ss.
        encoded_tag (str):  Example: VGVzdGVy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        short_uuid=short_uuid,
        type_=type_,
        encoded_tag=encoded_tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    short_uuid: str,
    type_: str,
    encoded_tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """
    Args:
        short_uuid (str):
        type_ (str):  Example: ss.
        encoded_tag (str):  Example: VGVzdGVy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        short_uuid=short_uuid,
        type_=type_,
        encoded_tag=encoded_tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
