# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Conversion for SEZ coordinates to ECEF coordinates
# Parameters:
#  o_lat_deg: lattitude in degrees
#  o_lon_deg: longitude in degrees
#  o_hae_km:  altitude in degrees
#  s_km: south coordinate in kilometers
#  e_km: east coordinate in kilometers
#  z_km: zeneith coordinate in kilometers   
#  ...
# Output:
#  A description of the script output
#
# Written by Owen Davies
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., 
import math # math module
import sys # argv


# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions

## function description
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
o_lat_deg = float('nan') # lattitude in degrees
o_lon_deg = float('nan') # longitude in degrees
o_hae_km = float('nan') # altitude in kilometers
s_km = float('nan') # s coordinate in kilometers
e_km = float('nan') # e coordinate in kilometers
z_km = float('nan') # z coordinate in kilomateres

# parse script arguments
if len(sys.argv)==7:
   o_lat_deg = float(sys.argv[1])
   o_lon_deg = float(sys.argv[2])
   o_hae_km = float(sys.argv[3])
   s_km = float(sys.argv[4])
   e_km = float(sys.argv[5])
   z_km = float(sys.argv[6])
else:
    print(\
    'Usage: '\
    'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km'\
    )
    exit()

# write script below this line
#phi is latitude theta is longitude

#convert to radians
o_lat_rad = o_lat_deg*(math.pi/180.0)
o_lon_rad = o_lon_deg*(math.pi/180.0)

# Calculates ECEF Coordinates
ecef_x=(math.cos(o_lon_rad)*math.sin(o_lat_rad)*s_km)+(math.cos(o_lon_rad)*math.cos(o_lat_rad)*z_km)-(math.sin(o_lon_rad)*e_km)
ecef_y=(math.sin(o_lon_rad)*math.sin(o_lat_rad)*s_km)+(math.sin(o_lon_rad)*math.cos(o_lat_rad)*z_km)+(math.cos(o_lon_rad)*e_km)
ecef_z=(-math.cos(o_lat_rad)*s_km)+(math.sin(o_lat_rad)*z_km)

#Calculates the rxyz vector
denom = calc_denom(E_E, o_lat_rad)
C_E = R_E_KM / denom
S_E = (R_E_KM * (1 - E_E * E_E)) / denom
r_x_km = (C_E + o_hae_km) * math.cos(o_lat_rad) * math.cos(o_lon_rad)
r_y_km = (C_E + o_hae_km) * math.cos(o_lat_rad) * math.sin(o_lon_rad)
r_z_km = (S_E + o_hae_km) * math.sin(o_lat_rad)

#ECEF Vector
ecef_x_km = ecef_x+r_x_km
ecef_y_km = ecef_y+r_y_km
ecef_z_km = ecef_z+r_z_km


print(f"{ecef_x_km:.3f}")
print(f"{ecef_y_km:.3f}")
print(f"{ecef_z_km:.3f}")
