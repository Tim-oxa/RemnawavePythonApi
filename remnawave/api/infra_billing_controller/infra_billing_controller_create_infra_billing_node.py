from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_infra_billing_node_request_dto import CreateInfraBillingNodeRequestDto
from ...models.create_infra_billing_node_response_dto import CreateInfraBillingNodeResponseDto
from ...models.infra_billing_controller_create_infra_billing_node_response_500 import (
    InfraBillingControllerCreateInfraBillingNodeResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CreateInfraBillingNodeRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/infra-billing/nodes",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]:
    if response.status_code == 201:
        response_201 = CreateInfraBillingNodeResponseDto.from_dict(response.json())

        return response_201
    if response.status_code == 500:
        response_500 = InfraBillingControllerCreateInfraBillingNodeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInfraBillingNodeRequestDto,
) -> Response[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]:
    """Create infra billing node

    Args:
        body (CreateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]
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
    body: CreateInfraBillingNodeRequestDto,
) -> Optional[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]:
    """Create infra billing node

    Args:
        body (CreateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInfraBillingNodeRequestDto,
) -> Response[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]:
    """Create infra billing node

    Args:
        body (CreateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInfraBillingNodeRequestDto,
) -> Optional[Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]]:
    """Create infra billing node

    Args:
        body (CreateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateInfraBillingNodeResponseDto, InfraBillingControllerCreateInfraBillingNodeResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
