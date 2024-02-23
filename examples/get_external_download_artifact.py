"""

Example: Perform a contract agreement and download an artifact from an external connector

Last update: 2024-01-27

This  request requests a contract agreement and retrieves content for an external artifact
using a connection to a custom connector. It loads environment variables from a .env file,
establishes a connection to the custom connector, and then requests a contract agreement
and retrieves content for the first external artifact.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Retrieve and print information about external connector self-description
    4. Extract (from self-descriptions) information regarding available artifacts
    5. Request a contract agreement for the first artifact
    6. Retrieve content for the first artifact

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to download an artifact from an external connector.

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
    self_description = conn.get_connector_selfdescription(
        access_url=EXTERNAL_CONNECTOR['ACCESS_URL'],
        connector_id=EXTERNAL_CONNECTOR['CONNECTOR_ID'],
        agent_id=EXTERNAL_CONNECTOR['AGENT_ID']
    )

    # Get external connector artifacts
    artifacts = conn.parse_catalog_artifacts(self_description=self_description)

    # Preview first artifact contract offer & request agreement
    example_artifact = artifacts[0]  # first artifact
    print("-" * 79)
    print("> Contract Offer (from external connector):")
    pprint(example_artifact['contract_offer'])

    # Request contract agreement for the first artifact
    contract_agreement_id = conn.request_agreement(
        connector_id=EXTERNAL_CONNECTOR['CONNECTOR_ID'],
        artifact_access_url=example_artifact['access_url'],
        artifact_contract_offer=example_artifact['contract_offer']
    )

    print("-" * 79)
    print("> Contract Agreement Identifier:")
    print(contract_agreement_id)

    # Retrieve content for the first artifact
    artifact_content = conn.request_data_artifact(
        artifact_id=artifacts[0]['id'],
        artifact_access_url=artifacts[0]['access_url'],
        agent_id=EXTERNAL_CONNECTOR['AGENT_ID'],
        connector_id=EXTERNAL_CONNECTOR['CONNECTOR_ID'],
        contract_agreement_id=contract_agreement_id,
        keep_original_format=True,
        file_path=""
    )
