# Ewald Site Energies Calculation Tool

This project comprises a set of Python scripts with a focus on calculating Ewald site energies for structures described in CIF files. The core of this project is the `calculate_ewald_site_potentials.py` script, which utilizes the pymatgen library to compute the electrostatic potential at atomic sites within periodic systems. This calculation is pivotal in the field of materials science and computational chemistry for understanding the electrostatic contributions to a material's total energy.

## Core Script: calculate_ewald_site_potentials.py

### Purpose

This script calculates Ewald site potentials, providing insights into the electrostatic potential experienced by atoms in a crystalline structure. It reads structures from CIF files, assigns oxidation states, symmetrizes the structure, and performs Ewald summation to compute site-specific energies.

### Key Features

- **Oxidation State Assignment**: Utilizes a predefined oxidation state dictionary for elements to prepare the structure for Ewald summation.
- **Structure Symmetrization**: Applies symmetry analysis to identify equivalent atomic sites, enhancing the accuracy of the Ewald calculation.
- **Ewald Summation**: Computes the electrostatic potential at each atomic site, factoring in the periodic nature of the crystal lattice.
- **Coordination Number Calculation**: Determines the coordination number for each site, aiding in the analysis of the structure's chemical environment.

### Installation

Ensure you have Python installed, along with the pymatgen library, which is essential for structure manipulation and Ewald summation calculations. Install pymatgen using pip:

```
pip install pymatgen
```

## Usage

1. Place your CIF files in `data`.
2. Adjust the `oxi_dict` within the script if necessary to match the oxidation states in your structures.
3. Run the script, specifying the directory containing your CIF files (default: `data`):

```
python main.py
```

The script will iterate over all CIF files in the specified directory, performing Ewald summation for each and outputting the results, including site energies and coordination numbers.

## Other Scripts in This Project

- **main.py**: Orchestrates the overall workflow, potentially calling the Ewald calculation script and handling input/output.
- **create_csv.py**: Formats and exports the calculation results to a CSV file for easy analysis and sharing.

## Contributing

Contributions to enhance the functionality, accuracy, or usability of these scripts are welcome. Whether it's improving the core Ewald calculation, extending the project's capabilities, or fixing bugs, your input is valued.
