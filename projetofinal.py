import math

def Main():

    while(True):

        print("")
        print("What problem do you want to solve?")
        print("1. Floating")
        print("2. Springs")
        print("")

        command = input()

        if command == "1":

            Fluid()

        elif command == "2":

            Springs()

        elif command == "exit":
            exit()

        else:
            print("")
            print("Choose the problem that you want to solve by typing '1' for Floating or '2' for Springs")
            print("Type 'exit' if you want to exit the application")
            print("Let's try again...")
            print("")

def Fluid():

    # Default Variables
    mass = 20.00
    density = 4.00
    volume = 5.00
    fluidDensity = 1.00
    gravity = 9.81

    # Default Formulas to calculate some other needed variables
    edge = volume ** (1/3)
    volumeImmersed = (mass * gravity) / (fluidDensity * gravity)
    volumeHeightImmersed = volumeImmersed / (edge**2)

    while(True):
        print("")
        print(f"Object properties: Mass = {mass:.2f}, Density = {density:.2f}, Volume = {volume:.2f}")
        print(f"Fluid properties: Fluid Density = {fluidDensity:.2f}, Gravity = {gravity:.2f}")
        print(f"Object would float at {volumeHeightImmersed:.2f} meters. ")
        print("Use the command 'set [variable] [value]' to change a variable's value")
        print("Type 'back' to go back to the menu or 'exit' to exit the application")
        print("")

        var = input().lower().split()
        if var[0] == "set":
            if var[1] == "volume":
                volume = float(var[2])
                mass = density * volume
            elif var[1] == "density":
                density = float(var[2])
                mass = density * volume
            elif var[1] == "mass":  
                mass = float(var[2])
                density = mass / volume
            elif (var[1] == "fluid") and (var[2] == "density"):
                fluidDensity = float(var[3])   
            elif var[1] == "gravity":
                gravity = float(var[2]) 
        elif var[0] == "back":
            print("")
            break
        elif var[0] == "exit":
            exit()
        else:
            print("Use the command 'set [variable] [value]' to change a variable's value")
            print("Please try again...")

        # Formulas used
        edge = volume ** (1/3)
        volumeImmersed = (mass * gravity) / (fluidDensity * gravity)
        volumeHeightImmersed = volumeImmersed / (edge**2)

def Springs():
    gravity = 9.81
    mass = 1.50
    springLenght = 0.50
    constant = 0.20

    while(True):
        
        # Formulas used
        gravityForce = mass * (-gravity)
        stretchedSpring = (gravityForce/(-constant)) + springLenght

        print("")
        print(f"Object mass = {mass:.2f}, Gravity = {gravity:.2f}")
        print(f"Base spring lenght = {springLenght:.2f}, Constant = {constant:.2f}")
        print(f"Spring would stretch to {stretchedSpring:.2f} meters")
        print("Use the command 'set [variable] [value]' to change a variable's value")
        print("Type 'back' to go back to the menu or 'exit' to exit the application")
        print("")

        var = input().lower().split()
        if var[0] == "set":
            if var[1] == "mass":
                mass = float(var[2])              
            elif var[1] == "gravity":
                gravity = float(var[2])
            elif var[1] == "lenght":  
                springLenght = float(var[2])
        elif var[0] == "back":
            print("")
            break
        elif var[0] == "exit":
            exit()
        else:
            print("Use the command 'set [variable] [value]' to change a variable's value")
            print("Please try again...")

Main()