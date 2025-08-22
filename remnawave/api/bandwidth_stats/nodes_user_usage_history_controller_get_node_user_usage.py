import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_node_user_usage_by_range_response_dto import GetNodeUserUsageByRangeResponseDto
from ...models.nodes_user_usage_history_controller_get_node_user_usage_response_500 import (
    NodesUserUsageHistoryControllerGetNodeUserUsageResponse500,
)
from ...types import UNSET, Response


def _get_kwargs(
    uuid: str,
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
        "url": f"/api/nodes/usage/{uuid}/users/range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]:
    if response.status_code == 200:
        response_200 = GetNodeUserUsageByRangeResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = NodesUserUsageHistoryControllerGetNodeUserUsageResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]:
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
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]:
    """Get node user usage by range and Node UUID

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]:
    """Get node user usage by range and Node UUID

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]:
    """Get node user usage by range and Node UUID

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]]:
    """Get node user usage by range and Node UUID

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetNodeUserUsageByRangeResponseDto, NodesUserUsageHistoryControllerGetNodeUserUsageResponse500]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
