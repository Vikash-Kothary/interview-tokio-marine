
from typing import List, Optional


from tokio_marine.domain.models import InsurancePolicy
from tokio_marine.domain.repositories import PolicyRepository
from tokio_marine.domain.exceptions import NotImplementedException
from tokio_marine.application.utils import json_util


class InMemoryPolicyRepository(PolicyRepository):
    def __init__(self):
        self.policies = {}

    def list_policies(self) -> List[InsurancePolicy]:
        return list(self.policies.values())

    def create_policy(self, policy: InsurancePolicy):
        self.policies[policy.policy_id] = policy

    def get_policy_by_id(self, policy_id: str) -> Optional[InsurancePolicy]:
        return self.policies.get(policy_id)


class JsonPolicyRepository(PolicyRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        policies = json_util.load_json(self.file_path)
        
        if policies is None:
            self.policies = {}
        else:
            self.policies = {p["policy_id"]: InsurancePolicy(**p) for p in policies.values()}

    def list_policies(self) -> List[InsurancePolicy]:
        return list(self.policies.values())

    def create_policy(self, policy: InsurancePolicy):
        self.policies[policy.policy_id] = policy
        json_util.save_json(self.file_path, [p.dict() for p in self.policies.values()])

    def get_policy_by_id(self, policy_id: str) -> Optional[InsurancePolicy]:
        return self.policies.get(policy_id)


class PostgresPolicyRepository(PolicyRepository):
    def __init__(self):
        raise NotImplementedException()

    def list_policies(self) -> List[InsurancePolicy]:
        raise NotImplementedException()

    def create_policy(self, policy: InsurancePolicy):
        raise NotImplementedException()

    def get_policy_by_id(self, policy_id: str) -> Optional[InsurancePolicy]:
        raise NotImplementedException()

