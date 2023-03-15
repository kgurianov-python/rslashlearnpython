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

# we start with 0 current savings amount
current_savings = 0
months_counter = 0

# Calculate initial monthly salary, we will later recalculate it once a year
monthly_salary = annual_salary / 12
while current_savings < target:
    # basically, the new savings amount calculation
    current_savings += (current_savings * MONTHLY_RETURN) + (monthly_salary * savings_ratio)

    # Fail-safe, if the savings account has not increased (e.g. user saves 0% monthly) we will exit the loop to avoid infinite loop
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