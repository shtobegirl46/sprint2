import math

radar_titude = {
    "ashdod": {"lat" : 31.77757586390034, "lon": 34.65751251836753},

    "gat": {"lat" : 31.602089287486198, "lon": 34.74535762921831},

    "ofakim":{"lat" : 31.302709659709315, "lon": 34.59685294800365},

    "tseelim": {"lat" : 31.20184656499955, "lon": 34.52669152933695},

    "meiron": {"lat" : 33.00023023451869, "lon": 35.404698698883585},

    "yaba": {"lat" : 30.653610411909529, "lon": 34.783379139342955},

    "modiin": {"lat" : 31.891980958022323, "lon": 34.99481765229601},

    "dan": {"lat" : 32.105913486777084, "lon": 34.78624983651992},

    "karmel": {"lat" : 32.65365306190331, "lon": 35.03028065430696}
}

"""Ashdod_with_id_target_bank
Carmel_with_id_target_bank
Gosh_dan_with_id_target_bank
Kiryat_Gat_with_id_target_bank
Meron_with_id_target_bank 
Modiin_with_id_target_bank
Ofakim_with_id_target_bank
Tseelim_with_id_target_bank
YABA_with_id_target_bank
Ashdod_with_id_impact_point
Carmel_with_id_impact_point
Gosh_dan_with_id_impact_point
Kiryat_Gat_with_id_impact_point
Meron_with_id_impact_point
Modiin_with_id_impact_point
Ofakim_with_id_impact_point
Tseelim_with_id_impact_point
YABA_with_id_impact_point"""


def to_cartesian(teta, a, R):
    R = float(R)
    a = float(a)
    teta = float(teta) 

    a = math.radians(a)
    teta = math.radians(teta)

    x = R * math.cos(a) * math.sin(teta)
    y = R * math.cos(a) * math.cos(teta)
    z = R * math.sin(a)

    return x, y, z

def radar_data_to_cart_earth(R_data, azimuth_data, teta_data, radar_name: str):
    earth_rad = 6371000.0

    latitude = math.radians(radar_titude[radar_name]["lat"])
    longitude = math.radians(radar_titude[radar_name]["lon"])

    x, y, z = to_cartesian(R_data, azimuth_data, teta_data)
    final_z = x * math.cos(latitude) + z * math.sin(latitude) + earth_rad * math.sin(latitude)
    final_y = x * math.sin(longitude) * math.sin(latitude) + y * math.cos(longitude) + z * math.cos(latitude) * math.sin(longitude) + earth_rad * math.cos(latitude) * math.sin(longitude)
    final_x = x * math.cos(longitude) * math.sin(latitude) + y * math.sin(longitude) + z * math.cos(latitude) * math.cos(longitude) + earth_rad * math.cos(latitude) * math.cos(longitude)

    return [final_x, final_y, final_z]

def from_cart_to_titude(x, y, z):
    lat = math.degrees(math.atan(z / math.sqrt(x**2 + y**2)))
    lon = math.degrees(math.atan(x / y))

    return lat, lon