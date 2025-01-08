import pandas as pd
import numpy as np


# import typing


def read_from_macam(name: str) -> np.ndarray:
    # Read the CSV file

    df = pd.read_csv(name, header=None, skiprows=1)

    # Convert the DataFrame to a NumPy array
    data_array = df.to_numpy()

    """
1,2,3               np.array[[1, 2, 3]
4,5,6   ======>>>>>      [4, 5, 6]"""
    return data_array[:,1:]

"""
Ashdod_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Ashdod_with_ID.csv")
Carmel_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Carmel_with_ID.csv")
Gosh_dan_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Gosh_dan_with_ID.csv")
Kiryat_Gat_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Kiryat_Gat_with_ID.csv")
Meron_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Meron_with_ID.csv")
Modiin_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Modiin_with_ID.csv")
Ofakim_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Ofakim_with_ID.csv")
Tseelim_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Tseelim_with_ID.csv")
YABA_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\YABA_with_ID.csv")

Ashdod_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Ashdod_with_ID.csv")
Carmel_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Carmel_with_ID.csv")
Gosh_dan_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Gosh_dan_with_ID.csv")
Kiryat_Gat_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Kiryat_Gat_with_ID.csv")
Meron_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Meron_with_ID.csv")
Modiin_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Modiin_with_ID.csv")
Ofakim_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Ofakim_with_ID.csv")
Tseelim_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Tseelim_with_ID.csv")
YABA_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\YABA_with_ID.csv")

"""
Ashdod_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Ashdod_without_ID.csv")
"""
Carmel_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Carmel_without_ID.csv")
Gosh_dan_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Gosh_dan_without_ID.csv")
Kiryat_Gat_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Kiryat_Gat_without_ID.csv")
Meron_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Meron_without_ID.csv")
Modiin_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Modiin_without_ID.csv")
Ofakim_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Ofakim_without_ID.csv")
Tseelim_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Tseelim_without_ID.csv")
YABA_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\YABA_without_ID.csv")

Ashdod_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Ashdod_without_ID.csv")
Carmel_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Carmel_without_ID.csv")
Gosh_dan_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Gosh_dan_without_ID.csv")
Kiryat_Gat_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Kiryat_Gat_without_ID.csv")
Meron_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Meron_without_ID.csv")
Modiin_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Modiin_without_ID.csv")
Ofakim_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Ofakim_without_ID.csv")
Tseelim_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Tseelim_without_ID.csv")
YABA_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\YABA_without_ID.csv")
"""
print(Ashdod_without_id_target_bank)
list_without_ID = []
#list_without_ID.append()

def extract_to_times(macam: np.ndarray):
    times_existing = []
    data_for_times = []
    new_time = 0
    for i in range(macam.shape[0]):
        if macam[i][0] not in times_existing:
            times_existing.append(float(macam[i][0]))
            new_time += 1
            #data_for_times.append((macam[:,1:])[i])
    print(new_time)
    return times_existing

print(extract_to_times(Ashdod_without_id_target_bank))

#divided_to_times = dict{}