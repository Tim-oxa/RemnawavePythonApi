from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_node_request_dto import CreateNodeRequestDto
from ...models.create_node_response_dto import CreateNodeResponseDto
from ...models.nodes_controller_create_node_response_500 import NodesControllerCreateNodeResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateNodeRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/nodes",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]:
    if response.status_code == 201:
        response_201 = CreateNodeResponseDto.from_dict(response.json())

        return response_201
    if response.status_code == 500:
        response_500 = NodesControllerCreateNodeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateNodeRequestDto,
) -> Response[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]:
    """Create a new node

    Args:
        body (CreateNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]
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
    body: CreateNodeRequestDto,
) -> Optional[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]:
    """Create a new node

    Args:
        body (CreateNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateNodeRequestDto,
) -> Response[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]:
    """Create a new node

    Args:
        body (CreateNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateNodeRequestDto,
) -> Optional[Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]]:
    """Create a new node

    Args:
        body (CreateNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateNodeResponseDto, NodesControllerCreateNodeResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
