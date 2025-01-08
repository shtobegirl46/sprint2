import pandas as pd
import numpy as np


# import typing


def read_from_macam(name: str) -> np.ndarray:
    # Read the CSV file

    df = pd.read_csv(f"{name}.csv", header=None, skiprows=1)

    # Convert the DataFrame to a NumPy array
    data_array = df.to_numpy()

    """
1,2,3               np.array[[1, 2, 3]
4,5,6   ======>>>>>      [4, 5, 6]"""
    return data_array


Ashdod_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Ashdod_with_ID")
Carmel_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Carmel_with_id")
Gosh_dan_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Gosh_dan")
Kiryat_Gat_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Kiryat_Gat")
Meron_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Meron")
Modiin_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Modiin")
Ofakim_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Ofakim")
Tseelim_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\Tseelim")
YABA_with_id_target_bank = read_from_macam(r"With_ID\Target_bank_data\YABA")

Ashdod_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Ashdod_with_ID")
Carmel_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Carmel_with_id")
Gosh_dan_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Gosh_dan")
Kiryat_Gat_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Kiryat_Gat")
Meron_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Meron")
Modiin_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Modiin")
Ofakim_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Ofakim")
Tseelim_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\Tseelim")
YABA_with_id_impact_point = read_from_macam(r"With_ID\Impact_points_data\YABA")

Ashdod_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Ashdod_with_ID")
Carmel_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Carmel_with_id")
Gosh_dan_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Gosh_dan")
Kiryat_Gat_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Kiryat_Gat")
Meron_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Meron")
Modiin_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Modiin")
Ofakim_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Ofakim")
Tseelim_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\Tseelim")
YABA_without_id_target_bank = read_from_macam(r"Without_ID\Target_bank_data\YABA")

Ashdod_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Ashdod_with_ID")
Carmel_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Carmel_with_id")
Gosh_dan_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Gosh_dan")
Kiryat_Gat_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Kiryat_Gat")
Meron_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Meron")
Modiin_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Modiin")
Ofakim_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Ofakim")
Tseelim_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\Tseelim")
YABA_without_id_impact_point = read_from_macam(r"Without_ID\Impact_points_data\YABA")
