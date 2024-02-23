<div align="center">
  <img src="/docs/source/_static/logo.png"  align="middle">
</div>

-----------------------------------------------------
# INESC TEC Client for TNO Security Gateway (TSG) Dataspace Components (TSG-Client)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)]()
[![Status](https://img.shields.io/badge/status-development-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
-----------------------------------------------------

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

###  Base Requirements

* [Python 3.9+](https://www.python.org/downloads/)

### Installation steps

To install the TSG-Client, please follow the steps below:

  1. Clone the repository.

```bash
$ git clone https://github.com/CPES-Power-and-Energy-Systems/tsg-client.git
```

  4. Run the following command to install the package:

```bash
$ python setup.py install
```

## Adding new dependencies

In case of new developments, if you plan to a add a new dependency, please add it to the `requirements.in` file and run the following command:

```bash
pip-compile requirements.in
```

This will generate a new `requirements.txt` file with the new dependency added.

## Usage
To get started, check out the examples in the [examples](./examples) directory. These examples demonstrate how to instanciate the `TSGController` and use the multiple functionalities of TSG Client.

## Contacts:

If you have any questions regarding this project, please contact the following people:

Developers (SW source code / methodology questions):
- **Carolina Catorze:** [carolina.catorze@inesctec.pt](mailto:carolina.catorze@inesctec.pt)
- **Vasco Guedes:** [vasco.r.maia@inesctec.pt](mailto:vasco.r.maia@inesctec.pt)
- **José Luís Rodrigues:** [jose.l.rodrigues@.inesctec.pt](mailto:jose.l.rodrigues@.inesctec.pt)
- **José Ricardo Andrade:** [jose.r.andrade@inesctec.pt](mailto:jose.r.andrade@inesctec.pt)

