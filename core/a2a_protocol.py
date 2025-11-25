import uuid, time
def make_message(from_id: str, to_id: str, mtype: str, payload: dict, meta: dict=None):
    return {
        'message_id': str(uuid.uuid4()),
        'trace_id': str(uuid.uuid4()),
        'from': from_id,
        'to': to_id,
        'type': mtype,
        'payload': payload,
        'timestamp': time.time(),
        'meta': meta or {}
    }
