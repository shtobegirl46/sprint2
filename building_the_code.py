#we have: excel, equations,
# parameters: time, range, elevation, azimuth,
# radial_velocity, range_uncertainty, elevation_uncertainty, azimuth_uncertainty
# , radial_velocity_uncertainty, ID, macam


#plan:
#read excel
#calculate ID
#divide information per til and macam

#################################################
import numpy as np
import pandas
#################################################

def data_to_coordinates(data_line: np.ndarray) ->list:
    """gets data line from macam, and returns absolute location coordinates
    relative to YABA in meters"""
    pass


def generate_list(macam_name: str) -> list[list]:
    """gets macam name, generates a list of all measurements of it as a list
    looks like: return [x, y, z, ID]"""

def merge_lists(list_of_names: list) ->list[list]:
    """gets lists from different macams using 'generate_list' and returns one list
    of [x, y, z, ID] lists"""

def split_to_missiles(list_of_all: list[list]) ->dict:
    """dfghj"""


def calculate_where_from(ID: str[int]):
    pass

def calculate_where_to():
    pass
def certainty(x, y):
    calculation = y
    certainty_value = x
    if calculation > x:
        return False
    else:
        return True
def from_cartesian_to_coordinates()

def export_to_excel():
    pass


def main():
