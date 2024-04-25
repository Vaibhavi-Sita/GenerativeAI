import os
import sys
from pymol import cmd, finish_launching

finish_launching(['pymol', '-c'])  # The '-c' flag launches PyMOL without the GUI

pdb_directory = './newpdb'
output_directory = './newpdb/images'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for file_name in os.listdir(pdb_directory):
    if file_name.endswith('.pdb'):
        pdb_path = os.path.join(pdb_directory, file_name)
        output_path = os.path.join(output_directory, file_name.replace('.pdb', '.png'))
        print(pdb_path)
        cmd.load(pdb_path)
        cmd.remove('solvent')
        cmd.png(output_path)
        cmd.delete('all')  # Clear the PyMOL workspace for the next file

cmd.quit()
