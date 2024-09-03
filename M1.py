import pandas as pd 
import os


#Variables
PROJ = 'M1'
doc = 'impurities_24-1.csv'
categories = ['Day', 'Filtration', 'Surfactant', 'Sonication'] #Independent
response = 'response' #Dependent

#Dirs
cwd = os.getcwd()
print(cwd)
cwd = cwd.replace("\\", "/")
projdir = cwd + '/Projects/' + PROJ + '/'
resultsdir = projdir + 'ANOVA/'

#Work folders 
folds = [projdir,resultsdir]
for fold in folds:
    if not os.path.exists(fold):
        os.makedirs(fold)

#Data
fil = projdir + doc 
df = pd.read_csv(fil, sep="\t")
print(df)



