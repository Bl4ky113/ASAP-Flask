
from flask import current_app

def filter_dict_for_model (dict_data, model, warn=False, skip_id=True):
    model_fields = model._fields.keys()
    filtered_data = {}

    for field in model_fields:
        try:
            if field == "id" and skip_id:
                continue

            filtered_data[field] = dict_data[field]

        except KeyError as warning:
            if warn:
                current_app.logger.warning(f"STUDENT DATA FIELD ({field}) NOT PASSED")

    return filtered_data
