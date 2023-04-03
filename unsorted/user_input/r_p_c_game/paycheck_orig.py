STANDARD_HOURS = 40.0
OVERTIME_COEFFICIENT = 1.5

FED_INC_TAX = 0.28
STATE_INC_TAX = 0.00
OASDI_TAX = 0.062
MEDICARE_TAX = 0.0145


def main():
    # Get Inputs
    emp_fname = input("Enter your first name: ")
    emp_lname = input("Enter your last name: ")
    emp_ID = int(input("Enter your 6-digit Employee ID: "))
    pay_rate = float(input("Enter your hourly pay rate: $"))
    hours_worked = float(input("Enter hours worked: "))

    # Calculate overtime and gross pay
    regular_hours = min(STANDARD_HOURS, hours_worked)  # Standard hours  not more than 40
    overtime_hours = max(0, hours_worked - STANDARD_HOURS)  # if hours_worked < STANDARD_HOURS, overtime is 0

    regular_pay = regular_hours * pay_rate
    overtime_pay_rate = pay_rate * OVERTIME_COEFFICIENT
    overtime_pay = overtime_hours * overtime_pay_rate
    gross_pay =  regular_pay + overtime_pay

    # Calculate tax deductions
    # ~Calculate tax withholdings
    fed_tax_wh = gross_pay * FED_INC_TAX
    state_tax_wh = gross_pay * STATE_INC_TAX
    oasdi_tax_wh = gross_pay * OASDI_TAX
    medicare_tax_wh = gross_pay * MEDICARE_TAX

    # Calculate net pay
    net_pay = gross_pay - fed_tax_wh - state_tax_wh - oasdi_tax_wh - medicare_tax_wh
    deduct_total = fed_tax_wh + state_tax_wh + oasdi_tax_wh + medicare_tax_wh

    # Underline Formatting
    class Format:
        end = '\033[0m'
        underline = '\033[4m'

    # Earnings Statement
    print("\n")
    title = "EARNINGS STATEMENT"
    centered_title = title.center(48, " ")
    print(centered_title)
    print("\nName: {} {}\t\t\tEmployee ID: {}".format(emp_fname, emp_lname, emp_ID))
    print("\nEARNINGS")
    print(Format.underline + "\t\t\t\trate\t\t\thours\t\t\tthis period" + Format.end)
    print("Regular \t\t{:>5,.2f}\t\t\t{:>7,.2f}\t\t\t{:>10,.2f}".format(pay_rate, regular_hours, regular_pay))
    print(
        "Overtime\t\t{:>5,.2f}\t\t\t{:>7,.2f}\t\t\t{:>10,.2f}".format(overtime_pay_rate, overtime_hours, overtime_pay))
    print("\nDEDUCTIONS")
    print(Format.underline + "\t\t\t\tStatutory\t\t\t\t\t\tthis period" + Format.end)
    print("FICA\t\t\tFederal Income Tax\t\t\t\t{:=12,.2f}".format(-1 * fed_tax_wh))
    print("\t\t\t\tSocial Security Tax\t\t\t\t{:=12,.2f}".format(-1 * oasdi_tax_wh))
    print("\t\t\t\tMedicare Tax\t\t\t\t\t{:=12,.2f}".format(-1 * medicare_tax_wh))
    print("-" * 60)
    print("\t\t\t\tState Income Tax\t\t\t\t{:=12,.2f}".format(-1 * state_tax_wh))
    print("\n\t\t\t\tNet Pay\t\t\t\t\t\t\t${:>12,.2f}".format(net_pay))


if __name__ == '__main__':
    main()
