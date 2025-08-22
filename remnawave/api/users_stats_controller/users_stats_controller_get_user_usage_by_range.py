import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_usage_by_range_response_dto import GetUserUsageByRangeResponseDto
from ...models.users_stats_controller_get_user_usage_by_range_response_500 import (
    UsersStatsControllerGetUserUsageByRangeResponse500,
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
        "url": f"/api/users/stats/usage/{uuid}/range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]:
    if response.status_code == 200:
        response_200 = GetUserUsageByRangeResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = UsersStatsControllerGetUserUsageByRangeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]:
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
) -> Response[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]:
    """Get user usage by range

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]
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
) -> Optional[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]:
    """Get user usage by range

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]
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
) -> Response[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]:
    """Get user usage by range

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]
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
) -> Optional[Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]]:
    """Get user usage by range

    Args:
        uuid (str):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetUserUsageByRangeResponseDto, UsersStatsControllerGetUserUsageByRangeResponse500]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
