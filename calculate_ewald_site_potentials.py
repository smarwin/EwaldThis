import os

from pymatgen.core.structure import Structure
from pymatgen.analysis.ewald import EwaldSummation
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.local_env import CrystalNN

cnn = CrystalNN(cation_anion=True)

oxi_dict = {"Li": 1, "Na": 1, "K": 1, "Rb": 1, "Cs": 1, "Be": 2, "Mg": 2, "Ca": 2, "Sr": 2, "Ba": 2, "La": 3, "Ce": 3, "Pr": 3, "Nd": 3, "Sm": 3, "Eu": 2,
            "Gd": 3, "Tb": 3, "Dy": 3, "Ho": 3, "Er": 3, "Yb": 3, "Lu": 3, "Al": 3, "Si": 4, "P": 5, "N": -3, "O": -2, "F": -1, "Cl": -1, "Br": -1, "I": -1}

site_energies = []
data = []
# Column names
columns = ['Filename', 'Site', 'Element', 'CN', 'Site Energy / MJ/mol']


def calculate_ewald_site_potentials(directory):

    for filename in os.listdir(directory):
        # Skip if not cif file
        if not filename.endswith(".cif"):
            continue

        # Create the file path by joining the directory path and the file name
        file_path = os.path.join(directory, filename)

        # Create a structure from a cif file
        structure = Structure.from_file(file_path)

        # Add oxidation states
        structure.add_oxidation_state_by_element(oxi_dict)

        # Symmetrize structure
        symmetry_analyzer = SpacegroupAnalyzer(structure)
        symmetric_structure = symmetry_analyzer.get_symmetrized_structure()

        # Calculate Ewald site energies
        ewald = EwaldSummation(symmetric_structure)

        """
        We solve the problem of correct indexing of equivalent sites.
        We want to stick to the convention that the index of every species starts with 1, e.g., Sr1, Si1, N1, N2, and NOT Sr1, Si2, N3, N4.
        """
        index_count = {}
        equivalent_indices = []

        # Loop over all equivalent sites
        for n, equivalent_sites in enumerate(symmetric_structure.equivalent_sites):
            # Get element symbol
            if len(equivalent_sites[0].species.elements) > 1:
                element = equivalent_sites[0].species.remove_charges(
                ).to_pretty_string()
                site = f"M{n}"
            else:
                element = equivalent_sites[0].species.elements[0].symbol
                site = f"{element}{n}"

            ############################################################################
            ######################### EWALD SUMMATION OF SITES #########################
            ############################################################################

            # Get correct index of equivalent_sites[0] in symmetric_structure.sites
            index_in_sites = symmetric_structure.index(equivalent_sites[0])

            # Calculate site energy in MJ/mol
            site_energy = round(ewald.get_site_energy(
                index_in_sites) * (-96.485) / 1000, 3)

            site_energies.append(site_energy)

            # Get coordination number of equicalent_sites[0]
            try:
                coordination_number = cnn.get_cn(
                    symmetric_structure, index_in_sites, on_disorder='take_max_species')
            except:
                coordination_number = 0

            # Append site data to data list
            data.append([filename, site,
                        element, coordination_number, site_energy])

    return data, columns
