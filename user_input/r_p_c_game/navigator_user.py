import os
import matplotlib.pyplot as plt

GRID_SIZE = 12

def print_grid(coords):
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x, y in coords:
        if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
            print('Error: The route is outside of the grid')
            return
        grid[y][x] = 'X'
    for row in grid:
        print(' '.join(row))

def main():
    # Set the directory path
    directory_path = r"routes/"

    # Check if the directory and files exist
    if not os.path.exists(directory_path):
        print("Directory not found")
        return

    # Define the file names
    ROUTE_FILE_NAMES = ["Route 1.txt", "Route 2.txt", "Route 3.txt"]

    # Check if all files exist
    if not all(os.path.exists(os.path.join(directory_path, file_name)) for file_name in ROUTE_FILE_NAMES):
        print("Not all route files found")
        return

    while True:
        route_num = input('Enter a route number (1, 2, 3, or stop): ')
        if route_num == 'stop':
            break
        try:
            with open(os.path.join(directory_path, f"Route {route_num}.txt")) as route_file:
                route_content = route_file.read()
                #initial Data
                grid = [['.'] * 12 for i in range(12)]
                coords = [(3,12)]

                #Replace coordinates in grid with X
                for c in coords:
                    grid[c[1]-1][c[0]-1] = 'x'


                #Display grid
                for row in grid[::-1]:
                    print(' '.join(row))

                print(f"Route {route_num} coordinates:")
                print_grid(coords)

        except FileNotFoundError:
            print(f"File not found for Route {route_num}")



    # Create a 12x12 grid with all values set to 0
    grid = [[0]*12 for _ in range(12)]

    # Read the file and populate the grid with the coordinates
    with open('coordinates.txt') as f:
        for line in f:
            x, y = map(int, line.strip().split(','))
            grid[y-1][x-1] = 1

    # Plot the grid
    fig, ax = plt.subplots()
    ax.set_xticks(range(13))
    ax.set_yticks(range(13))
    ax.grid()
    ax.invert_yaxis()

    for y in range(12):
        for x in range(12):
            if grid[y][x] == 1:
                ax.text(x+0.5, 11.5-y+0.5, 'x', ha='center', va='center', fontsize=14)


    plt.show()

if __name__ == '__main__':
    main()