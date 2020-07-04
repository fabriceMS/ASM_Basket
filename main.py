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
def getIntraExtra(city):
    CITY_NAME = 'MANTES-LA-JOLIE'
    if city == CITY_NAME:
        return 'INTRA'
    else:
        return 'EXTRA'
    




# Charge un fichier CSV 
def load_csv(csvFile):
    # Ouvertur du CSV dans un DataFrame
    df = pd.read_csv(csvFile)
    df.dropna()


    # Calcul de la date de naissance
    df['naissance'] = pd.to_datetime(df['naissance'], dayfirst=True)
    #print(df.info())


    intra_extra_array = [] 
    age_array = []
    category_array = []
    price_array = []
    for index, row in df.iterrows():

        # Calcul INTRA ou EXTRA
        intra_extra = getIntraExtra(row['lb_cmne'])
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
    
    
    
    df['Age'] = age_array
    df['INTRA/EXTRA'] = intra_extra_array
    df['Category'] = category_array
    df['Price'] = price_array
    df.to_csv('new_data.csv')
    #print (df.info())
    #print (df.head())
    
    #print(df.groupby('Category')['Price'].sum())
    #print('total: {}'.format(df['Price'].sum()))

    return df


# Calcul les sommes à retourner en fonction des INTRA et EXTRA
def calculateReturnValues(df_players):
    nb_intra_by_category = df_players.groupby('INTRA/EXTRA')['Category'].count()

    nb_intra = nb_intra_by_category['INTRA']
    nb_extra = nb_intra_by_category['EXTRA']

    return_intra = nb_intra * 5
    return_extra = nb_extra * 10

    to_return = {'INTRA': return_intra, 'EXTRA': return_extra}

    return to_return

    

if __name__ == "__main__":
    print('Bienvenue sur ASM Basket')
    file = 'data.csv'

    #print (getIntraExtra('Mantes'))
    players = load_csv(file)

    values = calculateReturnValues(players)
    
      
    print ('Pour les EXTRA: {}€'.format(values.get('EXTRA')))
    print ('Pour les INTRA: {}€'.format(values.get('INTRA')))
    np_array = [values.get('EXTRA'),values.get('INTRA')]
        
    total = np.sum(np_array)
    
    print('Au total: {}€'.format(total))


    
    