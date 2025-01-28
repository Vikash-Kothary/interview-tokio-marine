from typing import Optional

from fastapi import APIRouter, HTTPException, Depends

from tokio_marine.domain.exceptions import PolicyNotFoundException
from tokio_marine.infrastructure.routes.dependencies import get_policy_service

router = APIRouter()

# I am using a query parameter for this example to keep things simple
# I would normally use a separate endpoint.
# NOTE: API versioning and RESTful resources.
# NOTE: Mapping from domain exceptions to api errors.
@router.get("/api/v1/policies")
def list_policies(policy_id: Optional[str] = None):   
    policy_service = get_policy_service()

    if policy_id is not None:
        try:
            policy = policy_service.get_policy_by_id(policy_id)
            return { 'policies': [policy] }
        except PolicyNotFoundException:
            raise HTTPException(status_code=404)

    policies = policy_service.list_policies()
    return { 'policies': policies }
