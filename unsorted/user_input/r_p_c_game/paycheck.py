STANDARD_HOURS = 40.0
OVERTIME_COEFFICIENT = 1.5


def main():
    pay_rate = float(input("Enter your hourly pay rate: $"))
    hours_worked = float(input("Enter hours worked: "))

    standard_hours = min(STANDARD_HOURS, hours_worked) # Standard hours  not more than 40
    overtime_hours = max(0, hours_worked - STANDARD_HOURS) # if hours_worked < STANDARD_HOURS, overtime is 0

    gross_pay = standard_hours * pay_rate + overtime_hours * (pay_rate * OVERTIME_COEFFICIENT)
    print(f"Total Pay: {gross_pay}")


if __name__ == '__main__':
    main()
