"""
Neural Network Implementation
============================

Multi-layer neural network for educational purposes.
"""

import numpy as np
from .neuron import Neuron


class NeuralNetwork:
    """A simple multi-layer neural network."""
    
    def __init__(self, layer_sizes):
        """
        Initialize network with specified layer sizes.
        
        Args:
            layer_sizes: List of integers, e.g., [2, 3, 1] for 2 inputs, 3 hidden, 1 output
        """
        self.layers = []
        self.layer_sizes = layer_sizes
        
        # Create layers
        for i in range(len(layer_sizes) - 1):
            layer = []
            for _ in range(layer_sizes[i + 1]):
                neuron = Neuron(layer_sizes[i])
                layer.append(neuron)
            self.layers.append(layer)
    
    def forward(self, inputs):
        """Forward pass through all layers."""
        current_input = inputs
        
        for layer in self.layers:
            layer_output = []
            for neuron in layer:
                output = neuron.forward(current_input)
                layer_output.append(output)
            current_input = np.array(layer_output)
        
        return current_input
    
    def train_step(self, inputs, targets):
        """Single training step using backpropagation."""
        # This is a simplified version - full backprop implementation
        # will be covered in Phase 2 lessons
        predictions = self.forward(inputs)
        error = np.mean((targets - predictions) ** 2)
        return predictions, error
