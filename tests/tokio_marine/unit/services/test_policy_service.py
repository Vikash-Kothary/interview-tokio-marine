from tokio_marine.infrastructure.repositories import JsonPolicyRepository
from tokio_marine.application.services import PolicyService

# NOTE: Test business logic to boundary contexts i.e. repositories.
# NOTE: Different repository to allow easier testing.

def test_list_policies_when_repository_is_empty():
    expected = 0

    mock_policy_repository = JsonPolicyRepository('tests/tokio_marine/unit/services/resources/empty.json')
    policy_service = PolicyService(mock_policy_repository)

    policies = policy_service.list_policies()
    actual = len(policies)

    assert actual == expected

def test_list_policies_when_repository_is_not_empty():
    expected = 1

    mock_policy_repository = JsonPolicyRepository('tests/tokio_marine/unit/services/resources/one.json')
    policy_service = PolicyService(mock_policy_repository)

    policies = policy_service.list_policies()
    actual = len(policies)

    assert actual == expected

