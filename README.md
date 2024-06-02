# ePortfolio
This is a portfolio to present my learning outcomes from Object Oriented Programming module.

</br>

## System Design
>https://github.com/shur94/ePortfolio_/tree/main/Implementation%20(Week%2011)

Assignment was to design a software to support driverless car.

As instructed, I have designed a software to assist the process of 'recognition of obstacles and logical decision of stopping the car'.

</br>
With references from various materials, I have completed designing on the basis of backgrounds as below:

- Use Case Diagram: to present foundtaional architecure of the software

- Class Diagram: to present data types and classes that will be used in the software

- Activity Diagram: to represent the flow of activities to illustrate the software's behaviour

</br>
Although the final piece of the design still lacks many details that could have been used to improve, the design was created to progres

### Self assessment
#### 1. Overall
With given feedback and grade, the initial design lack of completed tasks.

Considering the quality of findings, the expertise to a certain level is not achieved, and it clearly needs to improve.

#### 2. Understanding
Even though I cited and referred some external knowledge, it cannot be confidently said that those were correctly implemented in my work.

Since I lack fundamental knowledge, which partially were satisfied through previous modules, I may needed more time and effort to follow up such scarcity.

However, I tried to simplify the whole process, which eventually became a final design that can be compiled as python codes.

### System Implementation
https://github.com/shur94/ePortfolio_/tree/main/System%20Design%20(Week%207)

Next assignment was to build a software to support driverless car, based on system design that was previously submitted.

As instructed, I have completed coding process (python) for a software.

</br>
Again, with references from various materials, following two codings are created:

#### 1. driverless_system.py

It consists of several classes that simulate the functionality of a driverless car system with classes as below:

#### DriverlessSystem:
This class represents the main system controlling the driverless car.

It has methods to make decisions, detect obstacles, and store data.

- The make_decision method decides whether to proceed or halt based on obstacle detection.

- The detect_obstacle method simulates the detection of obstacles using a camera.

- The store_data method stores captured image data in the Data class.

#### Camera:

This class represents the camera module of the driverless car.

- The capture_image method simulates capturing an image.
>For demonstration purposes, it returns a placeholder image.

#### Data:
This class represents the data storage module of the driverless car.

- The store_data method to store captured image data.

#### Obstacle:
This class represents the obstacle detection module of the driverless car.

- An attribute detected to simulate obstacle detection.

#### Decision:
This class represents the decision-making module of the driverless car.

- An attribute result to store the decision (proceed or halt).
