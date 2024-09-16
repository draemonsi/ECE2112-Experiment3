# Experiment 2: Numerical Python (NumPy)

## Course: ECE 2112 - Advanced Computer Programming and Algorithms <br/>
**Institution**: University of Santo Tomas, Faculty of Enginering, Electronics Engineering Department

## Project Overview

This experiment focuses on understanding and applying various functions from the NumPy library in Python. The goal is to implement and solve the following problems:

1. Normalization Problem: Implement the normalization process for a given ndarray. <br/>
2. Divisible by 3 Problem: Create a 10x10 ndarray of squares of the first 100 integers and determine the elements divisible by 3.
---
## Table of Contents
1. [Intended Learning Outcomes](#intended-learning-outcomes)
2. [Problem Descriptions](#problem-descriptions)
3. [Installation Instructions](#installation-instructions)
4. [Usage](#usage)
5. [Files Included](#files-included)
6. [Technologies Used](#technologies-used)
7. [License](#license)
8. [Author](#author)
---
## Intended Learning Outcomes
1. Identify the various codes and functions incorporated in the NumPy library.<br/>
2. Apply different NumPy codes and functions to create Python programs.
---
## Problem Descriptions

### Normalization Problem: <br/>
- Objective: Normalize a random 5x5 ndarray.<br/>
- Mathematical Formula:<br/>
<img width="115" alt="image" src="https://github.com/user-attachments/assets/06ae3aee-c5f0-42c9-b46f-a61d42e59bbc"><br/>

- Where:<br/>
  - X is the ndarray,<br/>
  - x̄ is the mean of the array,<br/>
  - σ is the standard deviation of the array.<br/>

- Task:<br/>
  - Create a random 5x5 ndarray using NumPu.<br/>
  - Normalize the ndarray using element-wise operations (using .mean() and .std()).<br/>
  - Save the normalized ndarray as X_normalized.npy<br/>

- Code sample:
```
import numpy as np

# Create a random 5x5 ndarray
X = np.random.rand(5, 5)

# Normalize the array using the formula Z = (X - mean) / std
X_mean = X.mean()
X_std = X.std()
X_normalized = (X - X_mean) / X_std

# Save the normalized ndarray as 'X_normalized.npy'
np.save('X_normalized.npy', X_normalized)

# Print the normalized array
print("Normalized Array:\n", X_normalized)
```

### Divisible by 3 Problem: <br/>
- Objective: Create a 10x10 ndarray of the squares of the first 100 integers, and extract elements divisible by 3. <br/>

- Task:<br/>
  - Contruct a 10x10 ndarray where the values are squares of integers from 1 to 100.<br/>
  - Identify elements divisible by 3.<br/>
  - Save the results as div_by_3.npy.<br/>
  
- Code sample:
```
import numpy as np

# Create a 10x10 ndarray of the squares of the first 100 positive integers
A = np.arange(1, 101).reshape(10, 10) ** 2

# Filter out the elements that are divisible by 3
div_by_3 = A[A % 3 == 0]

# Save the result as 'div_by_3.npy'
np.save('div_by_3.npy', div_by_3)

# Print the array to see the result
print("Elements Divisible by 3:\n", div_by_3)

```
---
## Installation Instructions

To run the provided python code, ensure you have the following installed:<br/>
1. Python (Version 3.6 or higher) <br/>
2. Jupyter Notebook <br/>
3. NumPy library <br/>

### Installation steps:<br/>
1. Clone the repository:<br/>
```git clone https://github.com/draemonsi/experiment-2-numpy.git``` <br/>
2. Navigate to the project folder: <br/>
```cd experiment-2-numpy``` <br/>
3. INstall dependencies (if NumPy is not installed):<br/>
```pip install numpy```<br/>
---
## Usage
1. Open jupyter notebook in your environment:<br/>
```jupyer notebook```<br/>
2. Navigate to the notebook containing the experiment code and run the cells sequentially.<br/>
3. Upon running the code, two .npy files will be generated:<br/>
   - X_normalized.npy: Contains the normalized 5x5 ndarray.<br/>
   - div_by_3.npy: Contains the elements from the 10x10 ndarray that are divisible by 3.<br/>
---
## Files included
- PA2.ipynb: Jupyter notebook with the Python code for both problems.
- X_normalized.npy: Output file containing the normalized ndarray.
- div_by_3.npy: Output file containing elements divisible by 3.
- ---
## Technologies Used
- Python (version 3.x)
- NumPy (Numerical Python Library)
- Jupyter Notebook for code execution and analysis
---
## License<br/>
- This project is licensed under The Unlicense. Please see [LICENSE](https://github.com/draemonsi/ECE2112-Experiment2/blob/main/LICENSE.txt) file for more details.
---
## Author<br/>
- Andrei Jorelle C. Simon<br/>
  [GitHub Profile](https://github.com/draemonsi)


