
Getting Started with the TSG Client
====================================

## Overview

TSG Client is a Python library for interacting with the TNO Security Gateway (TSG). 
It is current version, it is a simple REST API client that interacts with [TSG Core Connector APIs](https://tno-tsg.gitlab.io/docs/core-container/api/) and [TSG OpenAPI Data APP](https://gitlab.com/tno-tsg/data-apps/openapi).
It provides a simple and easy-to-use interface for tasks such as:

- Connecting to a TSG core container (via API KEY)
- Retrieving connector self-descriptions
- Parsing / filtering connector catalogs and artifacts, retrieved from self-descriptions
- Requesting and consuming data artifacts (via dataspace)
- Queries to the dataspace Metadata Broker to list registered connectors and respective self-descriptions
- Perform requests via OpenAPI Data APP

> **_WARNING:_** This library is under active development and is not yet recommended for production use at this time.

> **_IMPORTANT:_** This development is an internal initiative from INESC TEC within [ENERSHARE](https://enershare.eu/), and it is not officially maintained/supported by TNO team.


## Installation steps

### Install essential tools

- **OS:** Windows, Linux, macOS

- **Install GIT:**
  - Download and install GIT from [Git Download Page](https://git-scm.com/downloads)

- **Python**: Install Python (version 3.9+)



#### Installing as a package

Although the `tsg-client` is not yet published on public Python repositories of software (e.g., PyPI), you can install it (as a package) by directly referencing this repository URL. 

You can use the command below to install it directly using pip.

```bash
pip install git+https://github.com/CPES-Power-and-Energy-Systems/tsg-client.git
```

Do not forget that you will need to set up some environment variables to use this library. You can find mode details on the [Set up environment variables](#set-up-environment-variables) section.


#### Cloning and local installation

If you want to modify the source code of this library, it is recommended to clone and then use [Poetry](https://python-poetry.org) to create a virtual environment to install the library dependencies and do any modifications needed.

To do this, please follow the steps below:


1. Clone the repository.

```bash
git clone https://github.com/CPES-Power-and-Energy-Systems/tsg-client.git
```

2. Assuming you have Poetry [installed](https://python-poetry.org/docs/#installation), run the following command to install the required dependencies:

```bash
poetry install
```

3. Activate the virtual environment*:

```bash
poetry shell
```

Now you are ready to use the TSG-Client.

> *It's possible to use poetry without virtual environments (although recommended). For more info see Poetry [documentation](https://python-poetry.org/docs/configuration/#virtualenvscreate).


Once you install the library, you'll be able to use the TSG-Client in your Python projects by just importing it (see basic example below):

```python
from tsg_client import TSGController

# Set up the TSG connector:
conn = TSGController(
    api_key="<your-api-key>",
    connector_id="<your-connector-id>",
    access_url="<your-access-url>",
    agent_id="<your-agent-id>",
    metadata_broker_url="<your-dataspace-metadata-broker-url>"  # this one is optional
)

# Retrieve the connector self-description:
self_description = conn.get_connector_self_description()
print(self_description)

# List self-description of other connectors in the dataspace:
# Request data from DS Metadata Broker:
result = conn.query_metadata_broker()
print(result)
```

### Set up environment variables

Ideally, you should set up the environment variables to avoid hardcoding the API key and other sensitive information in your code.
We have a `dotenv` file in the project that may work as an example for you to create your `.env` file. Start by copying that file:

```bash
cp dotenv .env
```

### Edit the .env file and replace the following placeholders with your specific values:

Open the `.env` file in a text editor and modify the following variables with your actual information:

- **API_KEY**: Replace with your TSG API key.
- **CONNECTOR_ID**: Replace with the connector ID for your TSG instance.
- **ACCESS_URL**: Replace with the access URL for your TSG connector.
- **AGENT_ID**: Replace with the agent ID associated with your TSG connector.
- **METADATA_BROKER_URL**: Replace with the URL of the dataspace metadata broker (optional, just in case you will need to query the metadata broker)

Make sure to save the changes after updating the values.

### Examples

Follow the examples provided in the [Examples](examples) section.
