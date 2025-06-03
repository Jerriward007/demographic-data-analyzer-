# main.py

from demographic_data_analyzer import calculate_demographic_data

# Run the function and capture the returned results
result = calculate_demographic_data()

# Optional: print specific values to verify results
print("\nSummary:")
print("Average age of men:", result['average_age_men'])
print("Percentage with Bachelor's degrees:", result['percentage_bachelors'])
print("Country with highest % of rich:", result['highest_earning_country'])
print("Top occupation in India for >50K earners:", result['top_IN_occupation'])
