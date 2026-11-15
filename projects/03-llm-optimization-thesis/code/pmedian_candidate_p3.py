# Source repository: TM-HESSO-202526/llm-clustering-heuristics @ 1c810e0
# Source path: experiments/selected_clustering_heuristics_final_by_objective/P_MEDIAN_data_point_centers/P3_heuristic.py
# Candidate: P3 — Coarse-to-Fine Medoid Construction with Local In-Cluster Replacement
# Provenance: LLM-generated, curated candidate selected for final evaluation.
# Omissions: Standalone sample-data demo and print statement. Algorithm unchanged.

import numpy as np
import math

class ClusteringHeuristic:
    def __call__(self, X, p, rng=None):
        """
        Improved P-median clustering heuristic.

        :param X: Sample points (numpy array of shape (m, d))
        :param p: Number of centers to return
        :param rng: Optional numpy.random.Generator
        :return: p representative centers (numpy array of shape (p, d))
        """
        if rng is None:
            rng = np.random.default_rng()
        
        # Calculate quarter_p as the number of coarse representative centers
        quarter_p = max(1, p // 4)

        # Initialize coarse centers randomly from the sample points
        coarse_centers = X[rng.choice(X.shape[0], size=quarter_p, replace=False)]

        # Assign sample points to coarse centers
        distances = np.linalg.norm(X[:, np.newaxis] - coarse_centers, axis=2)
        assignments = np.argmin(distances, axis=1)

        # Split each coarse center into two
        centers = []
        for i in range(quarter_p):
            points_in_cluster = X[assignments == i]
            if len(points_in_cluster) > 0:
                # Calculate the centroid of the cluster
                centroid = np.mean(points_in_cluster, axis=0)
                
                # Calculate the point furthest from the centroid
                furthest_point_idx = np.argmax(np.linalg.norm(points_in_cluster - centroid, axis=1))
                furthest_point = points_in_cluster[furthest_point_idx]
                
                # Add the centroid and the furthest point to the list of centers
                centers.append(centroid)
                centers.append(furthest_point)
        
        # If we have less than p centers, add more points from the sample
        while len(centers) < p:
            # Calculate the distances from each sample point to the current centers
            distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
            min_distances = np.min(distances, axis=1)
            
            # Add the point with the maximum minimum distance to the list of centers
            max_distance_idx = np.argmax(min_distances)
            centers.append(X[max_distance_idx])
        
        # Refine the centers by replacing each center with the point in its cluster that minimizes the local sum of distances
        refined_centers = []
        for i in range(len(centers)):
            # Calculate the distances from each sample point to the current center
            distances = np.linalg.norm(X - centers[i], axis=1)
            
            # Assign sample points to the current center
            assignments = np.argmin(np.linalg.norm(X[:, np.newaxis] - centers, axis=2), axis=1)
            points_in_cluster = X[assignments == i]
            
            # Calculate the point in the cluster that minimizes the local sum of distances
            if len(points_in_cluster) > 0:
                cluster_distances = np.linalg.norm(points_in_cluster[:, np.newaxis] - points_in_cluster, axis=2)
                cluster_min_distances = np.min(cluster_distances, axis=1)
                distances_to_points = np.linalg.norm(points_in_cluster[:, np.newaxis] - points_in_cluster, axis=2)
                sum_distances_to_points = np.sum(distances_to_points, axis=1)
                replacement_idx = np.argmin(sum_distances_to_points)
                refined_centers.append(points_in_cluster[replacement_idx])
            else:
                refined_centers.append(centers[i])
        
        # Filter refined centers to only include points from the sample
        filtered_centers = []
        for center in refined_centers:
            distances = np.linalg.norm(X - center, axis=1)
            min_distance_idx = np.argmin(distances)
            if distances[min_distance_idx] < 1e-6:
                filtered_centers.append(X[min_distance_idx])
            else:
                filtered_centers.append(center)
        
        # Return the refined centers
        return np.array(filtered_centers[:p])
