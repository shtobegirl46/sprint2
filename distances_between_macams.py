import math

#latitude - affects y axis
#longitude - affects x axis
#this dictionary gives delta x and delta y between a certain radar and the yaba radar.
#the first value is according to latitude lines, therefore represents delta y!
radars_distances_dict = {
    "ashdod": (124980, -13994),

    "gat": (105470, -4227),

    "ofakim":(72177, -20738),

    "tseelim": (60961, -28538),

    "meiron": (260932, 69077),

    "yaba": (0,0),

    "modiin":(137701, 23507),

    "dan":(161489, 319.16),

    "karmel": (222395, -27450)
}

def function(r, a, teta, radar_name):
    """This function gets distance, elevation, aziumuth and radar name.
    According to those, it calculates the distance of the rocket from the yaba
     radar."""
    x, y, z = r*math.cos(a)*(math.sin(teta)), r*math.cos(a)*(math.cos(teta)), r*math.sin(a)
    difference_y, difference_x = radars_distances_dict[radar_name]
    rel_x, rel_y = x + difference_x , y + difference_y
    return rel_x, rel_y, z

print(function(41912.98, 12.50915, 217.8793, "karmel"))