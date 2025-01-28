
class DomainError(Exception):
    pass

class PolicyNotFoundException(NotImplementedError):
    def __init__(policy_id: str):
        super().__init__(f'{policy_id=} not found')

class NotImplementedException(NotImplementedError):
    pass