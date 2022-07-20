import pandas as pd


def upload_subscriber_df(subscriber_list_path):
    subscriber_df = pd.read_csv(subscriber_list_path, sep=";", encoding = "ISO-8859-1")

    if subscriber_df.columns[0] == 'Nom':
        subscriber_df.rename(columns={'Nom': 'NOM', "Prénom": "PRENOM"}, inplace=True)

    # Define subscriber_df
    def merge_names(row):
        return (row['PRENOM'] + " - " + row['NOM'])

    subscriber_df["PRENOM_NOM"] = subscriber_df.apply(merge_names, axis=1)
    return subscriber_df
