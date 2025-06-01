import pandas as pd
import os

file_name = os.listdir('Crime')
for file in file_name:

    if 'GN' in file:
        if '2021' in file:
            continue
        # Lire le fichier brut
        raw = pd.read_csv('Crime/' + file, header=None, encoding='unicode_escape', sep=';')

        # Extraire les lignes clés
        departements_line = raw.iloc[0]
        stations_line = raw.iloc[1]

        # Extraire les vraies données (après ligne 3)
        data = raw.iloc[2:].reset_index(drop=True)
        data.columns = raw.iloc[1]  # utiliser la 3e ligne comme colonnes

        # Boucler sur les colonnes département/périmètre
        records = []
        for col in data.columns[2:]:  # sauter 'Code index' et 'Libellé index'
            col_idx = data.columns.get_loc(col)
            dep_num = departements_line.iloc[col_idx]
            station = stations_line.iloc[col_idx]
            data.columns = data.columns.str.encode('latin1').str.decode('utf-8', 'ignore')
            print(data.columns.tolist())
            for idx, row in data.iterrows():
                records.append({
                    'annee': '2021',
                    'departement_numero': dep_num,
                    'poste': station,
                    'code_index': row['Code index'],
                    'libelle_index': row['Libell index \\ CGD'],
                    'faits': row[col]
                })

        # Créer un DataFrame plat
        flat_df = pd.DataFrame(records)
        flat_df.fillna(0, inplace=True)
        file_new_name = file.split('.')[0] + '_flat.csv'

        # Sauver en CSV plat
        flat_df.to_csv(file_new_name, index=False)
    else:

        # Lire le fichier brut
        raw = pd.read_csv('Crime/' + file, header=None, encoding='latin1', sep=';')

        # Extraire les lignes clés
        departements_line = raw.iloc[0]
        perimetres_line = raw.iloc[1]
        stations_line = raw.iloc[2]

        # Extraire les vraies données (après ligne 3)
        data = raw.iloc[3:].reset_index(drop=True)
        data.columns = raw.iloc[2]  # utiliser la 3e ligne comme colonnes

        # Boucler sur les colonnes département/périmètre
        records = []
        for col in data.columns[2:]:  # sauter 'Code index' et 'Libellé index'
            col_idx = data.columns.get_loc(col)
            dep_num = departements_line.iloc[col_idx]
            peri = perimetres_line.iloc[col_idx]
            station = stations_line.iloc[col_idx]
            data.columns = data.columns.str.encode('latin1').str.decode('utf-8', 'ignore')
            print(data.columns.tolist())
            for idx, row in data.iterrows():
                records.append({
                    'annee': '2021',
                    'departement_numero': dep_num,
                    'perimetre': peri,
                    'poste': station,
                    'code_index': row['Code index'],
                    'libelle_index': row['Libell index \\ CSP'],
                    'faits': row[col]
                })

        # Créer un DataFrame plat
        flat_df = pd.DataFrame(records)
        flat_df.fillna(0, inplace=True)
        file_new_name = file.split('.')[0] + '_flat.csv'

        # Sauver en CSV plat
        flat_df.to_csv(file_new_name, index=False)
