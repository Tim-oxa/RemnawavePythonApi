from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.infra_billing_controller_update_infra_billing_node_response_500 import (
    InfraBillingControllerUpdateInfraBillingNodeResponse500,
)
from ...models.update_infra_billing_node_request_dto import UpdateInfraBillingNodeRequestDto
from ...models.update_infra_billing_node_response_dto import UpdateInfraBillingNodeResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateInfraBillingNodeRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/infra-billing/nodes",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]:
    if response.status_code == 200:
        response_200 = UpdateInfraBillingNodeResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = InfraBillingControllerUpdateInfraBillingNodeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateInfraBillingNodeRequestDto,
) -> Response[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]:
    """Update infra billing node

    Args:
        body (UpdateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]
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
    body: UpdateInfraBillingNodeRequestDto,
) -> Optional[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]:
    """Update infra billing node

    Args:
        body (UpdateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateInfraBillingNodeRequestDto,
) -> Response[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]:
    """Update infra billing node

    Args:
        body (UpdateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateInfraBillingNodeRequestDto,
) -> Optional[Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]]:
    """Update infra billing node

    Args:
        body (UpdateInfraBillingNodeRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InfraBillingControllerUpdateInfraBillingNodeResponse500, UpdateInfraBillingNodeResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
