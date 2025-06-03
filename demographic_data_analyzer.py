import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv('adult.data.csv')

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education: Bachelors, Masters, Doctorate
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Min work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage earning >50K among min-hour workers
    min_hour_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_hour_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest % of >50K earners
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    rich_country_ratio = (rich_by_country / country_counts).fillna(0)
    highest_earning_country = rich_country_ratio.idxmax()
    highest_earning_country_percentage = round(rich_country_ratio.max() * 100, 1)

    # 8. Top occupation in India for >50K earners
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Output dictionary
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Higher education rich: {higher_education_rich}%")
        print(f"Lower education rich: {lower_education_rich}%")
        print("Min work time:", min_work_hours, "hours/week")
        print(f"Rich percentage of min hour workers: {rich_percentage}%")
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

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
