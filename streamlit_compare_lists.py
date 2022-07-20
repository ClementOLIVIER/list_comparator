import streamlit as st
from comparetor import Comparator
from streamlit_widget import display_compared_lists, display_input_tables, display_counts

def main():
    st.title('Comparateur de listes')


    # Get & Display input tables
    previous_season_subscriber_df, new_season_subscriber_df = display_input_tables()

    # Comparator & Compared lists
    comparator = Comparator()
    comparator.define_lists(previous_season_subscriber_df, new_season_subscriber_df, column_to_compare="PRENOM_NOM")

    # Compare lists
    # compared_list_names = ["new_subscribers", "unsubscribers", "subscribers_in_both"]
    compared_list_names = ["Nouveaux Inscrits", "Désinscrits", "Inscrit dans les deux saisons"]
    compared_subscriber_dfs = comparator.compare_lists()

    # Display compared lists
    display_compared_lists(compared_list_names, compared_subscriber_dfs)

    # Display compared list counts
    compared_names = ["New Subscribers", "Unsubscribers", "Subscribers in both"]
    subscriber_count_df = comparator.count(compared_subscriber_dfs, compared_names)

    # Display compared plot counts
    display_counts(subscriber_count_df)

main()
