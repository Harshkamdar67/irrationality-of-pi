# irrationality-of-pi

# Animated Visualization of Irrationality of π

This repository contains Python code to create an animated visualization of the irrationality of the mathematical constant π (pi) using Matplotlib and SymPy.

## Table of Contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Code Explanation](#code-explanation)
- [Why π is Irrational](#why-pi-is-irrational)
- [How to Use](#how-to-use)
- [License](#license)

## Introduction

This code generates an interactive animation that illustrates the concept of irrationality of π. It shows two rotating rods, one inside the other, and the path traced by the outer rod. The speed at which the rods rotate is such that it demonstrates the near-miss approximations of π. The animation allows you to zoom in and out, providing an interactive experience.

## Demo

To see the animation in action, you can visit the live demo [here](#your-demo-link).

## Code Explanation

### Constants

- `inner_angular_velocity`: This constant controls the rotational speed of the inner rod.
- `x`: The value of π, represented as an exact value using the SymPy library.

### Calculating Position

The `calculate_position(theta)` function uses complex number mathematics to calculate the position of the end of the outer rod based on the given angle `theta`. It utilizes SymPy's `exp` function to handle complex exponentiation and extracts the real and imaginary components of the result.

### Visualization

The code uses Matplotlib to create the figure and initialize the rods for visualization. The rods are represented as lines with markers for improved styling.

### Animation

The animation is created using Matplotlib's `FuncAnimation` class. The `update` function updates the animation at each frame, calculating the positions of the rods and tracing the path of the outer rod.

### Smooth Zooming

The animation is made interactive by allowing smooth zooming with the canvas following the pointer. The `on_scroll` function handles the mouse scroll event, adjusting the axis limits to zoom in and out while keeping the pointer position constant.

## Why π is Irrational

The irrationality of π means that it cannot be expressed as a simple fraction, and its decimal representation goes on forever without repeating. There is no pair of integers (a and b) for which a/b equals π. This property is a consequence of the mathematical nature of π and is demonstrated in the animation through near-miss approximations.

## How to Use

To run this code locally, you will need Python installed, along with the SymPy and Matplotlib libraries. You can install these dependencies using pip:

```bash
pip install sympy matplotlib
