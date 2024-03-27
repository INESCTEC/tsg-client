"""

Example - Delete an artifact via your connector

Last update: 2024-02-01

This  request deletes an artifact on a custom connector using a connection to the connector.
It uses a pre-established connection from the examples  request to our connector.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Deletes the artifact from your connector.

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to delete an artifact from your connector.

Ensure that the required parameters are specified before executing the  request:

    - artifact_id: The id of the artifact.

"""


if __name__ == "__main__":
    from loguru import logger
    from dotenv import dotenv_values
    from tsg_client.controllers import TSGController

    # Comment the line below to enable internal logger:
    logger.disable("")

    # Load environment variables:
    config = dotenv_values('.env')

    # Connect to our TSG connector:
    conn = TSGController(
        api_key=config['API_KEY'],
        connector_id=config['CONNECTOR_ID'],
        access_url=config['ACCESS_URL'],
        agent_id=config['AGENT_ID']
    )

    # Specify the required parameters:
    artifact_id = "<artifact_id>"

    # Post artifact on our connector:
    conn.delete_artifact(artifact_id)
