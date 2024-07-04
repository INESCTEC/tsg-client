"""

Example - Generate a contract that can be used to post artifacts

Last update: 2024-05-25

The following operations are demonstrated:

    1. Generate the contract

Ensure that the required parameters are specified before executing the  request:

    - id: The id of the user (username).
    - new_password: The new secret and secure password.
    - new_roles: The new list of roles this user should have. (optional)
"""


if __name__ == "__main__":
    import uuid
    from tsg_client.utils.contracts import update_and_save_contract

    contract_id = str(uuid.uuid4())
    contract_start = "2024-01-01T00:00:00.000+00:00"
    contract_end = "2024-12-31T00:00:00.000+00:00"

    update_and_save_contract(
        contract_id,
        contract_start,
        contract_end
    )
