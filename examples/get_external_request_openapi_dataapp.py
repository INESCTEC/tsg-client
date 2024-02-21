"""

Example: Perform a GET request to an external OpenAPI endpoint (via Data APP)

Last update: 2024-01-27

This  request performs an external OpenAPI request using a connection to a
custom connector.

It loads environment variables from a .env file, establishes a connection to
the custom connector, and then executes an OpenAPI request using the specified
API version and endpoint.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Execute an HTTP (GET) request to an external OpenAPI endpoint (via Data APP)

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to get perform a GET request to an external OpenAPI endpoint (via Data APP)

"""


if __name__ == "__main__":
    from loguru import logger
    from dotenv import dotenv_values
    from tsg_client.controllers import TSGController

    # Comment the line below to enable internal logger:
    logger.disable("")

    # Load environment variables:
    config = dotenv_values('.env')

    # Example of external connector configs (TNO Playground)
    EXTERNAL_CONNECTOR = {
        "CONNECTOR_ID": 'urn:playground:tsg:connectors:TestConnector',
        "ACCESS_URL": 'https://test-connector.playground.dataspac.es/router',
        "AGENT_ID": 'urn:playground:tsg:TNO'
    }

    # Connect to our TSG connector:
    conn = TSGController(
        api_key=config['API_KEY'],
        connector_id=config['CONNECTOR_ID'],
        access_url=config['ACCESS_URL'],
        agent_id=config['AGENT_ID']
    )

    # Execute external OpenAPI request:
    api_version = "0.9.2"
    endpoint = "uuid"

    response = conn.openapi_request(
        external_access_url=EXTERNAL_CONNECTOR['ACCESS_URL'],
        external_connector_id=EXTERNAL_CONNECTOR['CONNECTOR_ID'],
        api_version=api_version,
        endpoint=endpoint,
        params="",
        method="get"
    )

    print("-" * 79)
    print(f"> Connector {EXTERNAL_CONNECTOR['CONNECTOR_ID']} RESPONSE:")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
