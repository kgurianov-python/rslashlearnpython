import csv

openfile = open("mvehpop_dataset.csv")
csvreader = csv.reader(openfile)
next(csvreader)


def meanvehpop(category):
    sel = input("Please select A, B, C, D, E, F or Q:")
    datarows = []
    month = []
    vehicle_type = []

    if sel == "A" or sel == "a":
        vehicle_type = datarows[1]
    elif sel == "B" or sel == "b":
        vehicle_type = datarows[2]
    elif sel == "C" or sel == "c":
        vehicle_type = datarows[3]
    elif sel == "D" or sel == "d":
        vehicle_type = datarows[4]
    elif sel == "E" or sel == "e":
        vehicle_type = datarows[5]
    elif sel == "F" or sel == "f":
        vehicle_type = datarows[6]
    else:
        print("Sorry, invalid entry. PLease try again.")

    for row in range(8, 11):
        datarows.append(row)

        month = datarows[0]
        vehicle_type = datarows[category]
        average = sum(vehicle_type) / len(month)

    print("Mean vehicle population in the 4-month span of August to Novmember")

    print(f"Mean Value:{average}")
