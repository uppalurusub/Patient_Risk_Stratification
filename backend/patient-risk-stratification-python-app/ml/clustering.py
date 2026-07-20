# ml/clustering.py

from sklearn.cluster import KMeans

def train_kmeans(data):

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    model.fit(data)

    return model