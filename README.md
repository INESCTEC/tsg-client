<div align="left">
  <img src="/docs/source/_static/logo.png"  align="middle" width="33%" height="auto">
</div>

---

# INESC TEC Client for TNO Security Gateway (TSG) Dataspace Components (TSG-Client)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)]()
[![Status](https://img.shields.io/badge/status-development-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
![CI](https://github.com/CPES-Power-and-Energy-Systems/tsg-client/actions/workflows/publish_docs.yml/badge.svg)
![UnitTEST](https://img.shields.io/badge/unit_testing-passing-brightgreen)

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

This document provides detailed instructions for setting up the INESC TEC Client for TNO Security Gateway (TSG-Client) environment.
Please follow these steps carefully to ensure successful configuration and deployment.

> **_NOTE:_** This library assumes that you have a running instance of the TSG Core Connector and OpenAPI Data APP. For this, please follow the [Official TSG Documentation](https://tno-tsg.gitlab.io/).

> **_WARNING:_** This library is under active development and is not yet recommended for production use at this time.

> **_IMPORTANT:_** This development is an internal initiative from INESC TEC within [ENERSHARE](https://enershare.eu/), and it is not officially maintained/supported by TNO team.

## Documentation & Examples

A detailed documentation is available [here](https://cpes-power-and-energy-systems.github.io/tsg-client/).
Python example scripts (and respective description) are also available in the [examples](examples/) directory of the repository.

## Installation

### Base Requirements

- [Python 3.9+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

### Installation steps

To install the TSG-Client, please follow the steps below:

1. Clone the repository.

```bash
$ git clone https://github.com/CPES-Power-and-Energy-Systems/tsg-client.git
```

2. Assuming you have Poetry [installed](https://python-poetry.org/docs/#installation), run the following command to install the required dependencies:

```bash
$ poetry install
```

3. Activate the virtual environment*:

```bash
$ poetry shell
```

Now you are ready to use the TSG-Client.

> *It's possible to use poetry without virtual environments (although recommended). For more info see Poetry [documentation](https://python-poetry.org/docs/configuration/#virtualenvscreate).

## Adding new dependencies

To add a new dependency to the project, use the following command:

```bash
$ poetry add <package-name>
```

Poetry will automatically update the `pyproject.toml` file and install the new package.

## Usage

To get started, check out the examples in the [examples](./examples) directory. These examples demonstrate how to instanciate the `TSGController` and use the multiple functionalities of TSG Client.

## Contacts:

If you have any questions regarding this project, please contact the following people:

Developers (SW source code / methodology questions):

- **Carolina Catorze:** [carolina.catorze@inesctec.pt](mailto:carolina.catorze@inesctec.pt)
- **Vasco Guedes:** [vasco.r.maia@inesctec.pt](mailto:vasco.r.maia@inesctec.pt)
- **José Luís Rodrigues:** [jose.l.rodrigues@inesctec.pt](mailto:jose.l.rodrigues@inesctec.pt)
- **José Ricardo Andrade:** [jose.r.andrade@inesctec.pt](mailto:jose.r.andrade@inesctec.pt)
