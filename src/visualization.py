import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(data, labels):
    """
    Visualize the clusters using a scatter plot.
    
    Args:
        data (np.array): Data points.
        labels (np.array): Cluster labels.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=labels, palette='viridis')
    plt.title('Cluster Visualization')
    plt.show()
