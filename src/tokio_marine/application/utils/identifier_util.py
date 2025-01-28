import uuid

# NOTE: Domain specific adapter functions.
# Abstracts away the implementation details

def create_new_id():
    return str(uuid.uuid4())