from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def perform_kmeans(data, n_clusters):
    """
    Perform K-Means clustering and calculate the silhouette score.
    
    Args:
        data (np.array): Preprocessed data for clustering.
        n_clusters (int): Number of clusters.
    
    Returns:
        model (KMeans): Trained KMeans model.
        labels (np.array): Cluster labels for each data point.
        score (float): Silhouette score of the clustering.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(data)
    score = silhouette_score(data, labels)
    return model, labels, score
