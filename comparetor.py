import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Comparator:
    def __init__(self):
        pass
    def define_lists(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

        # Compute

    def print_lists(self):
        print("# List A")
        print(self.print(self.list_1))
        print("# List B")
        print(self.print(self.list_2))

    def compare_lists(self):
        column_name = "Prénom - Nom"
        compared_list_dfs = []

        l1_minus_l2 = set(self.list_1).difference(set(self.list_2))
        l1_minus_l2_df = pd.DataFrame(list(l1_minus_l2), columns=[column_name])
        compared_list_dfs.append(l1_minus_l2_df)

        l2_minus_l1 = set(self.list_2).difference(set(self.list_1))
        l2_minus_l1_df = pd.DataFrame(list(l2_minus_l1), columns=[column_name])
        compared_list_dfs.append(l2_minus_l1_df)

        l1_and_l2 = set(self.list_1).intersection(set(self.list_2))
        l1_and_l2_df = pd.DataFrame(list(l1_and_l2), columns=[column_name])
        compared_list_dfs.append(l1_and_l2_df)

        # compared_list_dfs = (l1_minus_l2, l2_minus_l1, l1_and_l2_df)
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


