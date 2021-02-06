import pandas
import numpy
from collections import Counter

# Country Name   // Important column names
# Country Code
# Indicator Name
# Indicator Code



def get_list_diff(list1, list2):  # This tells us we have 113 countrys in both datasets
    a = Counter(list1)
    b = Counter(list2)
    c = a - b  
    list3 = list(c.elements())
    print(list3)
    print('CountedDiff: ', len(list3))
    print('ActualDiff: ', (len(list1)-len(list2)))

def get_unique(column):
    return numpy.unique(column)

def get_csvFiles(a,b,c,d,e):
    datalist = [{'frame':a, 'title':'TotalPopulation'},{'frame':b, 'title':'PopulationGrowth'},{'frame':c, 'title':'BirthRate'},
    {'frame':d ,'title':'DeathRate'},{'frame':e, 'title':'LifeExp'}]
    for i in datalist:
        title = i['title']+'.csv'
        i['frame'].to_csv(title)

def main():
    data = pandas.read_csv('data/PopData.csv')
    

    CountryNames_Unique = get_unique(data['Country Code'])
    FCN_Unique = get_unique(foodData['Area Abbreviation'])
    get_list_diff(CountryNames_Unique, FCN_Unique)

    total_pop = data.loc[lambda data: data['Indicator Code'] == 'SP.POP.TOTL']
    pop_growth = data.loc[lambda data: data['Indicator Code'] == 'SP.POP.GROW']
    proportion_birthrate = data.loc[lambda data: data['Indicator Code'] == 'SP.DYN.CBRT.IN'] ## Dont forget to divide by 1000 to get proportion
    proportion_deathrate = data.loc[lambda data: data['Indicator Code'] == 'SP.DYN.CDRT.IN']
    pop_lifeexp = data.loc[lambda data: data['Indicator Code'] == 'SP.DYN.LE00.IN']

    a = total_pop.set_index('Country Name')
    b = pop_growth.set_index('Country Name')
    c = proportion_birthrate.set_index('Country Name')
    d = proportion_deathrate.set_index('Country Name')
    e = pop_lifeexp.set_index('Country Name')
    
    #get_csvFiles(a,b,c,d,e)


def foodMain():
    foodData = pandas.read_csv('fao.csv', encoding='latin1')
    print(foodData.head())

if __name__ == '__main__':
    foodMain()