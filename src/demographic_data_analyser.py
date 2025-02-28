import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_race_count(df):
    return df['race'].value_counts()

def calculate_average_age_men(df):
    return round(df[df['sex'] == 'Male']['age'].mean(), 1)

def calculate_percentage_bachelors(df):
    return round((df['education'] == 'Bachelors').mean() * 100, 1)

def calculate_higher_education_rich(df):
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    return round(
        (df[df['education'].isin(advanced_education)]['salary'] == '>50K').mean() * 100, 1
    )

def calculate_lower_education_rich(df):
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    return round(
        (df[~df['education'].isin(advanced_education)]['salary'] == '>50K').mean() * 100, 1
    )

def find_min_work_hours(df):
    return df['hours-per-week'].min()

def calculate_rich_percentage_min_hours(df):
    min_hours = df['hours-per-week'].min()
    return round(
        (df[df['hours-per-week'] == min_hours]['salary'] == '>50K').mean() * 100, 1
    )

def find_highest_earning_country(df):
    country_percentages = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').mean() * 100
    )
    return country_percentages.idxmax(), round(country_percentages.max(), 1)

def find_top_occupation_india(df):
    return df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

def calculate_demographic_data(print_data=True):
    df = load_data('../data/adult.data.csv')

    race_count = calculate_race_count(df)
    average_age_men = calculate_average_age_men(df)
    percentage_bachelors = calculate_percentage_bachelors(df)
    higher_education_rich = calculate_higher_education_rich(df)
    lower_education_rich = calculate_lower_education_rich(df)
    min_work_hours = find_min_work_hours(df)
    rich_percentage = calculate_rich_percentage_min_hours(df)
    highest_earning_country, highest_earning_country_percentage = find_highest_earning_country(df)
    top_IN_occupation = find_top_occupation_india(df)

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }