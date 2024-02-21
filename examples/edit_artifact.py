"""

Example - Edit an artifact from your connector

Last update: 2024-02-02

This request edits an artifact on a custom connector using a connection to the connector.
It uses a pre-established connection from the examples  request to our connector.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Edits an artifact from your connector.


Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.
    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to publish a data artifact on your connector.

Ensure that the required parameters are specified before executing the request:

    - artifact_id: Id of the artifact.
    - artifact_path: The path to the data artifact.
    - artifact_description: The description of the data artifact.
    - artifact_title: The title of the data artifact.
    - contract_offer_path: The path to the contract offer file.

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

    # Specify the required parameters:
    artifact_id = "<artifact_id>"
    artifact_path = "<artifact_path>"
    artifact_description = "<description>"
    artifact_title = "<title>"
    contract_offer_path = "../files/contracts/default.json"

    # Read the contract offer content from the file:
    with open(contract_offer_path, 'r') as file:
        contract_offer_content = file.read()

    # Post artifact on our connector:
    updated_data_artifact = conn.edit_artifact(
        artifact_id=artifact_id,
        artifact=artifact_path,
        contract_offer=contract_offer_content,
        description=artifact_description,
        title=artifact_title
    )

    print("-" * 79)
    print("Updated Data Artifact:")
    print(updated_data_artifact)
