from sklearn.datasetsimport load_iris
from sklearn.cluster import KMeans
from sklearn.metricsimport accuracy_score, f1_score, precision_score, recall_score
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt import
seaborn as sns
import pandas as pd
import numpy as np
# Load the iris dataset iris
= load_iris()
X = iris.data y
= iris.target
# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)
# Function to match predicted cluster labels to true labels def
cluster_labels_to_true_labels(y_true, y_pred):
D = np.zeros((np.max(y_pred) + 1, np.max(y_true) + 1), dtype=np.int32) for i
in range(y_pred.size):
D[y_pred[i], y_true[i]] += 1
row_ind, col_ind = linear_sum_assignment(D.max() - D) return
col_ind
# Function to compute evaluation metrics def
compute_metrics(y_true, y_pred):

y_pred_matched = cluster_labels_to_true_labels(y_true, y_pred)[y_pred] accuracy
= accuracy_score(y_true, y_pred_matched)
precision = precision_score(y_true, y_pred_matched, average='weighted')
recall = recall_score(y_true, y_pred_matched, average='weighted')
f1 = f1_score(y_true, y_pred_matched, average='weighted')
return accuracy, precision, recall, f1
# Compute metrics for K-Means clustering kmeans_metrics =
compute_metrics(y, kmeans_labels)
# Plot the results
df = pd.DataFrame(X, columns=iris.feature_names)
df['Cluster'] = kmeans_labels
df['True Label'] = y
sns.pairplot(df, hue='Cluster', palette='viridis')
plt.suptitle('K-Means Clustering')
plt.show()
