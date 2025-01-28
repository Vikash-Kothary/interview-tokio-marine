from typing import List, Optional
from abc import ABC, abstractmethod

from tokio_marine.domain.models import InsurancePolicy
from tokio_marine.domain.exceptions import NotImplementedException

# Base Service Interface
class PolicyService(ABC):
    @abstractmethod
    def list_policies(self) -> List[InsurancePolicy]:
        raise NotImplementedException()
    
    @abstractmethod
    def get_policy_by_id(self, policy_id: str) -> Optional[InsurancePolicy]:
        raise NotImplementedException()

