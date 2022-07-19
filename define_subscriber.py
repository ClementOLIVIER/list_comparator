import os
import pandas as pd
import streamlit as st

def upload_default_subscriber_dfs():
    # OLD: define_subscriber_df_old
    # Load user input compare list
    dir = "."
    list_1_filename = "data/sample_list_1.csv"
    list_2_filename = "data/sample_list_2.csv"

    previous_season_subscribers = pd.read_csv(os.path.join(dir, list_1_filename))
    new_season_subscribers = pd.read_csv(os.path.join(dir, list_2_filename))
    new_season_subscribers.rename(columns={'Nom': 'NOM', "Prénom": "PRENOM"}, inplace=True)

    # Define subscriber_df
    def merge_names(row):
        return (row['PRENOM'] + " - " + row['NOM'])

    previous_season_subscriber_df = previous_season_subscribers.apply(merge_names, axis=1)
    new_season_subscriber_df = new_season_subscribers.apply(merge_names, axis=1)

    return previous_season_subscriber_df, new_season_subscriber_df


def upload_subscriber_df(file):
    st.write("#############")
    st.write("File : " + str(file))
    # season_subsribers_df = pd.read_csv(file)
    # if season_subsribers_df.columns[0] == 'Nom':
    #     season_subsribers_df.rename(columns={'Nom': 'NOM', "Prénom": "PRENOM"}, inplace=True)
    return None