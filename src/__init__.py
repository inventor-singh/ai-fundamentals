"""
AI Mastery From Scratch - Core Library
======================================

This package contains reusable components for building neural networks from scratch.
"""

__version__ = "1.0.0"
__author__ = "AI Mastery From Scratch"

from .neuron import Neuron
from .network import NeuralNetwork
from .visualization import plot_learning_curve, plot_decision_boundary

__all__ = [
    'Neuron',
    'NeuralNetwork', 
    'plot_learning_curve',
    'plot_decision_boundary'
]
