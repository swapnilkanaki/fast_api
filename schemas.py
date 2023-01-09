def dataUse_serializer(dataUse) -> dict:
    return {
        "id": dataUse["id"],
        "region": dataUse["region"],
        "data": dataUse["data"],
        "lat": dataUse["lat"],
        "lng":dataUse["lng"],
    }

def dataUses_serializer(dataUses) -> list:
    return [dataUse_serializer(dataUse) for dataUse in dataUses]