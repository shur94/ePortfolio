# ePortfolio_
This is my portfolio of learning outcome from Object Oriented Programming based on submitted assignments. 

## Driverless Car System Implementation

This assignment focuses on implementing the software components necessary to support the operation of a driverless car, as outlined in the provided class diagram from system design, however, it has been amended from the initial version.

![image](https://github.com/shur94/ePortfolio/assets/152515871/726b51ad-3538-4d66-a3d3-2b0b461a1cf7)

This README includes the implementation of software components necessary to support the operation of a driverless car. 

Below, you'll find a description of the code and the testing code specifically for the system along with instructions on how to execute the code.

### Driverless System

driverless_system.py
It consists of several classes that simulate the functionality of a driverless car system. Here's an overview of each class:

#### DriverlessSystem:
This class represents the main system controlling the driverless car.

It has methods to make decisions, detect obstacles, and store data.

The make_decision method decides whether to proceed or halt based on obstacle detection.

The detect_obstacle method simulates the detection of obstacles using a camera. 

To avoid any doubt, it will need to be replaced once being implemented in the real system.

The store_data method stores captured image data in the Data class.

#### Camera:
This class represents the camera module of the driverless car.

It has a method capture_image that simulates capturing an image. 

To avoid any doubt, it will need to be replaced once being implemented in the real system.

For demonstration purposes, it returns a placeholder image.

#### Data:
This class represents the data storage module of the driverless car.

It has a method store_data to store captured image data.

#### Obstacle:
This class represents the obstacle detection module of the driverless car.

It has an attribute detected to simulate obstacle detection.

#### Decision:
This class represents the decision-making module of the driverless car.

It has an attribute result to store the decision (proceed or halt).

test_driverless_system.py

### Testing Code
The testing code uses the unittest(Python, n.d.) framework to test the functionality of the driverless car system. 

Here's a description of the test cases:

#### test_make_decision: 
Tests the make_decision method of the DriverlessSystem class. 

It verifies whether the system makes the correct decision based on obstacle detection.

#### test_detect_obstacle: 
Tests the detect_obstacle method of the DriverlessSystem class. 

It ensures that the system detects obstacles correctly.

#### test_store_data:
Tests the store_data method of the DriverlessSystem class. 

It checks whether the system stores data correctly after capturing an image.
 

### References
Python (n.d.). unittest — Unit testing framework — Python 3.8.2 documentation. [online] docs.python.org. Available at: https://docs.python.org/3/library/unittest.html. 
