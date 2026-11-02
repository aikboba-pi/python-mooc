def list_years(dates: list) -> list:
    years = [d.year for d in dates]
    return sorted(years)