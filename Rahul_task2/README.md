# BMI Calculator

## Project Description
This is an Advanced BMI (Body Mass Index) Calculator developed using Python and Tkinter. 
The application allows users to enter their name, weight, and height, calculates BMI, 
displays the corresponding health category, and stores the results in a CSV file with a timestamp.

## Features
- Graphical User Interface (GUI) using Tkinter
- Name input
- Weight and height input
- BMI calculation
- Health category classification
- Input validation
- Error pop-up messages
- Automatic data storage in CSV file
- Timestamp for each record

## Technologies Used
- Python 3
- Tkinter
- CSV Module
- Datetime Module

## BMI Formula
BMI = Weight (kg) / Height² (m²)

## BMI Categories
- Underweight: BMI < 18.5
- Normal Weight: 18.5 ≤ BMI < 25
- Overweight: 25 ≤ BMI < 30
- Obesity: BMI ≥ 30

## How to Run
1. Open the project folder in VS Code.
2. Run the following command:

python main.py

3. Enter your name, weight, and height.
4. Click the "Calculate BMI" button.
5. View the BMI result and category.

## Sample Output
Name: Rahul
Weight: 70 kg
Height: 1.75 m
BMI: 22.857
Category: Normal Weight

## Files in the Project
- main.py - Main Python source code
- README.md - Project documentation
- bmi_data.csv - Stores BMI calculation history

## Author
Rahul R