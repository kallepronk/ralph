"""Module py.test fixtures."""

# pylint: disable=unused-import

from .fixtures import hypothesis_configuration  # noqa: F401
from .fixtures import hypothesis_strategies  # noqa: F401
from .fixtures.auth import (  # noqa: F401
    auth_credentials,
    basic_auth_test_client,
    encoded_token,
    mock_discovery_response,
    mock_oidc_jwks,
    oidc_auth_test_client,
)
from .fixtures.backends import (  # noqa: F401
    anyio_backend,
    clickhouse,
    es,
    es_data_stream,
    es_forwarding,
    events,
    lrs,
    mongo,
    mongo_forwarding,
    moto_fs,
    s3,
    settings_fs,
    swift,
    ws,
)
from .fixtures.logs import gelf_logger  # noqa: F401
