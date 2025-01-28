
class DomainError(Exception):
    pass

# NOTE: Domain specific error cases

class PolicyNotFoundException(NotImplementedError):
    def __init__(self, policy_id: str):
        super().__init__(f'{policy_id=} not found')

class NotImplementedException(NotImplementedError):
    pass