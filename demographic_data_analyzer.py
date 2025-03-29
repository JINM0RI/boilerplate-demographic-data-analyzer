import pandas as pd



def calculate_demographic_data(print_data=True):
    # Read data from file
    df=pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count=df['race'].value_counts()
    print(race_count.tolist())

    # What is the average age of men?
    df1=df.copy()
    df1=df1.set_index('sex')
    MALE=df1.loc['Male']
    MALE_AGE=MALE['age'].mean()
    average_age_men = MALE_AGE.round(1)
    print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    edu_count=df['education'].value_counts()
    percentage_bachelors = round((edu_count['Bachelors']/edu_count.sum())*100,1)
    print(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education =df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    higher_education_salary= len(higher_education[higher_education['salary']=='>50K'])
    higher_education_rich =round((higher_education_salary/len(higher_education))*100,1)
    lower_education_salary=len(lower_education[lower_education['salary']=='>50K'])
    lower_education_rich = round((lower_education_salary/len(lower_education))*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work=df[df['hours-per-week']==min_work_hours]
    salles=min_work[min_work['salary']=='>50K']
    num_min_workers = len(salles['hours-per-week'])

    rich_percentage=(num_min_workers/len(min_work))*100

    # What country has the highest percentage of people that earn >50K?
    salary50K=df[df['salary']=='>50K']
    countary_count=df['native-country'].value_counts()
    high_country=salary50K['native-country'].value_counts()
    pp=round((high_country/countary_count)*100,1)
    highest_earning_country = pp.idxmax()
    highest_earning_country_percentage = pp.max()

    # Identify the most popular occupation for those who earn >50K in India.
    ind50K=salary50K[salary50K['native-country']=='India']
    ind_occ=ind50K['occupation'].value_counts()
    top_IN_occupation = ind_occ.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
