"""

Example - Get self-descriptions of an external connector

Last update: 2024-02-28

This request retrieves the self-descriptions of connectors registered in the
 metadata broker.

The following operations are demonstrated:

    1. Load environment variables (your connector configs) from a `.env` file.
    2. Establish a connection to your TSG connector.
    3. Retrieve and print information about external connector self-descriptions (registered in the Metadata Broker)

Important:

    - Ensure that the required environment variables (Your Connector `API_KEY`, `CONNECTOR_ID`, `ACCESS_URL` and `AGENT_ID`) are set in the .env file before using this  request.

    - The connector `API_KEY` can be retrieved by loging into the TSG connector UI and navigating to the 'API Keys' tab.

Execute the code below to make a request to the metadata broker


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
        agent_id=config['AGENT_ID'],
        metadata_broker_url=config['METADATA_BROKER_URL']
    )

    # Request data from DS Metadata Broker:
    result = conn.query_metadata_broker()
    pprint(result)

    print("-" * 79)
    print("> Connectors w/ self-descriptions in metadata-broker")
    for k in result:
        print("Connector ID:", k["@id"])
        print("Access URL:", k["ids:hasEndpoint"][0]["ids:accessURL"]["@id"].split('/router')[0])
        print("Agent ID:", k["ids:maintainer"]["@id"])
        print("-")

    print("-" * 79)
    print("> Connectors w/ data apps")
    for k in result:
        try:
            rc = k["ids:resourceCatalog"]
        except KeyError:
            continue
        data_apps = [x["@id"] for x in rc if 'data-app' in x["@id"]]
        if any(data_apps):
            print("Connector:", k["@id"])
            print("Data Apps:", data_apps)
