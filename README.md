# TSG-Client

[![version](https://img.shields.io/badge/version-0.0.1-blue.svg)]()
[![status](https://img.shields.io/badge/status-dev-brightgreen.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)



This document provides detailed instructions for setting up the TSG-Client environment. Please follow these steps carefully to ensure successful configuration and deployment.


## Overview
TSG Client is a Python library for interacting with the TNO Security Gateway (TSG). It provides a simple and easy-to-use interface for tasks such as:

- Connecting to TSG connectors
- Retrieving connector self-descriptions
- Working with catalogs and artifacts
- Requesting and consuming data artifacts
- Knowing what connectors are in the dataspace
- Take advantage of the OpenAPI functionalities


## Installation steps

### Install essential tools


- **Install GIT:**
  - Download and install GIT from [Git Download Page](https://git-scm.com/downloads)

- **Python**: Install Python (tested using Python 3.9)

- **Install Python requirements:**
  - Open a terminal and execute the following command:
    ```bash
    pip install -r requirements.txt
    ```

### Clone the project and setup the environment

Open a terminal and execute the following commands:

```bash
git clone https://gitlab.inesctec.pt/cpes/european-projects/enershare/tsg-client.git
cd tsg-client
```

### OR Install the Library

Open a project and execute the following commands:

```bash
pip install git+https://gitlab.inesctec.pt/cpes/european-projects/enershare/tsg-client.git
```

### Set up environment variables

Create a `.env` file with the following contents:

```bash
cp dotenv .env
```

### Edit the .env file and replace the following placeholders with your specific values:

Open the `.env` file in a text editor and modify the following variables with your actual information:

- **API_KEY**: Replace with your TSG API key.
- **CONNECTOR_ID**: Replace with the connector ID for your TSG instance.
- **ACCESS_URL**: Replace with the access URL for your TSG connector.
- **AGENT_ID**: Replace with the agent ID associated with your TSG connector.

- **EXTERNAL_CONNECTOR_ID**: Replace with the external connector ID.
- **EXTERNAL_ACCESS_URL**: Replace with the access URL for the external connector.
- **EXTERNAL_AGENT_ID**: Replace with the agent ID associated with the external connector.

Make sure to save the changes after updating the values.


## Additional Information

The TSG-Client is a REST API that interacts with the connector of the dataspace of TNO, deployed following a specific tutorial. The available requests are currently being tested in `main.py`. The script demonstrates interactions with TSG OpenApi Data APP and inter-connector API.


## Adding dependencies

To add a new dependency, please add it to the `requirements.in` file and run the following command:

```bash
pip-compile requirements.in
```

This will generate a new `requirements.txt` file with the new dependency added.

## Usage

To use the TSG Client, you first need to create a `TSGController` instance:

```bash
from tsg_client.controllers import TSGController

config = {
    "API_KEY": "<YOUR_API_KEY>",
    "CONNECTOR_ID": "<YOUR_CONNECTOR_ID>",
    "ACCESS_URL": "<YOUR_ACCESS_URL>",
    "AGENT_ID": "<YOUR_AGENT_ID>",
}

conn = TSGController(**config)
```

1. Connect to a TSG connector:

    ```bash
    conn.connect()
    ```

2. Get connector self-description:

    ```bash
    self_description = conn.get_connector_self_selfdescription()
    print(self_description)
    ```

3. Get external connector self-description:

    ```bash
    access_url = "https://<external_connector_url>/selfdescription"
    connector_id = "<external_connector_id>"
    agent_id = "<agent_id>"
    
    description = conn.get_connector_selfdescription(
        access_url=access_url,
        connector_id=connector_id,
        agent_id=agent_id
    )
    print(description)

    ```
4. Work with catalogs and artifacts:

    ```bash
    # Parse resource catalogs
    catalogs = conn.parse_resource_catalogs(self_description=description)
    print(catalogs)
    
    # Parse catalog artifacts
    artifacts = conn.parse_catalog_artifacts(self_description=description)
    print(artifacts)
    ```

5. Request and consume data artifacts:
    ```bash
    # Request contract agreement
    artifact_id = artifacts[0]['id']
    artifact_access_url = artifacts[0]['access_url']
    artifact_contract_offer = artifacts[0]['contract_offer']
    
    contract_agreement_id = conn.request_agreement(
        connector_id=external_connector['CONNECTOR_ID'],
        artifact_access_url=artifact_access_url,
        artifact_contract_offer=artifact_contract_offer
    )
    print(contract_agreement_id)
    
    # Request data artifact
    artifact_path = "<artifact_path>"
    artifact_description = "<description>"
    artifact_title = "<title>"
    data_artifact = conn.publish_data_artifact(artifact=artifact_path,
                                               contract_offer=artifacts[0]['contract_offer'],
                                               description=artifact_description,
                                               title=artifact_title)
    
    print(data_artifact)
    ```

6. Request the OpenAPI specifications from an external connector:
    ```bash
    open_api_specs = conn.get_openapi_specs(description, "0.9.2")
    print(open_api_specs)
    ```

7. Execute an request through the OpenAPI to an external connector:
Note: To enable this functionality, it is required that the OpenAPI is deployed on the used connector.
    ```bash
    openapi_request = conn.openapi_request(
        "https://backend-01.enershare.inesctec.pt/router",
        "urn:playground:tsg:connectors:cpes01",
        "1.0.0",
        "test-service")
    print(openapi_request)
    ```

### Contact Information

If you encounter any issues or have questions, please feel free to reach out to the support team:

- **Carolina Catorze:** [carolina.catorze@inesctec.pt](mailto:carolina.catorze@inesctec.pt)
- **Vasco Maia:** [vasco.r.maia@inesctec.pt](mailto:vasco.r.maia@inesctec.pt)
- **José Ricardo Andrade:** [jose.r.andrade@inesctec.pt](mailto:jose.r.andrade@inesctec.pt)

