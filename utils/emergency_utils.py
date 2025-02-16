def get_emergency_numbers(country_name):
    """Fetch emergency numbers based on the country."""
    emergency_numbers = {
        "United States": {"Emergency Services": "911", "Poison Control": "1-800-222-1222"},
        "United Kingdom": {"Emergency Services": "999", "Poison Control": "111"},
        "India": {"Emergency Services": "112", "Ambulance": "102"},
        "Canada": {"Emergency Services": "911", "Health Services": "811"},
        "Australia": {"Emergency Services": "000", "Poison Control": "13 11 26"},
        "Pakistan": {"Emergency Services": "1122"}
    }
    return emergency_numbers.get(country_name, {"Emergency Services": "Check local authorities"})