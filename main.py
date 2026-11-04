from functions.reader import merge_vehicles, read_cars, read_trucks, save_vehicles


def main():
    trucks = read_trucks("data/trucks.txt")
    cars = read_cars("data/cars.json")
    # print("\nTrucks:\n")
    # print(trucks)
    # print("\nCars:\n")
    # print(cars)
    vehicles = merge_vehicles(trucks, cars)
    # print("\nVehicles:\n")
    # print(vehicles)
    save_vehicles(vehicles, "data/vehicles.csv")
    print("Vehicles successfully saved!")


if __name__ == "__main__":
    main()
