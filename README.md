# Restaurant Review Analysis 🍽️
## About the Project

Restaurants constantly receive feedback through customer reviews. Whether positive or negative, these reviews contain valuable information that can help an establishment identify common issues and areas for improvement.

The objective of this Python program is to analyze restaurant reviews and determine the **most common complaints made by guests**.

## How It Works

The program reads reviews from a plain-text file called:

`restaurant_reviews.txt`

Each line in the file contains one customer review.

The program uses a dictionary of **complaint categories**, with each category mapped to a set of keywords commonly associated with that type of complaint.

For each review, the program:

1. Converts the review to lowercase for consistent matching.
2. Checks the review for keywords associated with each complaint category.
3. Classifies the review into all applicable complaint categories.
4. Labels reviews with no matching complaint keywords as **Neutral**.
5. Counts how frequently each complaint category appears.
6. Records the category assignments for each individual review.

A single review can be assigned to multiple complaint categories if it contains more than one type of issue.

## Features

The program includes an interactive menu that allows the user to:

- Run the restaurant review analysis
- View a summary of the results in the terminal
- Generate a detailed output file called `complaint_report.txt`

## Summary Output

The analysis displays:

- Total number of reviews analyzed
- Number of reviews associated with each complaint category
- Number of neutral reviews
- Most frequently identified complaint type

The generated `complaint_report.txt` file provides a more detailed breakdown of the results, including the classifications assigned to individual reviews.

## Project Files

- `restaurant_reviews.txt` - Input file containing one restaurant review per line
- `complaint_report.txt` - Generated output file containing the detailed analysis
- `README.md` - Project documentation
- `restaurant_review_analysis.py` - Contains the program used to analyze the reviews

## Running the Program

1. Make sure Python is installed on your computer.
2. Place `restaurant_reviews.txt` in the same project directory as the Python program.
3. Run `restaurant_review_analysis.py`.
4. Follow the menu prompts displayed in the terminal.
5. Choose whether to view the analysis summary or generate the detailed report.

## Python Concepts Used

This project demonstrates the use of several Python concepts, including:

- File reading and writing
- Dictionaries
- Sets
- Functions
- Loops
- Conditional statements
- String manipulation
- Keyword matching
- Data classification
- Frequency counting
- User input

## Purpose

The purpose of this project is to demonstrate how basic text analysis can be used to turn customer feedback into useful information.

By identifying recurring complaints, restaurants can better understand common guest concerns and determine areas where the customer experience could be improved.

## Data Set Citation

Vigneshwarsofficial. (n.d.). *Restaurant Customer Reviews* [Data set]. Kaggle.

https://www.kaggle.com/datasets/vigneshwarsofficial/reviews
