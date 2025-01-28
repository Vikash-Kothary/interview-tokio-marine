from typing import Optional

from fastapi import APIRouter, HTTPException, Depends

from tokio_marine.domain.exceptions import PolicyNotFoundException
from tokio_marine.infrastructure.routes.dependencies import get_policy_service

router = APIRouter()

# I am using a query parameter for this example to keep things simple
# I would normally use a separate endpoint.
# NOTE: API versioning and RESTful resources.
# NOTE: Typically would map from domain exceptions to api errors.
# Here I'm mapping to an empty list to be inline with restful standards
@router.get("/api/v1/policies")
def list_policies(policy_id: Optional[str] = None):   
    policy_service = get_policy_service()

    if policy_id is not None:
        try:
            policy = policy_service.get_policy_by_id(policy_id)
            return { 'policies': [policy] }
        except PolicyNotFoundException:
            return { 'policies': [] }

    policies = policy_service.list_policies()
    return { 'policies': policies }
