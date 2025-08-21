class Mircowave:
    def __init__(self, brand:str, power_rating:str):
        self.brand = brand
        self.power_rating = power_rating
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} microwave is now ON.")
        else:
            print(f"{self.brand} microwave is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} microwave is now OFF.")
        else:
            print(f"{self.brand} microwave is already OFF.")

    def __str__(self):
        return f"{self.brand} microwave with power rating {self.power_rating}"
    
    def __repr__(self):
        return f"Mircowave({self.brand!r}, {self.power_rating!r})"
    
    def run(self, time:int):
        if self.is_on:
            print(f"{self.brand} microwave is running for {time} seconds.")
        else:
            print(f"{self.brand} microwave is OFF. Please turn it ON first.")


    
my_mircowave = Mircowave("Samsung", "800W")

print(str(my_mircowave),"\n")
my_mircowave.turn_off()
my_mircowave.run(30)
my_mircowave.turn_on()
my_mircowave.run(30)
my_mircowave.turn_off()



# --- IGNORE ---
# This code defines a Mircowave class with methods to turn it on, turn it off,
# and run it for a specified time. It also includes string representation methods.
# The main function demonstrates the usage of the Mircowave class.