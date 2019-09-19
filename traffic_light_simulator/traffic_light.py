import time
import sys
from traffic_light_designs import traffic_lights_array, traffic_light_all


class TrafficLight:

    # Setup properties with time st
    def __init__(self, time=0, traffic_lights_array=traffic_lights_array):
        self.time = time
        self.traffic_lights_array = traffic_lights_array
        if __name__ == "__main__":
            self.setup()


    def setup(self):
        print(
'''
Traffic Light Simulator
You can exit the program any time by typing in exit
Enter time in seconds between light changes:
'''
)
        print(traffic_light_all)
        self.awaiting_user_input()


    def awaiting_user_input(self):
        user_input = input('> ')
        if (user_input == 'exit'):
            self.exit_simulator()
        
        if self.checkInput(user_input):
            self.time = float(user_input)
            self.change_light()
        else:
            self.awaiting_user_input()

        
    def checkInput(self, user_input):
        try:
            valid_int = float(user_input)
            if (valid_int <= 0):
                raise ValueError
            return True

        except ValueError:
            print("Not a valid input. Enter a number greater than 0.")
            return False


    def exit_simulator(self):
        print("Exiting Traffic Light Simulator")
        time.sleep(1)
        sys.exit()


    def change_light(self):
        for index, light in enumerate(self.traffic_lights_array):
            print(light)
            if (index != 2):
                time.sleep(self.time)
            else:
                time.sleep(1)
        if __name__ == "__main__":
            self.setup()


if __name__ == "__main__":
    TrafficLight()
