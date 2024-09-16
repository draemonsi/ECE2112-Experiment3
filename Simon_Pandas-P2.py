{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a475c76d-21a8-4196-8019-45f1ea24f888",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dad785af-d213-4d56-b9a6-dd0f823f743d",
   "metadata": {},
   "outputs": [],
   "source": [
    "cars = pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "028c1276-6793-4073-9797-b302b4c8d2d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n"
     ]
    }
   ],
   "source": [
    "# Part a: Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...)\n",
    "# By using the iloc function and setting the index to :5 and ::2 it means that it will display 5 columns with a 2 step interval\n",
    "first_five_odd_columns = cars.iloc[:5, ::2]\n",
    "print(first_five_odd_columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "1d1af660-1d85-483d-845f-ce28a40d2804",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n"
     ]
    }
   ],
   "source": [
    "# Part b: Display the row that contains the ‘Model’ of ‘Mazda RX4’.\n",
    "# Indexing with the given condition that if the value in the Model column is equal to Mazda RX4; it will display the row of that\n",
    "mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']\n",
    "print(mazda_rx4_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "902a38e2-7ee9-4095-b7c6-fe82ef12065b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23    8\n",
      "Name: cyl, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Part c: How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?\n",
    "# Indexing with the given condition that if the value in the Model is equal to Camaro Z28; it will display the 'cyl' column of that row\n",
    "cyl_camaro_z28 = cars[cars['Model'] == 'Camaro Z28']['cyl']\n",
    "print(cyl_camaro_z28)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e619cfca-0398-45fa-9263-c0431e9b8d51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "# Part d: Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models \n",
    "# ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.\n",
    "# Storing the model as string to models\n",
    "# Indexing with the given condition that if the value in models is equal to Model, if so; print the Model, Cyl, and gear columns of the rows\n",
    "models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']\n",
    "selected_cars = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]\n",
    "print(selected_cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ddc6c99-d735-4ff9-ac30-9faae85b4b53",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
