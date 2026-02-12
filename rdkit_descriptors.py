from pandas.core.interchange.dataframe_protocol import DataFrame
from rdkit import Chem
import requests
import pandas as pd

#Creation of an Excel file with SMILES annotations in the first column and name SMILES
smiles_list = ['[H][C@]12SC(C)(C)[C@@H](N1C(=O)[C@H]2NC(=O)[C@H](N)C1=CC=C(O)C=C1)C(O)=O',
'N[C@]([H])(C)C(=O)O',
'N[C@@]([H])(C)C(=O)O'
]

df = pd.DataFrame(data =smiles_list, columns = ['SMILES'])
df.to_excel('desc_table.xlsx', index = False)

# def descriptor_structure():
#
#     return structure
#
# if __name__ == '__main__':
#     structure = descriptor_structure()
