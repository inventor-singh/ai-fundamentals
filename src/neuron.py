"""
Basic Neuron Implementation
==========================

A simple neuron class for educational purposes.
"""

import numpy as np


class Neuron:
    """A single neuron that can learn through gradient descent."""
    
    def __init__(self, input_size):
        """Initialize neuron with random weights and zero bias."""
        self.weights = np.random.randn(input_size) * 0.01
        self.bias = 0.0
        self.learning_rate = 0.1
    
    def forward(self, inputs):
        """Forward pass: compute weighted sum + bias, then apply activation."""
        z = np.dot(inputs, self.weights) + self.bias
        return self.sigmoid(z)
    
    def sigmoid(self, z):
        """Sigmoid activation function."""
        # Clip z to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    
    def train_step(self, inputs, target):
        """Single training step using gradient descent."""
        # Forward pass
        prediction = self.forward(inputs)
        
        # Compute error
        error = target - prediction
        
        # Backward pass (gradient computation)
        gradient_w = error * prediction * (1 - prediction) * inputs
        gradient_b = error * prediction * (1 - prediction)
        
        # Update weights and bias
        self.weights += self.learning_rate * gradient_w
        self.bias += self.learning_rate * gradient_b
        
        return prediction, error
