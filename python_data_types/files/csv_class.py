import csv


class Employee:
    all = []

    def __init__(self, name, ID, Department):
        self.name = name
        self.ID = ID
        self.Department = Department

    @classmethod
    def import_info_csv(cls):
        with open('company.csv', 'r') as f:
            reader = csv.DictReader(f)
            employee_list = list(reader)

        for employee_list in employee_list:
            cls.all.append(
                Employee(
                    name=employee_list.get('name'),
                    ID=employee_list.get('ID'),
                    Department=employee_list.get('Department')
                ))


def main():
    Employee.import_info_csv()
    print(Employee.all)


if __name__ == '__main__':
    main()
