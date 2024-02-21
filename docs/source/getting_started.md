
Getting Started with the TSG Client
====================================

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

Make sure to save the changes after updating the values.

### Examples

Follow the examples provided in the Examples section


## Additional Information

The TSG-Client is a REST API that interacts with the connector of the dataspace of TNO, deployed following a specific tutorial. The available requests are currently being tested in `main.py`. The script demonstrates interactions with TSG OpenApi Data APP and inter-connector API.


