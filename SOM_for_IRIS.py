from minisom import MiniSom
from sklearn import preprocessing
import numpy as np
import sklearn.datasets
from sklearn.metrics import confusion_matrix, accuracy_score


def eu_dist(t1, t2):
    """
    Calculates Euclidean distance between two points
    """
    return ((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2)**0.5

def get_cluster(centroids, x):
    """
    Returns the cluster number to which a data point 'x' belongs to
    """
    dist = []
    for c in centroids:
        dist.append(eu_dist(c, x))
    return dist.index(min(dist))

def preprocessed_data():
    """
    Preprocess the Iris dataset using minimax normalization technique
    """
    iris = sklearn.datasets.load_iris()
    data = iris.data[:, :4]
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0.1, 0.9))
    data = np.array(min_max_scaler.fit_transform(data))
    return data


if __name__ == '__main__':
    data = preprocessed_data()
    # Initializing the SOM network with with a 7 X 7 Kohonen Network 
    som = MiniSom(7, 7, 4, sigma=1.0, learning_rate=0.5)
    som.pca_weights_init(data)
    # Train the SOM network with 1000 epochs
    som.train(data, 1000, verbose=True)
    # Finding the winning neuron
    coords = [som.winner(xx) for cnt, xx in enumerate(data)]
    # Calculating the centroids
    c1 = tuple(np.mean(coords[0:50], axis=0))
    c2 = tuple(np.mean(coords[50:100], axis=0))
    c3 = tuple(np.mean(coords[100:150], axis=0))
    centroids = []
    centroids.append(c1)
    centroids.append(c2)
    centroids.append(c3)
    print("Centroids")
    print(c1, c2, c3)
    # Get cluster numbers for all datapoints in the dataset
    clusters = [get_cluster(centroids, coord) for coord in coords]
    # Get the actual cluster labels as present in the dataset for calculating clustering accuracy
    labels = sklearn.datasets.load_iris().target
    # Finding the confusion matrix
    print(confusion_matrix(labels, clusters))
    # Finding the clustering accuracy
    print(str(accuracy_score(labels, clusters)*100) + " %")




