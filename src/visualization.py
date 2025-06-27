"""
Visualization Utilities
=======================

Beautiful plotting functions for neural network education.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for consistent, beautiful plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


def plot_learning_curve(errors, title="Learning Curve"):
    """Plot the learning curve showing error over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(errors, linewidth=2, alpha=0.8)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Training Step', fontsize=12)
    plt.ylabel('Error', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt.gcf()


def plot_decision_boundary(neuron, X, y, title="Decision Boundary"):
    """Plot the decision boundary of a neuron."""
    plt.figure(figsize=(10, 8))
    
    # Create a mesh to plot the decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    # Get predictions for the mesh
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    Z = np.array([neuron.forward(point) for point in mesh_points])
    Z = Z.reshape(xx.shape)
    
    # Plot the decision boundary
    plt.contourf(xx, yy, Z, levels=20, alpha=0.6, cmap='RdYlBu')
    plt.contour(xx, yy, Z, levels=[0.5], colors='black', linestyles='--', linewidths=2)
    
    # Plot the data points
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu', edgecolors='black', s=100)
    plt.colorbar(scatter, label='True Values')
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Input 1', fontsize=12)
    plt.ylabel('Input 2', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt.gcf()


def plot_weights_evolution(weight_history, title="Weight Evolution"):
    """Plot how weights change during training."""
    plt.figure(figsize=(10, 6))
    weight_history = np.array(weight_history)
    
    for i in range(weight_history.shape[1]):
        plt.plot(weight_history[:, i], linewidth=2, label=f'Weight {i+1}', alpha=0.8)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Training Step', fontsize=12)
    plt.ylabel('Weight Value', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt.gcf()
