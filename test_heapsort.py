import heapsort

if __name__ == "__main__":
    starting_array = []
    print("Enter a number, then press enter. Repeat this any number of time. This is your starting array. Enter 'X' or nothing to end input.")
    running = True
    while running:
        new_input = input()
        if new_input in ("X", "x", ""):
            running = False
            break
        if not new_input.isnumeric():
            print("Input must be a number! Ignoring this input.")
        else:
            starting_array.append(int(new_input))
    
    heapsort.heapsort(starting_array)
    