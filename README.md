# Demographic Data Analyzer

This project analyzes demographic data from the 1994 Census database using Pandas. It answers a series of questions about the dataset, providing insights into race distribution, gender-based age averages, education levels, salary comparisons, and more.

## Project Description

The project processes a dataset containing demographic information extracted from the 1994 Census database. The data includes details such as age, workclass, education, marital status, occupation, race, sex, capital gains, capital losses, hours worked per week, native country, and salary.

The analysis focuses on answering the following questions using the Pandas library:

1.  **Race Distribution:** How many people of each race are represented in the dataset?
2.  **Average Age of Men:** What is the average age of men in the dataset?
3.  **Bachelor's Degree Percentage:** What percentage of people in the dataset have a Bachelor's degree?
4.  **Advanced Education vs. High Salary:** What percentage of people with advanced education (Bachelors, Masters, or Doctorate) earn more than 50K?
5.  **No Advanced Education vs. High Salary:** What percentage of people without advanced education earn more than 50K?
6.  **Minimum Work Hours:** What is the minimum number of hours a person works per week in the dataset?
7.  **Minimum Work Hours & High Salary:** What percentage of people who work the minimum number of hours per week have a salary of more than 50K?
8.  **Highest Earning Country:** What country has the highest percentage of people that earn >50K, and what is that percentage?
9.  **Top Occupation in India:** What is the most common occupation for those who earn >50K in India?

## Data Description

The dataset is a CSV file (`adult.data.csv`) with the following columns:

| Column           | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| `age`            | Age of the individual.                                                           |
| `workclass`      | Type of employment (e.g., State-gov, Private).                                   |
| `fnlwgt`         | Final weight, a statistical weight assigned by the Census Bureau.                |
| `education`      | Highest level of education achieved.                                             |
| `education-num`  | Number of years of education.                                                    |
| `marital-status` | Marital status (e.g., Married-civ-spouse, Never-married).                        |
| `occupation`     | Occupation of the individual.                                                    |
| `relationship`   | Relationship status within the household.                                        |
| `race`           | Race of the individual.                                                          |
| `sex`            | Gender of the individual.                                                        |
| `capital-gain`   | Capital gains for the individual.                                                |
| `capital-loss`   | Capital losses for the individual.                                               |
| `hours-per-week` | Number of hours worked per week.                                                 |
| `native-country` | Country of origin.                                                               |
| `salary`         | Salary range (<=50K or >50K).                                                    |

## File Structure

demographic_data_analyzer/ 
├── src/ 
│   └── demographic_data_analyser.py # Main Python script 
├── data/ 
│   └── adult.data.csv # The dataset 
└── README.md # This file


## How to Run

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd demographic_data_analyzer
    ```

2.  **Place the dataset:**
    Ensure that the dataset `adult.data.csv` is located in the `data` directory.

3.  **Run the Script:**
    Execute the main Python script:
    ```bash
    python src/demographic_data_analyser.py
    ```

    This will run the analysis and print the results to the console.

## Code Description

The main logic is in `src/demographic_data_analyser.py`. It contains the following functions:

*   `load_data(file_path)`: Loads the dataset from a CSV file into a Pandas DataFrame.
*   `calculate_race_count(df)`: Calculates the number of people of each race.
*   `calculate_average_age_men(df)`: Calculates the average age of men.
*   `calculate_percentage_bachelors(df)`: Calculates the percentage of people with a Bachelor's degree.
*   `calculate_higher_education_rich(df)`: Calculates the percentage of people with advanced education who earn >50K.
*   `calculate_lower_education_rich(df)`: Calculates the percentage of people without advanced education who earn >50K.
*   `find_min_work_hours(df)`: Finds the minimum number of hours worked per week.
*   `calculate_rich_percentage_min_hours(df)`: Calculates the percentage of people who work the minimum hours and earn >50K.
*   `find_highest_earning_country(df)`: Finds the country with the highest percentage of people who earn >50K.
*   `find_top_occupation_india(df)`: Finds the most common occupation for those who earn >50K in India.
* `calculate_demographic_data(print_data=True)`: Calculates all the demographics and prints the results.

The function `calculate_demographic_data` orchestrates the calculations and can print the results if `print_data` is set to `True`.

## Dependencies:

    - Python 3
    - Pandas

You can install pandas by:
    ```bash
    pip install pandas
    

## Results

The script outputs the following results to the console:

*   Number of each race.
*   Average age of men.
*   Percentage with Bachelor's degrees.
*   Percentage with higher education that earn >50K.
*   Percentage without higher education that earn >50K.
*   Minimum work hours per week.
*   Percentage of rich among those who work fewest hours.
*   Country with the highest percentage of rich.
*   Highest percentage of rich people in any country.
*   Top occupations in India for those with salary >50K.

Each result is also returned in a dictionary for further usage.
