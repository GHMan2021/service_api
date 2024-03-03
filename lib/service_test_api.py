def check_validate_response(data, schema):
    if isinstance(data, list):
        for item in data:
            schema.model_validate(item)
    else:
        schema.model_validate(data)
