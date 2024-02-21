"""

Example: Get the artifacts list of an external connector

Last update: 2024-01-27

This  request retrieves and prints information about external connector
artifacts using a pre-established connection to your connector.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Retrieve and print information about external connector self-description
    4. Extract (from self-descriptions) information regarding available artifacts

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to get your connector self-description artifacts list.

"""


if __name__ == "__main__":
    from pprint import pprint
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
        "ACCESS_URL": 'https://test-connector.playground.dataspac.es/selfdescription',
        "AGENT_ID": 'urn:playground:tsg:TNO'
    }

    # Connect to our TSG connector:
    conn = TSGController(
        api_key=config['API_KEY'],
        connector_id=config['CONNECTOR_ID'],
        access_url=config['ACCESS_URL'],
        agent_id=config['AGENT_ID']
    )

    # Get external connector info (self-descriptions):
    self_description = conn.get_connector_selfdescription(
        access_url=EXTERNAL_CONNECTOR['ACCESS_URL'],
        connector_id=EXTERNAL_CONNECTOR['CONNECTOR_ID'],
        agent_id=EXTERNAL_CONNECTOR['AGENT_ID']
    )

    resource_type = "ids:ContractOffer"

    # Get artifacts list (note that you can refine your search using the
    # cursom filters below):
    artifacts = conn.parse_catalog_artifacts(
        self_description,
        catalog_id=self_description.catalogs[0].id,
        resource_type=resource_type,
        creation_date_gt="2021-08-10T00:00:00.000Z",
        creation_date_lt="2030-01-01T00:00:00.000Z",
        return_last_artifact=True,
        valid_contract_only=False
    )

    print("-" * 79)
    print(f"> Connector {EXTERNAL_CONNECTOR['CONNECTOR_ID']} in "
          f"catalog {self_description.catalogs[0].id} with "
          f"resource type {resource_type} has this list artifacts:")
    pprint(artifacts)
