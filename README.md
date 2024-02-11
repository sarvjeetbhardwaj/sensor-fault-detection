# sensor-fault-detection

# Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

# Solution Proposed
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

# Tech Stack Used
1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions

# How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.
Replace the  value of 'mongo_db_url' with your own collection's mongodburl on sensor.configuration.mongo_db_connection.py file

# DataCollection
![alt text](image.png)

# Project Architecture
![alt text](image-1.png)

# How to run the project on local
1. Create a virtual environment 
    1. pip install virtualenv==20.25.0  (download the required library)
    2. virtualenv -p /usr/bin/python3 <virtualenv_name> (create virtual environment)
    3. source <virtualenv_name>/bin/activate (activate virtual environment)
    4. python setup.py install (install the dependencies)
    5. uvicorn main:app (run application)


