
from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoints:
    METADATA_BROKER_CONNECTORS = "api/connectors/full"
    SELF_DESCRIPTION = "selfdescription"
    DESCRIPTION = "api/description"
    RESOURCES = "api/resources"
    ARTIFACTS_CONSUMER = "api/artifacts/consumer/artifact"
    ARTIFACTS_PROVIDER = "api/artifacts/provider"
    CONTRACT_REQUEST = "api/artifacts/consumer/contractRequest"
    OPEN_API = "openapi"
