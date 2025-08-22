from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_template_response_dto import GetTemplateResponseDto
from ...models.subscription_template_controller_get_template_response_500 import (
    SubscriptionTemplateControllerGetTemplateResponse500,
)
from ...models.subscription_template_controller_get_template_template_type import (
    SubscriptionTemplateControllerGetTemplateTemplateType,
)
from ...types import Response


def _get_kwargs(
    template_type: SubscriptionTemplateControllerGetTemplateTemplateType,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/subscription-templates/{template_type}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]:
    if response.status_code == 200:
        response_200 = GetTemplateResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = SubscriptionTemplateControllerGetTemplateResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_type: SubscriptionTemplateControllerGetTemplateTemplateType,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]:
    """Get subscription template

    Args:
        template_type (SubscriptionTemplateControllerGetTemplateTemplateType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]
    """

    kwargs = _get_kwargs(
        template_type=template_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_type: SubscriptionTemplateControllerGetTemplateTemplateType,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]:
    """Get subscription template

    Args:
        template_type (SubscriptionTemplateControllerGetTemplateTemplateType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]
    """

    return sync_detailed(
        template_type=template_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_type: SubscriptionTemplateControllerGetTemplateTemplateType,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]:
    """Get subscription template

    Args:
        template_type (SubscriptionTemplateControllerGetTemplateTemplateType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]
    """

    kwargs = _get_kwargs(
        template_type=template_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_type: SubscriptionTemplateControllerGetTemplateTemplateType,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]]:
    """Get subscription template

    Args:
        template_type (SubscriptionTemplateControllerGetTemplateTemplateType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTemplateResponseDto, SubscriptionTemplateControllerGetTemplateResponse500]
    """

    return (
        await asyncio_detailed(
            template_type=template_type,
            client=client,
        )
    ).parsed
