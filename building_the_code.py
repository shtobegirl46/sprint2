#we have: excel, equations,
# parameters: time, range, elevation, azimuth,
# radial_velocity, range_uncertainty, elevation_uncertainty, azimuth_uncertainty
# , radial_velocity_uncertainty, ID, macam
import create_list_for_excel
#plan:
#read excel
#calculate ID
#divide information per til and macam

#################################################
from convert_to_csv import result_to_csv
from reading import *
from create_list_for_excel import *
#################################################

def data_to_coordinates(data_line: np.ndarray) ->list:
    """gets data line from macam, and returns absolute location coordinates
    latitude, longtitude, and height"""
    pass


def generate_list(macam_name: str) -> list[list]:
    """gets macam name, generates a list of all measurements of it as a list
    looks like: return [lat, long, z, ID]"""
    pass

def merge_lists(list_of_names: list) ->list[list]:
    """gets lists from different macams using 'generate_list' and returns one list
    of [lat, long, z, ID] lists"""
    pass

def split_to_missiles(list_of_all: list[list]) ->dict:
    """gets the list of all lists of coordinates, and returns a dictionary :
    for each ID which is the key, it matches 2D list of data"""


def calculate_where_from(list_of_missile: list[list]) ->tuple:
    """gets the data for a missile, returns where was the launch"""

def calculate_where_to(list_of_missile: list[list]) -> tuple:
    """gets the data for a missile, returns where it will hit"""


def determine_ammunition_type(list_of_missile: list[list]) -> str:
    """gets the data for a missile, returns what is it's type"""

"""def certainty(x, y):
    calculation = y
    certainty_value = x
    if calculation > x:
        return False
    else:
        return True
def from_cartesian_to_coordinates():
        return True"""


def export_to_excel(result: list[list[float, float, str, str]], output_name, DEBUD=False):
    result_to_csv(result, output_name, DEBUD)


def main():

    all_measurements = merge_lists([
    Gosh_dan_without_id_target_bank,Kiryat_Gat_without_id_target_bank,
    Meron_without_id_target_bank,Modiin_without_id_target_bank,Ofakim_without_id_target_bank,
    Tseelim_without_id_target_bank,YABA_without_id_target_bank,  Ashdod_without_id_impact_point,
    Carmel_without_id_impact_point,Gosh_dan_without_id_impact_point,
    Kiryat_Gat_without_id_impact_point,Meron_without_id_impact_point ,Modiin_without_id_impact_point,
    Tseelim_without_id_impact_point,YABA_without_id_impact_point ])

    data_by_missile = split_to_missiles(all_measurements)
    target_bank = create_list_for_excel.data_form_dict_to_places(data_by_missile, "from")
    hitplaces = create_list_for_excel.data_form_dict_to_places(data_by_missile, "to")

    export_to_excel(target_bank, "results_target_bank")
    export_to_excel(hitplaces, "results_hitplaces")

