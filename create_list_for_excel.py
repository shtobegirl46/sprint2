from building_the_code import determine_ammunition_type, calculate_where_from, calculate_where_to, certainty

def data_form_dict_to_places(missiles_dict: dict, from_or_to: str) -> list[list]:
    """
    This function gets missiles_dict and return for every missile a list with all the data
    about the missile: latitude and longitude (of the launch or hit according to from_or_to),
    the ammunition type, and the certainty.
    :param missiles_dict:
    :param from_or_to:
    :return: list[list[latitude, logitude, ammunition_type, certainty]
    """
    data = []
    for ID in missiles_dict.keys():
        ammunition_type = determine_ammunition_type(missiles_dict[ID])
        if from_or_to == "from":
            latitude, longitude = calculate_where_from(missiles_dict[ID])
        elif from_or_to == "to":
            latitude, longitude = calculate_where_to(missiles_dict[ID])
        certainty_var = certainty(latitude, longitude)
        data.append([latitude, longitude, ammunition_type, certainty_var])
    return data


if __name__=="__main__":
    pass


