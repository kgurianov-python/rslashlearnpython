"""
Write a program to determine how long it will take you to save a million dollars.

Assume that you invest your savings with an annual return (r) of 4% (i.e. r=0.04)
so that at the end of each month you receive current_savings*r/12 to put into your savings
(the 12 is because r is an annual rate).

In other words, your savings will be increased by the return on your investment,
plus the percentage of your monthly salary that you decide to save each month.

Of course, you won't have the same salary all your life, so assume that you will get a 3% raise every year.
"""

# Progression constants
ANNUAL_RETURN = 0.04
MONTHLY_RETURN = ANNUAL_RETURN / 12
ANNUAL_SALARY_RAISE = 0.03

# collect user inputs
annual_salary = float(input("Enter the amount of your starting annual salary: "))
percentage_saved = float(input("Enter the percentage that you want to save from your salary: "))
target = float(input("Enter the amount you would like to achieve: "))

# set basic multipliers and counters
savings_ratio = percentage_saved / 100
current_savings = 0  # we start with 0 current savings amount
months_counter = 0

# Calculate initial monthly salary, we will later recalculate it once a year
monthly_salary = annual_salary / 12

while current_savings < target:
    # basically, the new savings amount calculation
    current_savings += (current_savings * MONTHLY_RETURN) + (monthly_salary * savings_ratio)

    # Fail-safe, if the savings account has not increased (e.g. user saves 0% monthly) we will exit the loop
    # to avoid infinite loop
    if current_savings <= 0:
        print(f'You are not saving anything, you will be poor forever')
        break

    # we only count months. In the end, we will be able to transform this number to years / months
    months_counter += 1

    # every 12 months the annual salary is increased by ANNUAL_SALARY_RAISE
    if (months_counter % 12) == 0:
        # We can increase monthly_salary directly, this is just for code readability
        annual_salary = annual_salary * (1 + ANNUAL_SALARY_RAISE)
        monthly_salary = annual_salary / 12
        #  just for tracking annual salary increase, output current salary nce a year has passed
        print(f'New annual salary: {monthly_salary}')

    # tracking monthly savings progress
    print(f'Month {months_counter}; savings: {current_savings}')

print(f"You will reach you goal after {int(months_counter / 12)} years and {months_counter % 12} months. "
      f"By then you will have a saving account balance  of ${current_savings}")
