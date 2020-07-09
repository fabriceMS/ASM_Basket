import pandas as pd
import numpy as np
from datetime import date



# Calcul le prix d'un joueur 
def getPrice(age, intra_extra):
    if intra_extra == 'INTRA':
            
        if age <= 0:
            return 0
        elif age > 0 and age <= 6:
            return 110
        elif age > 6 and age <= 8:
            return 120
        elif age > 8 and age <= 12:
            return 130
        elif age > 12 and age <= 16:
            return 140
        elif age > 16 and age <= 35:
            return 150
        elif age > 35: 
            return 170
    
    elif intra_extra == 'EXTRA':
        if age <= 0:
            return 0
        elif age > 0 and age <= 6:
            return 115
        elif age > 6 and age <= 8:
            return 125
        elif age > 8 and age <= 12:
            return 135
        elif age > 12 and age <= 16:
            return 145
        elif age > 16 and age <= 35:
            return 155
        elif age > 35: 
            return 175



# Calcul la catégorie du joueur
def getCategory(age):
    if age <= 0:
        return 'Problème'
    if age > 0 and age <= 6:
        return 'Baby-Basket'
    if age > 6 and age <= 8:
        return 'Mini-Poussin & Loisir'
    if age > 8 and age <= 12:
        return 'Poussin/Benjamins'
    if age > 12 and age <= 16:
        return 'Minimes/Cadet'
    if age > 16 and age <= 35:
        return 'Junior-Seniors'
    if age > 35: 
        return 'Anciens'



# Calcul l'age d'un joueur
def calculateAge(birthDate, today=date.today()):
    
    age = today.year - birthDate.year -  ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


# Indique si c'est INTRA ou EXTRA
def getIntraExtra(city,city_to_compare='MANTES-LA-JOLIE'):
    
    if city == city_to_compare:
        return 'INTRA'
    else:
        return 'EXTRA'
    




# Charge un fichier CSV 
def load_csv(csvFile):
    
    
    # Variable initialisation
    intra_extra_array = [] 
    age_array = []
    category_array = []
    price_array = []

    column_names = ['organisation','lb_org','license','nom','prenom','adresse','code_postal','commune',
        'cd_lic','qualification','sexe','taille','cd_cat','cd_ass','naissance','lieu_naissance',
        'numero_licence','certificat_medical','date_fin_certificat_medical','nationalite',
        'telephone_domicile','telephone_professionnel','telephone_portable','mail',
        'telephone_mineur_mere','mail_mineur_mere','telephone_mineur_pere','mail_mineur_pere',
        'autorisation_partenaire','Textbox1']

    
    
    # Ouvertur du CSV dans un DataFrame
    df = pd.read_csv(csvFile, header=0, names=column_names)
    
    # Replace NaN by value -1
    df = df.fillna(-1)

    # Convert float column to int (limitation of Pandas: NaN is a float)
    df.taille = df.taille.astype(int)
    df.license = df.license.astype(int)
    df.code_postal = df.code_postal.astype(int)


    # Calcul de la date de naissance
    df['naissance'] = pd.to_datetime(df['naissance'], dayfirst=True)
    #print(df.info())

    # Calculate the new output   
    for index, row in df.iterrows():

        # Calcul INTRA ou EXTRA
        intra_extra = getIntraExtra(row['commune'])
        intra_extra_array.append(intra_extra)

        # Calcul de l'age
        age = calculateAge(row['naissance'],today=date(2019, 12, 31))
        age_array.append(age)
        
        # Calculer la categorie
        category = getCategory(age)
        category_array.append(category)

        # calculer le prix
        price = getPrice(age, intra_extra)
        price_array.append(price)
        #print ('{} - Annee Naissance:{}\t - Age: {} ans'.format(row['nom'],row['naissance'],age))
    
    
    
    df['age'] = age_array
    df['INTRA/EXTRA'] = intra_extra_array
    df['Category'] = category_array
    df['Price'] = price_array
    df.to_csv('new_data.csv')

    # Create the new CSV
    new_df = df.filter(['nom','prenom','adresse','code_postal','commune','INTRA/EXTRA','age','naissance','id_lice','sexe','taille','Price', 'Category'])
    new_df.fillna(0, inplace=True)
    convert_dict = {'code_postal': int, 'age': int, 'license': int, 'taille': int, 'Price': int}
    new_df.code_postal.astype(int)
    
    
    #new_df = new_df.astype(convert_dict)
    print(new_df.info())
    new_df.to_csv('new_data_asm.csv')
    #new_df.to_json('new_data.json')




    #print (df.info())
    #print (df.head())
    
    #print(df.groupby('Category')['Price'].sum())
    #print('total: {}'.format(df['Price'].sum()))

    return df


# Calcul les sommes à retourner en fonction des INTRA et EXTRA
def calculateReturnValues(df_players):
    nb_intra_by_category = df_players.groupby('INTRA/EXTRA')['Category'].count()
    print('Nombre de joueur par catégorie: {}'.format(nb_intra_by_category))



    nb_intra = nb_intra_by_category['INTRA']
    nb_extra = nb_intra_by_category['EXTRA']

    return_intra = nb_intra * 5
    return_extra = nb_extra * 10
    print(return_extra)
    print(return_intra)

    to_return = {'INTRA': return_intra, 'EXTRA': return_extra}
    print(to_return)

    return to_return

    

if __name__ == "__main__":
    print('Bienvenue sur ASM Basket')
    file = 'asm2020.csv'

    #print (getIntraExtra('Mantes'))
    players = load_csv(file)

    values = calculateReturnValues(players)
    
      
    print ('Pour les EXTRA: {}€'.format(values.get('EXTRA')))
    print ('Pour les INTRA: {}€'.format(values.get('INTRA')))
    np_array = [values.get('EXTRA'),values.get('INTRA')]
        
    total = np.sum(np_array)
    
    print('Au total: {}€'.format(total))


    
    