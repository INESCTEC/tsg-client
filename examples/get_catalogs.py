"""

Example: Get the catalogs from a connector

Last update: 2024-05-16

This  request retrieves and prints information about
the catalogs of your connector.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Retrieve and print information about the catalogs

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and
    `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to get your connector catalogs list.

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

    # Get connector info (catalogs):
    catalogs = conn.catalogs()

    pprint(catalogs)
