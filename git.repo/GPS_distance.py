from math import pi,sqrt,sin,cos,atan2


n2 = 55.81580
e2 = 49.18116
n1 = 55.85152
e1 = 48.56731

def haversine(n1,e1,n2,e2):
    lat1 = float(n1)
    long1 = float(e1)
    lat2 = float(n2)
    long2 = float(e2)

    # haversine formula
    degree_to_rad = float(pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = 6367 * c
    mi = 3956 * c

    return {"km": km, "miles": mi}

print(haversine(n1,e1,n2,e2))