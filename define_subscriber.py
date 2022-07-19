import os
import pandas as pd
import streamlit as st

def upload_subscriber_df(subscriber_list_path):
    subscribers = pd.read_csv(subscriber_list_path)

    if subscribers.columns[0] == 'Nom':
        subscribers.rename(columns={'Nom': 'NOM', "Prénom": "PRENOM"}, inplace=True)

    # Define subscriber_df
    def merge_names(row):
        return (row['PRENOM'] + " - " + row['NOM'])

    subscriber_df = subscribers.apply(merge_names, axis=1)
    return subscriber_df