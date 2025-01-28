from enum import Enum
from datetime import date, datetime
from typing import List
from pydantic import BaseModel, Field, computed_field

# TODO: Use Field to add openapi information
# NOTE: Domain modelling should depend on the business domain
# Without knowledge of the business domain, I've just made something up.

class InsuranceType(Enum):
    HEALTH = "HEALTH"
    LIFE = "LIFE"

class State(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Address(BaseModel):
    pass

class Person(BaseModel):
    given_name: str
    middle_names: List[str]
    family_name: str
    address: Address

# I've linked the policy to a product foreign id
# This allows us to model the product schema to include all the details for the product
# NOTE: Without coupling it to the policy!
# TODO: Timezones!

class InsurancePolicy(BaseModel):
    policy_id: str
    insurance_type: InsuranceType
    product_id: str 
    policy_number: float
    start_datetime: datetime
    end_datetime: datetime
    billing_amount: float
    # People
    policy_holder: Person
    beneficiaries: List[Person]
    # Metadata
    created_at: datetime
    created_by: str
    last_modified_at: datetime
    last_modified_by: str

    # This is a derived property
    # NOTE: Trade-off between adding business logic in the 'object'
    # Or in the 'service'
    @property
    @computed_field
    def state(self) -> State:
        if self.start_date <= datetime.now() <= self.end_date:
            return State.ACTIVE
        return State.INACTIVE
