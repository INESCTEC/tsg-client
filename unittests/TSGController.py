# flake8: noqa
import unittest

from dotenv import dotenv_values
from tsg_client.controllers import TSGController
from tsg_client.controllers.SelfDescription import SelfDescription


class TestTSGController(unittest.TestCase):

    def test_parse_catalog_artifacts(self):
        raw_self_description = {
            "@context": {
                "ids": "https://w3id.org/idsa/core/",
                "idsc": "https://w3id.org/idsa/code/"
            },
            "@type": "ids:TrustedConnector",
            "@id": "urn:ids:enershare:connectors:connector-02",
            "ids:publicKey": {
                "@type": "ids:PublicKey",
                "@id": "https://w3id.org/idsa/autogen/publicKey/4162da36-7d86-4d10-b294-89578561720a",
                "ids:keyType": {
                    "@id": "https://w3id.org/idsa/code/RSA"
                },
                "ids:keyValue": "MIIDqjCCApKgAwIBAgIEdoDqFTANBgkqhkiG9w0BAQsFADB"
                                "/MQswCQYDVQQGEwJOTDESMBAGA1UECBMJR3JvbmluZ2VuMRIwEAYDVQQHEwlHcm9uaW5nZW4xDDAKBgNVBAoTA"
                                "1ROTzEYMBYGA1UECxMPRGF0YSBFY29zeXN0ZW1zMSAwHgYDVQQDExdFbmVyc2hhcmUgRGV2aWNlIFN1YiBDQTA"
                                "eFw0yNDAyMDgxNDEyMDVaFw0yNjAyMDgxNDEyMDVaMFMxCzAJBgNVBAYTAlBUMQ4wDAYDVQQIDAVQb3J0bzEOM"
                                "AwGA1UEBwwFUG9ydG8xETAPBgNVBAoMCElORVNDVEVDMREwDwYDVQQLDAhJTkVTQ1RFQzCCASIwDQYJKoZIhvc"
                                "NAQEBBQADggEPADCCAQoCggEBAKjFRmA4XgIF8k6ijpZIQPelhjoxrZmtoPoP5lY51NY2SqKEYLDYjMzDGiVK0"
                                "BhOJHhgCnGXhPDHIJVjSkky/Zs8xrEzfcQGHLT0SMKZ4hS7T0C0EJ+6M/NkwwfvH2rhb488vle0R9BqgGM9GTO"
                                "N4BSY8aG2tx/skEOMXSkA7simennuOZBYu6tEBQd9+XrINT89P2HqS4QOOxaW/2fJyxBdj4NzfNZD4M5vZ2n+6"
                                "qHn7ouuTmGobo8WwPicnVT6HA2v2y3ICFnZh/AZYnWTcA0hvLiTzh41M23PzhOMhYH5ngXmN84fZtLSrW9EUyh"
                                "aHJAjqcNVm1j3H6CnonbO7hECAwEAAaNaMFgwCQYDVR0TBAIwADALBgNVHQ8EBAMCBaAwHQYDVR0OBBYEFOYRf"
                                "TIjJ0JT1hZbL5gBOZCv37OCMB8GA1UdIwQYMBaAFEfPI4HNNMKRgU74b8oamoo/h/aNMA0GCSqGSIb3DQEBCwU"
                                "AA4IBAQA2Rip2LoOueo6++v+3a09t2qFih1jNl06oDN3NnselO/ZhRLsZ+ZjNC5D5YrxHdVhdI4hmb5ja3Eigh"
                                "WLsEYmoESaDhTAtDrbr8uyPz4+kDfDvkmKEiONY10ANvOLk6mjZKKjkF2e7uf4NKi184gsZK6ej/vjwuRieIQ"
                                "wjUnkL7XjEwezoj28Od+059meJhgMM8KlfUv0dxUjFuA1VWjoDaAEPve+h+6/7zhAKTSXA2YgeTu7G/9QsC2q"
                                "sJ5vqBH2wLoJF3dOW9H0i5dn604cL2saRxkUz0MIPVO76lO8e4GqYeG4BECcym6BCpu20RTpSsoEFBcr5Y45Gg"
                                "oJYCVOw"
            },
            "ids:description": [{
                "@value": "Enershare Local Demo Connector",
                "@language": "en"
            }],
            "ids:title": [{
                "@value": "Enershare Local Demo Connector",
                "@language": "en"
            }],
            "ids:resourceCatalog": [{
                "@type": "ids:ResourceCatalog",
                "@id": "urn:ids:enershare:connectors:connector-02:data-app",
                "ids:offeredResource": [{
                    "@type": "ids:Resource",
                    "@id": "https://w3id.org/idsa/autogen/resource/07426511-0aed-4736-b1c6-baa6a0e22f98",
                    "ids:title": [{
                        "@value": "Consumer Agent",
                        "@language": "en"
                    }],
                    "ids:sovereign": {
                        "@id": "urn:ids:enershare:connectors:connector-02:Agent"
                    }
                }]
            }, {
                "@type": "ids:ResourceCatalog",
                "@id": "urn:ids:enershare:connectors:connector-02:resources",
                "ids:offeredResource": [{
                    "@type": "ids:DataResource",
                    "@id": "urn:ids:enershare:connectors:connector-02:resources:8436fba4-e2d2-4419-b5f9-4714326f63c4",
                    "ids:keyword": [{
                        "@value": "description",
                        "@language": "en"
                    }],
                    "ids:language": [{
                        "@id": "https://w3id.org/idsa/code/EN"
                    }],
                    "ids:version": "1",
                    "ids:description": [{
                        "@value": "description",
                        "@language": "en"
                    }],
                    "ids:contractOffer": [{
                        "@type": "ids:ContractOffer",
                        "@id": "https://w3id.org/idsa/autogen/contractOffer/85d11dd0-7402-4503-ae16-6b29c5e3e0d7",
                        "ids:permission": [{
                            "@type": "ids:Permission",
                            "@id": "https://w3id.org/idsa/autogen/permission/5c469d0a-0455-43cf-a714-825c0d9e967d",
                            "ids:target": {
                                "@id": "urn:ids:enershare:connectors:connector-02:artifacts:61bb4fd2-896e-44bb-9326"
                                       "-d0944c266b01"
                            },
                            "ids:action": [{
                                "@id": "https://w3id.org/idsa/code/READ"
                            }, {
                                "@id": "https://w3id.org/idsa/code/USE"
                            }]
                        }],
                        "ids:contractStart": {
                            "@value": "2024-01-01T00:00:00.000Z",
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                        },
                        "ids:contractEnd": {
                            "@value": "2024-12-31T00:00:00.000Z",
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                        }
                    }],
                    "ids:title": [{
                        "@value": "test 1",
                        "@language": "en"
                    }],
                    "ids:representation": [{
                        "@type": "ids:Representation",
                        "@id": "https://w3id.org/idsa/autogen/representation/3b0b9247-cac3-4205-9295-bb7fc5963781",
                        "ids:mediaType": {
                            "@type": "ids:IANAMediaType",
                            "@id": "https://www.iana.org/assignments/media-types/application/pdf",
                            "ids:filenameExtension": "pdf"
                        },
                        "ids:instance": [{
                            "@type": "ids:Artifact",
                            "@id": "urn:ids:enershare:connectors:connector-02:artifacts:61bb4fd2-896e-44bb-9326"
                                   "-d0944c266b01",
                            "ids:byteSize": 3028,
                            "ids:fileName": "!.pdf"
                        }]
                    }],
                    "ids:resourceEndpoint": [{
                        "@type": "ids:ConnectorEndpoint",
                        "@id": "https://w3id.org/idsa/autogen/connectorEndpoint/8419d394-109a-4530-a2ae-f71a34a60a4f",
                        "ids:path": "/artifacts/urn%3Aids%3Aenershare%3Aconnectors%3Aconnector-02%3Aresources%3A8436fba"
                                    "4-e2d2-4419-b5f9-4714326f63c4",
                        "ids:accessURL": {
                            "@id": "https://connector-02.enershare.inesctec.pt/router"
                        }
                    }],
                    "ids:created": {
                        "@value": "2024-03-19T21:47:18.009Z",
                        "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                    },
                    "ids:standardLicense": {
                        "@id": "http://www.apache.org/licenses/LICENSE-2.0"
                    },
                    "ids:publisher": {
                        "@id": "urn:ids:enershare:participants:VascoGuedes"
                    },
                    "ids:sovereign": {
                        "@id": "urn:ids:enershare:participants:VascoGuedes"
                    }
                }, {
                    "@type": "ids:DataResource",
                    "@id": "urn:ids:enershare:connectors:connector-02:resources:6fa1d16d-8f86-412b-a366-12950e3dcfa7",
                    "ids:keyword": [{
                        "@value": "description",
                        "@language": "en"
                    }],
                    "ids:language": [{
                        "@id": "https://w3id.org/idsa/code/EN"
                    }],
                    "ids:version": "1",
                    "ids:description": [{
                        "@value": "description",
                        "@language": "en"
                    }],
                    "ids:contractOffer": [{
                        "@type": "ids:ContractOffer",
                        "@id": "https://w3id.org/idsa/autogen/contractOffer/038d749e-34e6-4f49-84c5-de9f46acdf2c",
                        "ids:permission": [{
                            "@type": "ids:Permission",
                            "@id": "https://w3id.org/idsa/autogen/permission/d8607d1d-8fc1-487f-af84-3c7d5efc3f25",
                            "ids:target": {
                                "@id": "urn:ids:enershare:connectors:connector-02:artifacts:302e1c0b-b18c-4e20-ad3c"
                                       "-abc3606d0801"
                            },
                            "ids:action": [{
                                "@id": "https://w3id.org/idsa/code/READ"
                            }, {
                                "@id": "https://w3id.org/idsa/code/USE"
                            }]
                        }],
                        "ids:contractStart": {
                            "@value": "2024-01-01T00:00:00.000Z",
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                        },
                        "ids:contractEnd": {
                            "@value": "2024-12-31T00:00:00.000Z",
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                        }
                    }],
                    "ids:title": [{
                        "@value": "test 2",
                        "@language": "en"
                    }],
                    "ids:representation": [{
                        "@type": "ids:Representation",
                        "@id": "https://w3id.org/idsa/autogen/representation/4dcfdc3d-df36-43b8-8e5d-8dcff3bc8ee3",
                        "ids:mediaType": {
                            "@type": "ids:IANAMediaType",
                            "@id": "https://www.iana.org/assignments/media-types/application/pdf",
                            "ids:filenameExtension": "pdf"
                        },
                        "ids:instance": [{
                            "@type": "ids:Artifact",
                            "@id": "urn:ids:enershare:connectors:connector-02:artifacts:302e1c0b-b18c-4e20-ad3c"
                                   "-abc3606d0801",
                            "ids:byteSize": 3028,
                            "ids:fileName": "!.pdf"
                        }]
                    }],
                    "ids:resourceEndpoint": [{
                        "@type": "ids:ConnectorEndpoint",
                        "@id": "https://w3id.org/idsa/autogen/connectorEndpoint/515fc1ba-9a38-490b-9faf-8300bd551ed6",
                        "ids:path": "/artifacts/urn%3Aids%3Aenershare%3Aconnectors%3Aconnector-02%3Aresources"
                                    "%3A6fa1d16d-8f86-412b-a366-12950e3dcfa7",
                        "ids:accessURL": {
                            "@id": "https://connector-02.enershare.inesctec.pt/router"
                        }
                    }],
                    "ids:created": {
                        "@value": "2024-03-19T21:47:30.109Z",
                        "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                    },
                    "ids:standardLicense": {
                        "@id": "http://www.apache.org/licenses/LICENSE-2.0"
                    },
                    "ids:publisher": {
                        "@id": "urn:ids:enershare:participants:VascoGuedes"
                    },
                    "ids:sovereign": {
                        "@id": "urn:ids:enershare:participants:VascoGuedes"
                    }
                }, {
                    "@type": "ids:DataResource",
                    "@id": "urn:ids:enershare:connectors:connector-02:resources:0631c904-94b8-43fc-84ad-2185f37a6d25",
                    "ids:keyword": [{
                        "@value": "description",
                        "@language": "en"
                    }],
                    "ids:language": [{
                        "@id": "https://w3id.org/idsa/code/EN"
                    }],
                    "ids:version": "1",
                    "ids:description": [{
                        "@value": "description",
                        "@language": "en"
                    }],
                    "ids:contractOffer": [{
                        "@type": "ids:ContractOffer",
                        "@id": "https://w3id.org/idsa/autogen/contractOffer/bc1921f9-275c-462d-add1-bfa2fc209874",
                        "ids:permission": [{
                            "@type": "ids:Permission",
                            "@id": "https://w3id.org/idsa/autogen/permission/96aff7c9-7c66-455c-8d5f-fb753e2b26e0",
                            "ids:target": {
                                "@id": "urn:ids:enershare:connectors:connector-02:artifacts:22e87052-c02a-4efc-b9a3"
                                       "-cc10a70184af"
                            },
                            "ids:action": [{
                                "@id": "https://w3id.org/idsa/code/READ"
                            }, {
                                "@id": "https://w3id.org/idsa/code/USE"
                            }]
                        }],
                        "ids:contractStart": {
                            "@value": "2024-01-01T00:00:00.000Z",
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                        },
                        "ids:contractEnd": {
                            "@value": "2024-12-31T00:00:00.000Z",
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                        }
                    }],
                    "ids:title": [{
                        "@value": "test 3",
                        "@language": "en"
                    }],
                    "ids:representation": [{
                        "@type": "ids:Representation",
                        "@id": "https://w3id.org/idsa/autogen/representation/84134f40-e1a4-4c2c-85b6-0c913435d5a8",
                        "ids:mediaType": {
                            "@type": "ids:IANAMediaType",
                            "@id": "https://www.iana.org/assignments/media-types/application/pdf",
                            "ids:filenameExtension": "pdf"
                        },
                        "ids:instance": [{
                            "@type": "ids:Artifact",
                            "@id": "urn:ids:enershare:connectors:connector-02:artifacts:22e87052-c02a-4efc-b9a3"
                                   "-cc10a70184af",
                            "ids:byteSize": 3028,
                            "ids:fileName": "!.pdf"
                        }]
                    }],
                    "ids:resourceEndpoint": [{
                        "@type": "ids:ConnectorEndpoint",
                        "@id": "https://w3id.org/idsa/autogen/connectorEndpoint/1d99c1ae-e197-4acc-a85a-242ad4d92ade",
                        "ids:path": "/artifacts/urn%3Aids%3Aenershare%3Aconnectors%3Aconnector-02%3Aresources"
                                    "%3A0631c904-94b8-43fc-84ad-2185f37a6d25",
                        "ids:accessURL": {
                            "@id": "https://connector-02.enershare.inesctec.pt/router"
                        }
                    }],
                    "ids:created": {
                        "@value": "2024-03-19T21:47:41.819Z",
                        "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
                    },
                    "ids:standardLicense": {
                        "@id": "http://www.apache.org/licenses/LICENSE-2.0"
                    },
                    "ids:publisher": {
                        "@id": "urn:ids:enershare:participants:VascoGuedes"
                    },
                    "ids:sovereign": {
                        "@id": "urn:ids:enershare:participants:VascoGuedes"
                    }
                }]
            }],
            "ids:securityProfile": {
                "@id": "https://w3id.org/idsa/code/TRUST_SECURITY_PROFILE"
            },
            "ids:hasEndpoint": [{
                "@type": "ids:ConnectorEndpoint",
                "@id": "https://w3id.org/idsa/autogen/connectorEndpoint/eea1bc85-e4e2-44a6-bb79-df251a2b5588",
                "ids:accessURL": {
                    "@id": "https://connector-02.enershare.inesctec.pt/router"
                }
            }],
            "ids:hasDefaultEndpoint": {
                "@type": "ids:ConnectorEndpoint",
                "@id": "https://w3id.org/idsa/autogen/connectorEndpoint/eea1bc85-e4e2-44a6-bb79-df251a2b5588",
                "ids:accessURL": {
                    "@id": "https://connector-02.enershare.inesctec.pt/router"
                }
            },
            "ids:maintainer": {
                "@id": "urn:ids:enershare:participants:VascoGuedes"
            },
            "ids:curator": {
                "@id": "urn:ids:enershare:participants:VascoGuedes"
            },
            "ids:inboundModelVersion": ["4.0.0", "4.1.0", "4.1.2", "4.2.0", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5",
                                        "4.2.6", "4.2.7"],
            "ids:outboundModelVersion": "4.2.7"
        }

        self_description = SelfDescription.from_dict(raw_self_description)
        artifacts = TSGController.parse_catalog_artifacts(self_description)

        expected_parsing = [
            {
                'id': 'urn:ids:enershare:connectors:connector-02:artifacts:61bb4fd2-896e-44bb-9326-d0944c266b01',
                'contract_offer': "{'@type': 'ids:ContractOffer', '@id': "
                                  "'https://w3id.org/idsa/autogen/contractOffer/85d11dd0-7402-4503-ae16-6b29c5e3e0d7"
                                  "', 'ids:permission': [{'@type': 'ids:Permission', "
                                  "'@id': 'https://w3id.org/idsa/autogen/permission/5c469d0a-0455-43cf-a714"
                                  "-825c0d9e967d', 'ids:target': {'@id': "
                                  "'urn:ids:enershare:connectors:connector-02:artifacts:61bb4fd2-896e-44bb-9326"
                                  "-d0944c266b01'}, 'ids:action': [{'@id': 'https://w3id.org/idsa/code/READ'}, "
                                  "{'@id': 'https://w3id.org/idsa/code/USE'}]}], 'ids:contractStart': {'@value': "
                                  "'2024-01-01T00:00:00.000Z', '@type': "
                                  "'http://www.w3.org/2001/XMLSchema#dateTimeStamp'}, 'ids:contractEnd': {'@value': "
                                  "'2024-12-31T00:00:00.000Z', '@type': "
                                  "'http://www.w3.org/2001/XMLSchema#dateTimeStamp'}}",
                'artifact_created': '2024-03-19T21:47:18.009Z',
                'access_url': 'https://connector-02.enershare.inesctec.pt/router/artifacts/urn%3Aids%3Aenershare'
                              '%3Aconnectors%3Aconnector-02%3Aresources%3A8436fba4-e2d2-4419-b5f9-4714326f63c4',
                'title': 'test 1',
                'description': 'description'
            },
            {
                'id': 'urn:ids:enershare:connectors:connector-02:artifacts:302e1c0b-b18c-4e20-ad3c-abc3606d0801',
                'contract_offer': "{'@type': 'ids:ContractOffer', '@id': "
                                  "'https://w3id.org/idsa/autogen/contractOffer/038d749e-34e6-4f49-84c5-de9f46acdf2c"
                                  "', 'ids:permission': [{'@type': 'ids:Permission', "
                                  "'@id': 'https://w3id.org/idsa/autogen/permission/d8607d1d-8fc1-487f-af84"
                                  "-3c7d5efc3f25', 'ids:target': {'@id': "
                                  "'urn:ids:enershare:connectors:connector-02:artifacts:302e1c0b-b18c-4e20-ad3c"
                                  "-abc3606d0801'}, 'ids:action': [{'@id': 'https://w3id.org/idsa/code/READ'}, "
                                  "{'@id': 'https://w3id.org/idsa/code/USE'}]}], 'ids:contractStart': {'@value': "
                                  "'2024-01-01T00:00:00.000Z', '@type': "
                                  "'http://www.w3.org/2001/XMLSchema#dateTimeStamp'}, 'ids:contractEnd': {'@value': "
                                  "'2024-12-31T00:00:00.000Z', '@type': "
                                  "'http://www.w3.org/2001/XMLSchema#dateTimeStamp'}}",
                'artifact_created': '2024-03-19T21:47:30.109Z',
                'access_url': 'https://connector-02.enershare.inesctec.pt/router/artifacts/urn%3Aids%3Aenershare'
                              '%3Aconnectors%3Aconnector-02%3Aresources%3A6fa1d16d-8f86-412b-a366-12950e3dcfa7',
                'title': 'test 2',
                'description': 'description'
            },
            {
                'id': 'urn:ids:enershare:connectors:connector-02:artifacts:22e87052-c02a-4efc-b9a3-cc10a70184af',
                'contract_offer': "{'@type': 'ids:ContractOffer', '@id': "
                                  "'https://w3id.org/idsa/autogen/contractOffer/bc1921f9-275c-462d-add1-bfa2fc209874"
                                  "', 'ids:permission': [{'@type': 'ids:Permission', "
                                  "'@id': 'https://w3id.org/idsa/autogen/permission/96aff7c9-7c66-455c-8d5f"
                                  "-fb753e2b26e0', 'ids:target': {'@id': "
                                  "'urn:ids:enershare:connectors:connector-02:artifacts:22e87052-c02a-4efc-b9a3"
                                  "-cc10a70184af'}, 'ids:action': [{'@id': 'https://w3id.org/idsa/code/READ'}, "
                                  "{'@id': 'https://w3id.org/idsa/code/USE'}]}], 'ids:contractStart': {'@value': "
                                  "'2024-01-01T00:00:00.000Z', '@type': "
                                  "'http://www.w3.org/2001/XMLSchema#dateTimeStamp'}, 'ids:contractEnd': {'@value': "
                                  "'2024-12-31T00:00:00.000Z', '@type': "
                                  "'http://www.w3.org/2001/XMLSchema#dateTimeStamp'}}",
                'artifact_created': '2024-03-19T21:47:41.819Z',
                'access_url': 'https://connector-02.enershare.inesctec.pt/router/artifacts/urn%3Aids%3Aenershare'
                              '%3Aconnectors%3Aconnector-02%3Aresources%3A0631c904-94b8-43fc-84ad-2185f37a6d25',
                'title': 'test 3',
                'description': 'description'
            }
        ]

        self.assertEqual(len(artifacts), 3)

        for expected_item, actual_item in zip(expected_parsing, artifacts):
            self.assertDictEqual(expected_item, actual_item)


# Run tests
if __name__ == '__main__':

    config = dotenv_values('.env')

    unittest.main()
