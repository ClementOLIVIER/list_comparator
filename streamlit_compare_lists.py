import os
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from comparetor import Comparator
from define_subscriber import upload_default_subscriber_dfs


# Todo: Add loading bar


def display_compared_lists(compared_list_names, compared_subscriber_dfs):
    st.markdown("# Comparaison des listes")

    # Set columns
    cols = st.columns(3)

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    for idx in range(len(compared_list_names)):
        list_name = compared_list_names[idx]
        cs_df = compared_subscriber_dfs[idx]

        cols[idx].write(f"**List: {list_name}**")
        cols[idx].write(cs_df)

        csv = convert_df(cs_df)
        path = os.path.join(list_name, '.csv')
        cols[idx].download_button(
            label="Download data as CSV",
            data=csv,
            file_name=path,
            mime='text/csv',
        )

    st.markdown("---")


def display_input_tables():
    st.markdown("# Fichiers .csv - Listes des inscrits")

    # Set columns
    col1, col2 = st.columns(2)

    # Load list_1 as user input
    previous_season_subscriber_df, new_season_subscriber_df = upload_default_subscriber_dfs()

    list_1_file = col1.file_uploader('Séléctionner le fichier de la saison précedente', type='csv')

    # df = upload_subscriber_df(list_1_file)
    col1.write(previous_season_subscriber_df)

    list_2_file = col2.file_uploader('Séléctionner le fichier de la nouvelle saison', type='csv')

    # df = upload_subscriber_df(list_1_file)
    col2.write(new_season_subscriber_df)

    if previous_season_subscriber_df is None or new_season_subscriber_df is None:
        st.write("Upload a .csv or .xlsx file to get started")

    st.markdown("---")

    return previous_season_subscriber_df, new_season_subscriber_df


def display_counts(subscriber_count_df):

    st.markdown("# Compte des inscrits")

    fig = plt.figure(figsize=(10, 5))
    sns.barplot(data=subscriber_count_df, x="name", y="count", palette="hls")
    plt.title('Subscriber Counts')
    plt.ylabel('Subscriber Count', fontsize=12)

    # Add figure in streamlit app
    st.pyplot(fig)

    st.markdown("---")


def main():
    st.title('Comparateur de listes')


    # Get & Display input tables
    previous_season_subscriber_df, new_season_subscriber_df = display_input_tables()

    # Comparator & Compared lists
    comparator = Comparator()
    comparator.define_lists(previous_season_subscriber_df, new_season_subscriber_df)

    # Compare lists
    compared_list_names = ["new_subscribers", "unsubscribers", "subscribers_in_both"]
    compared_subscriber_dfs = comparator.compare_lists()

    # Display compared lists
    display_compared_lists(compared_list_names, compared_subscriber_dfs)

    # Display compared list counts
    compared_names = ["New Subscribers", "Unsubscribers", "Subscribers in both"]
    subscriber_count_df = comparator.count(compared_subscriber_dfs, compared_names)

    # Display compared plot counts
    display_counts(subscriber_count_df)

main()
