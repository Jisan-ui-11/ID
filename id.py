def create_id_card(name, year, school, more_info=None):
    # Create a text-based ID card
    card = f"""
    Name: {name}
    Year: {year}
    School: {school}
    """
    if more_info:
        card += f"More: {more_info}\n"

    # Print the ID card
    print(card)