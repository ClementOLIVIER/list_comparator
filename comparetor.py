import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Comparator:
    def __init__(self):
        pass
    def define_lists(self, list_1, list_2, column_to_compare):
        self.list_1 = list_1
        self.list_2 = list_2
        self.column_to_compare = column_to_compare

    def print_lists(self):
        print("# List A")
        print(self.print(self.list_1))
        print("# List B")
        print(self.print(self.list_2))

    def compare_lists(self):
        compared_list_dfs = []

        # Define set
        l1_set = set(self.list_1[self.column_to_compare])
        l2_set = set(self.list_2[self.column_to_compare])

        # Difference and intersection
        l1_minus_l2 = l1_set.difference(l2_set)
        l2_minus_l1 = l2_set.difference(l1_set)
        l1_and_l2 = l1_set.intersection(l2_set)

        # To dataframe
        def set_to_dataframe(set_to_convert):

            dict_to_df = {
                "PRENOM": [],
                "NOM": [],
                "PRENOM_NOM": []
            }

            for prenom_nom in set_to_convert:
                prenom, nom = prenom_nom.split(" - ")

                dict_to_df["PRENOM"].append(prenom)
                dict_to_df["NOM"].append(nom)
                dict_to_df["PRENOM_NOM"].append(prenom_nom)

            return pd.DataFrame().from_dict(dict_to_df)

        l1_minus_l2_df = set_to_dataframe(l1_minus_l2)
        l2_minus_l1_df = set_to_dataframe(l2_minus_l1)
        l1_and_l2_df = set_to_dataframe(l1_and_l2)

        compared_list_dfs = (l1_minus_l2_df, l2_minus_l1_df, l1_and_l2_df)

        return compared_list_dfs

    def print(self, list_df):
        print(list_df.to_markdown())

    def count(self, list_dfs, list_names):
        list_counts = [list_df.count()[0] for list_df in list_dfs]
        counts_dict = {
            "name": list_names,
            "count": list_counts
        }
        count_df = pd.DataFrame.from_dict(counts_dict)
        return count_df

    def percentage(self, list_df):
        raise NotImplementedError

    def plot_counts(self, count_df):

        # Add segmentation by level: https://stackoverflow.com/questions/58320398/plotting-the-count-of-occurrences-per-date
        # Or: 30. Categorical Plots in https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
        fig = plt.figure()
        # Save a palette to a variable:
        palette = sns.color_palette("hls")

        # Use palplot and pass in the variable:
        #sns.palplot(palette)
        sns.barplot(data=count_df, x="name", y="count", palette="hls")
        fig.suptitle('sf')
        plt.show()
        print("Plotting...")


