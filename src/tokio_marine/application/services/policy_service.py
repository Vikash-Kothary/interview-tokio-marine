from tokio_marine.domain.exceptions import PolicyNotFoundException
from tokio_marine.infrastructure.repositories import PolicyRepository

class PolicyService:
    def __init__(self, repository: PolicyRepository):
        self.repository = repository

    def list_policies(self):
        return self.repository.list_policies()

    def get_policy_by_id(self, policy_id: str):
        policy = self.repository.get_policy_by_id(policy_id)
        if not policy:
            raise PolicyNotFoundException(policy_id)
        return policy
