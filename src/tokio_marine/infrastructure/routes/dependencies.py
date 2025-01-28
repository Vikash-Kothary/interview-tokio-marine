from tokio_marine.domain.models import InsurancePolicy
from tokio_marine.application.services import PolicyService
from tokio_marine.infrastructure.repositories import InMemoryPolicyRepository
from tokio_marine.infrastructure.repositories import JsonPolicyRepository
from tokio_marine.infrastructure.repositories import PostgresPolicyRepository

from datetime import datetime

initial_insurance_policy = {
    "policy_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "insurance_type": "HEALTH",
    "product_id": "H123456",
    "policy_number": 1234567890,
    "start_datetime": datetime.fromisoformat("2025-01-01T00:00:00"),
    "end_datetime": datetime.fromisoformat("2026-01-01T00:00:00"),
    "billing_amount": 200.75,
    "policy_holder": {
        "given_name": "Alice",
        "middle_names": [],
        "family_name": "Johnson",
        "date_of_birth": datetime.fromisoformat("1990-05-12"),
        "email": "alice.johnson@example.com",
        "phone_number": "+1-555-234-5678",
        "address": {
            "street": "456 Oak Lane",
            "city": "Greenwood",
            "state": "CA",
            "postal_code": "90210",
            "country": "USA"
        }
    },
    "beneficiaries": [
        {
            "given_name": "Bob",
            "middle_names": [],
            "family_name": "Johnson",
            "date_of_birth": datetime.fromisoformat("2015-09-01"),
            "email": "bob.johnson@example.com",
            "phone_number": "+1-555-678-9101",
            "address": {
                "street": "456 Oak Lane",
                "city": "Greenwood",
                "state": "CA",
                "postal_code": "90210",
                "country": "USA"
            }
        }
    ],
    "created_at": datetime.fromisoformat("2025-01-01T12:00:00"),
    "created_by": "admin_user",
    "last_modified_at": datetime.fromisoformat("2025-01-10T14:30:00"),
    "last_modified_by": "admin_user"
}


# NOTE: We can switch out the repository
def get_policy_service():
    repository = InMemoryPolicyRepository()
    repository.create_policy(InsurancePolicy.model_validate(initial_insurance_policy))
    return PolicyService(repository)
