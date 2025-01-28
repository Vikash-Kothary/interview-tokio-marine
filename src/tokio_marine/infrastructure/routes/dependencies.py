from tokio_marine.application.services import PolicyService
from tokio_marine.infrastructure.repositories import InMemoryPolicyRepository
from tokio_marine.infrastructure.repositories import JsonPolicyRepository
from tokio_marine.infrastructure.repositories import PostgresPolicyRepository

# NOTE: We can switch out the repository
def get_policy_service():
    return PolicyService(InMemoryPolicyRepository())
