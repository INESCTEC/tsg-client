"""

Example: Get self-descriptions of your TSG Connector

Last update: 2024-01-27

This request retrieves and prints information about your connector's
self-description (aka self-self-description) and displays the parsed result
in a simple Python dictionary.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Retrieve and print information about your connector's self-description

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to get your connector self-description.

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

    # Connect to our TSG connector:
    conn = TSGController(
        api_key=config['API_KEY'],
        connector_id=config['CONNECTOR_ID'],
        access_url=config['ACCESS_URL'],
        agent_id=config['AGENT_ID']
    )

    # Get internal connector info (self self-description):
    self_description = conn.get_connector_self_selfdescription()

    print("-" * 79)
    print("> Connector Self Self Description:")
    pprint(self_description.to_dict())
