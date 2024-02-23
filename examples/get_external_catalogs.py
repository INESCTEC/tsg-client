"""

Example: Extract catalogs from self-descriptions of an external connector

Last update: 2024-01-27

This request retrieves and prints information about external connector
catalogs using a pre-established connection to your TSG connector.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Retrieve and print information about external connector self-description
    4. Extract (from self-descriptions) information regarding available catalogs

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to get your connector self-description catalogs.

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
        "ACCESS_URL": 'https://test-connector.playground.dataspac.es',
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
    description = conn.get_connector_selfdescription(
        access_url=EXTERNAL_CONNECTOR['ACCESS_URL'],
        connector_id=EXTERNAL_CONNECTOR['CONNECTOR_ID'],
        agent_id=EXTERNAL_CONNECTOR['AGENT_ID']
    )

    # Get external connector catalogs:
    catalogs = conn.parse_resource_catalogs(self_description=description)

    print("-" * 79)
    print(f"> Connector {EXTERNAL_CONNECTOR['CONNECTOR_ID']} Catalogs:")
    pprint(catalogs)
