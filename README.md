# Experiment 3: Python Data Analysis (PANDAS)

## Course: ECE 2112 - Advanced Computer Programming and Algorithms <br/>
**Institution**: University of Santo Tomas, Faculty of Engineering, Electronics Engineering Department

## Project Overview

This experiment focuses on understanding and applying various DataFrame manipulation techniques using the Pandas library in Python. The goal is to implement and solve the following problems related to slicing, indexing, and subsetting a DataFrame:

1. Extract odd-numbered rows and columns from a given DataFrame.<br/>
2. Retrieve specific rows and columns using indexing.<br/>
3. Query and manipulate the data based on specific conditions.
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
1. Understand the basics of DataFrame indexing and slicing in Pandas.<br/>
2. Apply various DataFrame operations such as selecting specific rows, filtering data, and applying conditions.<br/>
3. Retrieve data based on column and row conditions using subsetting and slicing techniques.
---
## Problem Descriptions
### Problem 1
- **Objective:** Load the corresponding .csv file into a data frame named cars using pandas.<br/>
  - Task:<br/>
    - Use pd.read_csv to load the cars.csv<br/>
  - Code sample:
```
cars = pd.read_csv('cars.csv')
```
- **Objective:** Display the first five and last five rows of the resulting cars.<br/>
  - Task: <br/>
    - Use pd.concat to concatenate the first five and last rows: cars.head(), cars.tail()<br/>
  - Code sample:
```
print(pd.concat([cars.head(), cars.tails()])
```

### Problem 2
- **Objective:** Extract the first five odd-numbered columns (1, 3, 5, 7...) from the given DataFrame.<br/>
  - Task:<br/>
    - Use the Pandas iloc function to select odd-numbered columns.
    - Display the first five odd-numbered rows.<br/>
  - Code sample:
```
print(cars.iloc[:5,::2]
```
- **Objective:** Extract the row that contains the 'Model' of 'Mazda RX4'.<br/>
  - Task:<br/>
    - Use the Pandas loc function to retrieve the row containing the car model 'Mazda RX4'.<br/>
  - Code sample:
```
print(cars[cars['Model'] == 'Mazda RX4']
```
- **Objective:** Determine how many cylinders ('cyl') the car model 'Camaro Z28' has.<br/>
  - Task:<br/>
    - Filter the DataFrame to find the row for 'Camaro Z28' and retrieve the number of cylinders.<br/>
  - Code sample:
```
print(cars[cars['Model'] == 'Camaro Z28']['cyl']
```
- **Objective:** Retrieve the number of cylinders ('cyl') and gear type ('gear') for the car models: 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.<br/>
  - Task:<br/>
    - Use the Pandas isin() method to filter for these models and display the required columns.<br/>
  - Code sample:
```
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
selected_cars = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
print(selected_cars)
```
---
## Installation Instructions

To run the provided Python code, ensure you have the following installed:<br/>
1. Python (Version 3.6 or higher) <br/>
2. Jupyter Notebook <br/>
3. NumPy library <br/>

### Installation steps:<br/>
1. Clone the repository:<br/>
```git clone https://github.com/draemonsi/ECE2112-Experiment3.git``` <br/>
2. Navigate to the project folder: <br/>
```cd experiment-3-pandas``` <br/>
3. Install dependencies (if Pandas is not installed):<br/>
```pip install pandas```<br/>
---
## Usage
1. Open the Python environment (Jupyter Notebook, VS Code, etc.).<br/>
2. Load the provided dataset into a Pandas DataFrame.<br/>
3. Run the code snippets for each problem sequentially.<br/>
4. Upon running the code, you'll see the output directly in your environment.
---
## Files included
- Simon_Pandas-P1.py: Python file containing the solution to Problem 1<br/>
- Simon_Pandas-P2.py: Python file containing the solution to Problem 2<br/>
- cars.csv: Excel file containing the data of cars
---
## Technologies Used
- Python (version 3.x)
- Pandas (Python Data Analysis Library)
- Jupyter Notebook for code execution and analysis
---
## License<br/>
- This project is licensed under The Unlicense. Please see [LICENSE](https://github.com/draemonsi/ECE2112-Experiment3/blob/main/LICENSE.txt) file for more details.
---
## Author<br/>
- Andrei Jorelle C. Simon<br/>
  [GitHub Profile](https://github.com/draemonsi)


