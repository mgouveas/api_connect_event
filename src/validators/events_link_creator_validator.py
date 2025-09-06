from cerberus import Validator

def events_link_creator_validator(request: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "event_id": {"type": "integer", "required": True, "empty": False},
                "subscriber_id": {"type": "integer", "required": True, "empty": False},
            }
        }
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise Exception (body_validator.errors)