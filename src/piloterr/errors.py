"""Piloterr SDK error categories."""

from __future__ import annotations

from typing import Any

from .models import JsonResponse, RawResponse


class PiloterrError(Exception):
    """Base class for all SDK-defined errors."""


class PiloterrConfigurationError(PiloterrError):
    """The client configuration is missing or unusable."""


class PiloterrSerializationError(PiloterrError):
    """A request value cannot be represented safely on the wire."""

    param: str | None

    def __init__(self, message: str, param: str | None = None) -> None:
        super().__init__(message)
        self.param = param


class PiloterrTransportError(PiloterrError):
    """The request failed before a complete HTTP response was received."""

    cause: Exception

    def __init__(self, message: str, cause: Exception) -> None:
        super().__init__(message)
        self.cause = cause


class PiloterrAPIError(PiloterrError):
    """Piloterr returned a non-success HTTP status."""

    status: int
    error_message: str | None
    response_body: Any | None
    raw_response: RawResponse

    def __init__(
        self,
        *,
        raw_response: RawResponse,
        response_body: Any | None = None,
        error_message: str | None = None,
    ) -> None:
        super().__init__(
            error_message or f"Piloterr API request failed with status {raw_response.status}."
        )
        self.status = raw_response.status
        self.error_message = error_message
        self.response_body = response_body
        self.raw_response = raw_response


class PiloterrResponseDecodingError(PiloterrError):
    """A successful response could not be decoded as the documented representation."""

    raw_response: RawResponse
    cause: Exception | None

    def __init__(
        self, message: str, raw_response: RawResponse, cause: Exception | None = None
    ) -> None:
        super().__init__(message)
        self.raw_response = raw_response
        self.cause = cause


class PiloterrJobTimeoutError(PiloterrError):
    """An async job did not reach a terminal status before the deadline."""

    job_id: str
    last_response: JsonResponse | None

    def __init__(self, job_id: str, last_response: JsonResponse | None = None) -> None:
        super().__init__(f"Job {job_id} did not finish before the deadline.")
        self.job_id = job_id
        self.last_response = last_response
