# Traffic Light Simulator Challenge
Please write a program that draws and operates a traditional traffic light. The program should take input from a user about how long each light color should stay lit before transitioning. A graphical user interface or ASCII art are equally acceptable. Color transitions should be visible to the user. As your software will be used to operate critical infrastructure a user must not be able to crash the software. You must provide the user a mechanism for safely exiting your program. You must print ‘Exiting Traffic Light Simulator’ to the screen when the user instructs the program to exit.

You must complete this challenge in Python. You must provide a README file to explain how to build/install and operate your software. Your submission must be your own work.

*Evaluation criteria*
- You followed instructions
- Software functions as requested and meets all stated requirements
- Software is designed for easy extensibility. You will be asked how your software must be
modified to accommodate new use-cases and traffic light designs. You will not be provided
with descriptions of these variants at this time.
- Software is designed and implemented for testability
- Software is designed and implemented to support packaging and delivery
- Software is understandable and would be easily supported by a developer other than yourself

## Running my Solution
Go inside the traffic_light_simulator folder with the traffic_light.py file within the terminal
```cd traffic_light_simulator```

Run traffic_light.py with python3 within the terminal
```python3 traffic_light.py```

You can exit by typing 'exit' without the quotes while running the script
```exit```

Enter a positive number for the time delay (seconds) between color changes
```5```

The traffic light should go from red (top) to yellow (middle) to green (bottom) and let you enter a different value afterwards

Run Unit Tests by running tests.py
```python3 tests.py```
