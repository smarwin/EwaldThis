import os
from calculate_ewald_site_potentials import calculate_ewald_site_potentials
from create_csv import create_csv

directory = r'data'
output_file = 'EWALD_v1.csv'

# run get_volumes_from_polynator.py
data, columns = calculate_ewald_site_potentials(directory)

# create csv
file_path = os.path.join(directory, output_file)
create_csv(file_path, columns, data)
