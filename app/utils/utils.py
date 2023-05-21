def remove_critical_data(data: dict, remove_data: list = None):
    for remove_key in remove_data:
        if remove_key in data.keys():
            del data[remove_key]

    if data.get("_key"):
        data["key"] = data.pop("_key")

    if data.get("_id"):
        data["id"] = data.pop("_id")

    return data
