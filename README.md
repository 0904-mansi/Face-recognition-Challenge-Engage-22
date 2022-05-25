# Face Recognition Challenge for Microsoft Engage'22 

## Problem Statement🧐 

Develop a browser-based application or a native mobile application to demonstrate application of Face Recognition technology.

## Solution 

We all know that our Face is a unique and crucial part of the human body structure that identifies a person. Therefore, we can use it to trace the identity of a criminal person and also for finding missing people. With the advancement in technology, we are placed CCTV at many public places to capture the criminal’s crime. Using the previously captured faces and criminal’s images that are available in the police station, the criminal face recognition system of can be implemented. I propose an automatic criminal identification system and missing people identification for Police Department to enhance and upgrade the criminal distinguishing into a more effective and efficient approach. Technology working behind it will be face recognition, from the footage captured by the CCTV cameras; our system will detect the face and recognize the criminal who is coming to that public place. The captured images of the person coming to that public place get compared with the criminal data we have in our database. If any person’s face from public place matches, the system will display their image on the system screen and will give the message with their name that the criminal is found and present in this public place.

## Workflow of Project
<img width="500" alt="Screenshot 2022-05-21 at 2 51 35 PM" src="https://user-images.githubusercontent.com/81081105/169645049-0b84ff23-5b71-424c-9820-fa55a84143a5.png">

 

## Model Build on Keeping These Criteria in Mind

1. Performance of model
2. Model selection
3. Scalability
4. Scalability of model
5. Retrainable model
6. Accessibility
7. User friendly
8. Accuracy 


## Technologies 

### 1. Tkinter 

Python has a lot of GUI frameworks, but Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. It’s cross-platform, so the same code works on Windows, macOS, and Linux. Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform where they’re run. 

However, Tkinter is lightweight and relatively painless to use compared to other frameworks. This makes it a compelling choice for building GUI applications in Python, especially for applications where a modern sheen is unnecessary, and the top priority is to quickly build something that’s functional and cross-platform.

### 2. Python <img width="30" src="https://img.icons8.com/color/48/000000/python--v1.png"/>

Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems. Python is dynamically-typed and garbage-collected. 

Python has become one of the most popular programming languages in the world in recent years. It's used in everything from machine learning to building websites and software testing. It can be used by developers and non-developers alike.


### 3. Open-CV <img width="30" src="https://img.icons8.com/color/48/000000/opencv.png"/>

## Prerequisite 

1. Python version must be `3.8.10`
2. Tkinter version must be `8.6`
3. [Xampp](https://www.apachefriends.org/download.html) must be installed on your system

`Note: Tk interface can be different for different systems and their versions`

## Steps to run the project

1. start your mysql and apache server and navigate to [localhost/phpmyadmin](localhost/phpmyadmin) create database of name `criminaldb`.
2. Import `table.sql` file into your newly created `criminaldb`. 
3. run this sql command in your criminaldb `SET GLOBAL sql_mode='';`
4. Install the requiremnts using command `pip or pip3 install -r requirements.txt`.
5. Run the main python file `python or python3 main.py`.
6. Now experience the GUI and features of the project.

## Glimps of my Application

**Login Page**            |  **Sign-Up Page**
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/81081105/170031961-682d7f02-45e0-47b0-b8de-12fbb8576287.png)  |  ![](https://user-images.githubusercontent.com/81081105/170031999-d0f4ab21-aec8-4020-9466-d08fbf346321.png)

**Home Page**

<img width="800" alt="Screenshot 2022-05-24 at 11 09 27 PM" src="https://user-images.githubusercontent.com/81081105/170098347-9f328ba0-4f63-4f26-968c-395b1c20663f.png">

**Criminal Detection**            |  **Finding Missing People**
:-------------------------:|:-------------------------:
<img width="1212" alt="Screenshot 2022-05-24 at 11 14 45 PM" src="https://user-images.githubusercontent.com/81081105/170099565-dfc2e897-3602-4678-9ce0-592c24649e5a.png">  |  <img width="1212" alt="Screenshot 2022-05-24 at 11 19 00 PM" src="https://user-images.githubusercontent.com/81081105/170100191-829547af-66b5-4cc1-9d42-c8ea06a16556.png">


**Register Criminal**            |  **Register Missing Person**
:-------------------------:|:-------------------------:
 <img width="1212" alt="Screenshot 2022-05-25 at 3 42 58 PM" src="https://user-images.githubusercontent.com/81081105/170239156-76991442-83ab-4ccf-bbdc-33f81f67c850.png">                           | <img width="1212" alt="Screenshot 2022-05-25 at 3 17 40 PM" src="https://user-images.githubusercontent.com/81081105/170234114-602f0d49-ffca-4107-8d05-825a9362dc74.png">

    

## Documents related to project

1. [My Roadmap](https://docs.google.com/document/d/1Vvo75mWCfiRvxTxxgcbv9ka2XeGkBIDrIBSEelaaudQ/edit?usp=sharing)
2. [Presentation](https://docs.google.com/presentation/d/1djK7o2FT_ateDKO9a9j9DQfC6ofK4lAmsMMufQHv-r0/edit?usp=sharing)
3. [Youtube Video]()
