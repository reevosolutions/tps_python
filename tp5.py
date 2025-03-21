import pandas as pd
import matplotlib.pyplot as plt

data_types = {
    "age": 'int',
    "job": 'str',
    "marital": 'str',
    "education": 'str',
    "default": 'str',
    "balance": 'int',
    "housing": 'str',
    "loan": 'str',
    "contact": 'str',
    "day": 'int',
    "month": 'str',
    "duration": 'int',
    "campaign": 'int',
    "pdays": 'int',
    "previous": 'int',
    "poutcome": 'str',
    "y": 'str',
}

# Chargement des données
df = pd.read_csv('./bank.csv', dtype=data_types)


# Affichage des premières lignes
print(df.head())

# Ajouter une colonne calculée
df['new_column'] = df['balance'] * 10
print(df.head())

# Filtrage des données selon un critère
filtered_df = df[df['balance'] > 4000]
print(filtered_df)


# Tracer un histogramme
df['month'].hist()
plt.title('Histogramme')
plt.show()

# Sauvegarde du plot
plt.savefig('path_to_save_plot.png')