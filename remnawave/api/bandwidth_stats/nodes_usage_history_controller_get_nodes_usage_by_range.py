import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_nodes_usage_by_range_response_dto import GetNodesUsageByRangeResponseDto
from ...models.nodes_usage_history_controller_get_nodes_usage_by_range_response_500 import (
    NodesUsageHistoryControllerGetNodesUsageByRangeResponse500,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start: datetime.datetime,
    end: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/nodes/usage/range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]:
    if response.status_code == 200:
        response_200 = GetNodesUsageByRangeResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = NodesUsageHistoryControllerGetNodesUsageByRangeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]:
    """Get nodes usage by range

    Args:
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]:
    """Get nodes usage by range

    Args:
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]:
    """Get nodes usage by range

    Args:
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]]:
    """Get nodes usage by range

    Args:
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetNodesUsageByRangeResponseDto, NodesUsageHistoryControllerGetNodesUsageByRangeResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
        )
    ).parsed
