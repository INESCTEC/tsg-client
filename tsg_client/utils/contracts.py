import json
import os

def update_and_save_contract(contract_id, contract_start, contract_end):
    
    contract_template = {
      "@context" : {
        "ids" : "https://w3id.org/idsa/core/",
        "idsc" : "https://w3id.org/idsa/code/"
      },
      "@type" : "ids:ContractOffer",
      "@id" : f"https://w3id.org/idsa/autogen/contractOffer/{contract_id}",
      "ids:permission" : [ {
        "@type" : "ids:Permission",
        "@id" : "https://w3id.org/idsa/autogen/permission/15f85a6b-f921-47fd-b541-3f8367998048",
        "ids:action" : [ {
          "@id" : "https://w3id.org/idsa/code/USE"
        }, {
          "@id" : "https://w3id.org/idsa/code/READ"
        } ]
      } ],
      "ids:contractStart" : {
        "@value" : contract_start,
        "@type" : "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
      },
      "ids:contractEnd" : {
        "@value" : contract_end,
        "@type" : "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
      }
    }

    # Convert dictionary to JSON string
    contract_json = json.dumps(contract_template, indent=2)

    # Define the path to save the contract
    save_path = os.path.join("docs", "contracts")

    # Ensure the directory exists
    os.makedirs(save_path, exist_ok=True)

    # Define the filename
    filename = f"contract_{contract_id}.json"

    # Write the JSON to a file
    with open(os.path.join(save_path, filename), "w") as file:
        file.write(contract_json)