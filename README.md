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
<img width="1095" alt="Screenshot 2022-05-28 at 4 03 16 PM" src="https://user-images.githubusercontent.com/81081105/170822969-67fe0d7a-180c-4874-a36b-86174425e720.png"> | <img width="1088" alt="Screenshot 2022-05-28 at 4 16 37 PM" src="https://user-images.githubusercontent.com/81081105/170822906-0a180413-3c15-42f8-b434-7dfdd2932b7c.png"> 

**Image Observation**      |  **Image Observation**
:-------------------------:|:-------------------------:
<img width="1099" alt="Screenshot 2022-05-28 at 4 19 33 PM" src="https://user-images.githubusercontent.com/81081105/170823024-4f6c3432-8eca-4e9e-8d57-458a2728fc6b.png">  |  <img width="1088" alt="Screenshot 2022-05-28 at 4 17 09 PM" src="https://user-images.githubusercontent.com/81081105/170823029-a3c15dd6-279d-40f4-9862-43cce47609a6.png">

**Video Observation**      |  **Video Observation**
:-------------------------:|:-------------------------:
![lisa](https://user-images.githubusercontent.com/81081105/170823267-9538ff3a-c918-432c-93c9-6677b094a671.mp4) | ![lisa2](https://user-images.githubusercontent.com/81081105/170823274-0643f7c4-1323-4bd4-99da-dcefed1afaeb.mp4)


**Alerts**                 |  **Alerts**    
:-------------------------:|:-------------------------:
<img width="1090" alt="Screenshot 2022-05-28 at 11 24 19 PM" src="https://user-images.githubusercontent.com/81081105/170837323-d9ddf905-e837-43e5-ac43-7036eed7b653.png"> | <img width="1099" alt="Screenshot 2022-05-28 at 4 20 32 PM" src="https://user-images.githubusercontent.com/81081105/170837045-d021aea3-cf91-4dd6-8446-344f8fbf680e.png">  

**Alerts**                 | **Alerts**    
:-------------------------:|:-------------------------:
<img width="1090" alt="Screenshot 2022-05-28 at 11 25 17 PM" src="https://user-images.githubusercontent.com/81081105/170837354-d99b0d47-0163-46f0-9432-e73ed613f381.png"> |  <img width="1099" alt="Screenshot 2022-05-28 at 4 21 54 PM" src="https://user-images.githubusercontent.com/81081105/170837081-a88f4599-b149-4a41-81c8-3c309ee7c65d.png">



## Documents related to project

1. [My Roadmap](https://docs.google.com/document/d/1Vvo75mWCfiRvxTxxgcbv9ka2XeGkBIDrIBSEelaaudQ/edit?usp=sharing)
2. [One Pager](https://docs.google.com/document/d/1HGDGQlH0xjRnrk-JU5w1jfEVMJE2FOT9GkJOYi6psYA/edit?usp=sharing)
3. [Presentation](https://docs.google.com/presentation/d/1djK7o2FT_ateDKO9a9j9DQfC6ofK4lAmsMMufQHv-r0/edit?usp=sharing)
4. [Youtube Video]()
