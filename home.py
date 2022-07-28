# import modules
import faulthandler
import sys
import tracemalloc 
from tkinter import *
import cv2
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.tix import Tk
from tkvideo import tkvideo
from PIL import ImageTk 
import threading
# module that offers several functions to deal with operations on files and their collections.
import shutil
from facerec import *
from register import *
from handler import *
import time
import csv
import pymysql
import numpy as np
# provides os.path functionality on Windows platforms. 
import ntpath
import os
from main_login import *
#basic image processing functionality like image resizing, rotation and transformation.
from PIL import Image

# define variables
active_page = 0
thread_event = None
left_frame =None
right_frame = None
heading = None
webcam = None
img_label = None
img_read = None
img_list = []
slide_caption = None
slide_control_panel = None
current_slide = -1

def home():
    # creating window for Criminal Detection Project    
    global bgg1, label, pimg1
    root = Toplevel()
    root.title("Criminal Detection Project")
    root.geometry("1100x1300")    
    
    
    # create Pages
    pages = []
    for i in range(4):
        pages.append(tk.Frame(root, bg="#051729"))
        pages[i].pack(side="top", fill="both", expand=True)
        pages[i].place(x=0, y=0, relwidth=1, relheight=1)

    # function for back     
    def goBack():
        global active_page
        # get the list of all the child widgets and destroy it when back button is pressed
        for widget in pages[active_page].winfo_children():
            widget.destroy()

        pages[0].lift()
        active_page = 0


    # basic page setup for all window of tkinter
    def basicPageSetup(pageNo):
        global left_frame, right_frame, heading

        # adding back button
        back_img = ImageTk.PhotoImage(file="back.png")
        back_button = tk.Button(pages[pageNo], image=back_img, bg="#051729", bd=0, highlightthickness=2,
            highlightbackground="white",activebackground="#051729", command=goBack)
        back_button.image = back_img
        # placing the button
        back_button.place(x=10, y=10)

        heading = tk.Label(pages[pageNo], fg="white", bg="#051729", font="Verdana 20 bold", pady=10)
        heading.pack()
        # Tkinter Frame widget is used to organize the group of widgets. It acts like a container which can be used to hold the other widgets.
        content = tk.Frame(pages[pageNo], bg="#051729", pady=20)
        content.pack(expand="true", fill="both")
        
        left_frame = tk.Frame(content, bg="#051729")
        left_frame.grid(row=0, column=0, sticky="nsew")
        
        # created a column where detected criminals will be listed
        right_frame = tk.LabelFrame(content, text="Detected Criminals", fg="white", bg="#051729", font="Verdana 20 bold", bd=4,
                    foreground="white", labelanchor="n")# labelanchor="n" is for string label
        right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        # creating column where result will be displayed
        content.grid_columnconfigure(0, weight=1, uniform="group1")
        content.grid_columnconfigure(1, weight=1, uniform="group1")
        content.grid_rowconfigure(0, weight=1)


    def showImage(frame, img_size):
        global img_label, left_frame
        img = cv2.resize(frame, (img_size, img_size))
        # converting image into rgb format
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
         # creating array
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        # placing image as label in left frame
        if (img_label == None):
            img_label = tk.Label(left_frame, image=img, bg="#051729")
            img_label.image = img
            img_label.pack(padx=20)
        else:
            img_label.configure(image=img)
            img_label.image = img

            
    # function for switching over to images that selected for registering a person
    def getNewSlide(control):
        global img_list, current_slide

        if(len(img_list) > 1):
            if(control == "prev"):
              # math formula is applied
                current_slide = (current_slide-1) % len(img_list)
                  # 3 = 2 % 5 = 2
            else:
                current_slide = (current_slide+1) % len(img_list)

            img_size = left_frame.winfo_height() - 200
            
            showImage(img_list[current_slide], img_size)
            # caption
            slide_caption.configure(text = "Image {} of {}".format(current_slide+1, len(img_list)), fg = "white")

    # function for selecting multiple pages
    def selectMultiImage(opt_menu, menu_var):
        global img_list, current_slide, slide_caption, slide_control_panel
        # file type must be in png format
        filetype = [("images", "*.png")]
        path_list = filedialog.askopenfilenames(title="Choose atleast 5 images", filetypes=filetype)
        # error for selecting 5 images
        if(len(path_list) < 5):
            messagebox.showerror("Error", "Choose atleast 5 images.")
        else:
            img_list = []
            current_slide = -1

            # Resetting slide control panel
            if (slide_control_panel != None):
                slide_control_panel.destroy()

            # Creating Image list
            for path in path_list:
                img_list.append(cv2.imread(path))

            # Creating choices for profile pic menu
            menu_var.set("")
            opt_menu['menu'].delete(0, 'end')
            # choose any one image for profile pic
            for i in range(len(img_list)):
                ch = "Image " + str(i+1)
                opt_menu['menu'].add_command(label=ch, command= tk._setit(menu_var, ch))
                menu_var.set("Image 1")


            # Creating slideshow of images
            img_size =  left_frame.winfo_height() - 200
            current_slide += 1
            showImage(img_list[current_slide], img_size)

            slide_control_panel = tk.Frame(left_frame, bg="#051729", pady=20)
            slide_control_panel.pack()
            # adding buttons for switch over to images
            back_img = tk.PhotoImage(file="previous.png")
            next_img = tk.PhotoImage(file="next.png")
            prev_slide = tk.Button(slide_control_panel, image=back_img, bg="#051729", bd=0, highlightthickness=0,
                                activebackground="#051729", command=lambda : getNewSlide("prev"))
            prev_slide.image = back_img
            prev_slide.grid(row=0, column=0, padx=60)

            slide_caption = tk.Label(slide_control_panel, text="Image 1 of {}".format(len(img_list)), fg="white",
                                bg="#051729", font="Verdana 13 bold")
            slide_caption.grid(row=0, column=1)

            next_slide = tk.Button(slide_control_panel, image=next_img, bg="#051729", bd=0, highlightthickness=0,
                                activebackground="#051729", command=lambda : getNewSlide("next"))
            next_slide.image = next_img
            next_slide.grid(row=0, column=2, padx=60)

    # function for register new criminal
    def register(entries, required, menu_var):
        global img_list

        # Checking if no image selected
        if(len(img_list) == 0):
            messagebox.showerror("Error", "Select Images first.")
            return

        # Fetching data from entries
        entry_data = {}
        for i, entry in enumerate(entries):
            # print(i)
            val = entry[1].get()
            # print(val)
            
            # error for required field missing
            if (len(val) == 0 and required[i] == 1):
                messagebox.showerror("Field Error", "Required field missing :\n\n%s" % (entry[0]))
                return
            else:
                entry_data[entry[0]] = val.lower()


        # Setting Directory for storing temp images of registered criminal
        path = os.path.join('face_samples', "temp_criminal")
        if not os.path.isdir(path):
            os.mkdir(path)

        no_face = []
        for i, img in enumerate(img_list):
            # adding registered person in no_face list
            id = registerCriminal(img, path, i + 1)
                if(id != None):
                no_face.append(id)

        # check if any image doesn't contain face
        if(len(no_face) > 0):
            no_face_st = ""
            for i in no_face:
                no_face_st += "Image " + str(i) + ", "
            messagebox.showerror("Registration Error", "Registration failed!\n\nFollowing images doesn't contain"
                            " face or Face is not clear:\n\n%s"%(no_face_st))
            shutil.rmtree(path, ignore_errors=True)
        else:
            # Storing data in database
            insertData(entry_data)
            rowId=1
            if(rowId >= 0):
                # Confirmation message
                messagebox.showinfo("Success", "Criminal Registered Successfully.")
                print("New Criminal registered.")
                # saving the unique face with their name
                shutil.move(path, os.path.join('face_samples', entry_data["Name"])
                goBack()
            else:
                shutil.rmtree(path, ignore_errors=True)
                messagebox.showerror("Database Error", "Some error occured while storing data.")


    ## update scrollregion when all widgets are in canvas
#     def on_configure(event, canvas, win):
#         canvas.configure(scrollregion=canvas.bbox('all'))
#         canvas.itemconfig(win, width=event.width)

    ## Register Page ##
    def getPage1():
        global active_page, left_frame, right_frame, heading, img_label
        active_page = 1
        img_label = None
        opt_menu = None
        menu_var = tk.StringVar(root)
        # display page 1
        pages[1].lift()
        # adding title in first page
        basicPageSetup(1)
        heading.configure(text="Register Criminal here",fg="white", highlightthickness=2, highlightbackground="white",bg="#051729")
        # creating column for enter details
        right_frame.configure(text="Enter Details", fg="white", bg="#051729")
        btn_grid = tk.Frame(left_frame, bg="#051729")
        btn_grid.pack()
        
        #adding button for select multiple images
        tk.Button(btn_grid, text="Select Images", command=lambda: selectMultiImage(opt_menu, menu_var), font="Verdana 13 bold", bg="#000000",
            fg="white", pady=10, bd=0, highlightthickness=2,highlightbackground="#051729", activebackground="#000000",
            activeforeground="white").grid(row=0, column=0, padx=25, pady=25)


        # Creating Scrollable Frame using canvas for registering details
        # The Canvas is a rectangular area intended for drawing pictures or other complex layouts. 
        # You can place graphics, text, widgets or frames on a Canvas.
        canvas = tk.Canvas(right_frame, bg="#051729", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand="true", padx=30)
        scrollbar = tk.Scrollbar(right_frame, command=canvas.yview, width=20, troughcolor="#051729", bd=0,
                            activebackground="#051729", bg="#000000", relief="raised")
        scrollbar.pack(side="left", fill="y")
        scroll_frame = tk.Frame(canvas, bg="#051729", pady=20)
        scroll_win = canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

        canvas.configure(yscrollcommand=scrollbar.set)
        # When function is invoked, Lambda runs the handler method. 
        canvas.bind('<Configure>', lambda event, canvas=canvas, win=scroll_win: on_configure(event, canvas, win))

        tk.Label(scroll_frame, text="* Required Fields", bg="#051729", fg="red", font="Verdana 13 bold").pack()
        # Adding Input Fields
        input_fields = ("Criminal-ID","Address","Phone","Name", "Father's Name", "Gender", "DOB(yyyy-mm-dd)", "Crimes Done","Date of Arrest(yyyy-mm-dd)","Place of Arrest", "Profile Image")
        ip_len = len(input_fields)
        # making some fields required
        required = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]

        entries = []
        for i, field in enumerate(input_fields):
            row = tk.Frame(scroll_frame, bg="#051729")
            row.pack(side="top", fill="x", pady=15)

            label = tk.Text(row, width=20, height=1, bg="#051729", fg="white", font="Verdana 13", highlightthickness=0, bd=0)
            label.insert("insert", field)
            label.pack(side="left")
            
            # making fields required
            if(required[i] == 1):
                label.tag_configure("star", foreground="red", font="Verdana 13 bold")
                label.insert("end", "  *", "star")
            

            if(i != ip_len-1):
                ent = tk.Entry(row, font="Verdana 13", selectbackground="#000000")
                ent.pack(side="right", expand="true", fill="x", padx=10)
                entries.append((field, ent))
            else:
                menu_var.set("Image 1")
                choices = ["Image 1"]
                opt_menu = tk.OptionMenu(row, menu_var, *choices)
                opt_menu.pack(side="right", fill="x", expand="true", padx=10)
                opt_menu.configure(font="Verdana 13", bg="#000000", fg="white", bd=0, highlightthickness=0, activebackground="#051729")
                menu = opt_menu.nametowidget(opt_menu.menuname)
                menu.configure(font="Verdana 13", bg="white", activebackground="#000000", bd=0)
        # adding register button and calling register function from register.py 
        tk.Button(scroll_frame, text="Register", command=lambda: register(entries, required, menu_var), font="Verdana 13 bold",
            bg="#000000", fg="white", pady=10, padx=30, bd=0, highlightthickness=2,highlightbackground="black", activebackground="#051729",
            activeforeground="white").pack(pady=25)


    # recognition function
    def startRecognition():
        global img_read, img_label
        # alert for no images selected
        if(img_label == None):
            messagebox.showerror("Error", "No image selected !! ")
            return

        crims_found_labels = []
        for wid in right_frame.winfo_children():
            wid.destroy()
        #  flipping image for detecting
        frame = cv2.flip(img_read, 1, 0)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_coords = detect_faces(gray_frame)
        # errors for those images that doesn't contain face or clear face
        if (len(face_coords) == 0):
            messagebox.showerror("Error", "Image doesn't contain any face or face is not clear.")
        else:
            # started training model
            (model, names) = train_model()
            print('Training Successful.')
            print('Detecting Faces....')

            
            (frame, recognized) = recognize_face(model, frame, gray_frame, face_coords, names)
            img_size = left_frame.winfo_height() - 40
            frame = cv2.flip(frame, 1, 0)
            showImage(frame, img_size)
            # starting recognition
            if (len(recognized) == 0):
                messagebox.showerror("Oops", "No criminal recognized.")
                # terminal message
                print("No criminal recognized.")
                print('Thankyou for using this project.')
                return
            # display the name of recognized
            for i, crim in enumerate(recognized):
                crims_found_labels.append(tk.Label(right_frame, text=crim[0], bg="black",
                                                font="Verdana 13 bold", pady=20))
                crims_found_labels[i].pack(fill="x", padx=20, pady=10)            

# function for selecting image for detection
    def selectImage():
        global left_frame, img_label, img_read
        # destroying another windows
        for wid in right_frame.winfo_children():
            wid.destroy()
        # setting filetypes
        filetype = [("images", "*.jpg *.jpeg *.png")]
        path = filedialog.askopenfilename(title="Choose a image", filetypes=filetype)

        if(len(path) > 0):
            img_read = cv2.imread(path)

            img_size =  left_frame.winfo_height() - 40
            showImage(img_read, img_size)
   

    ## Detection Page ##
  # page for image observation
    def getPage2():
        global active_page, left_frame, right_frame, img_label, heading
        img_label = None
        active_page = 2
        # display page 2
        pages[2].lift()
        basicPageSetup(2)
        # heading for detect criminal page
        heading.configure(text="Detect Criminal",  highlightthickness=2,highlightbackground="white",fg="white" )
        right_frame.configure(text="Detected Criminals", highlightthickness=2,highlightbackground="white",fg="white")

        btn_grid = tk.Frame(left_frame, bg="#051729")
        btn_grid.pack()
        
        # added buttons with function for selecting image and recognize 
        tk.Button(btn_grid, text="Select Image", command=selectImage, font="Verdana 13 bold", padx=20, bg="#000000",
                fg="white", pady=10, bd=0, highlightthickness=2,highlightbackground="#051729", activebackground="#051729",
                activeforeground="white").grid(row=0, column=0, padx=25, pady=25)
        tk.Button(btn_grid, text="Recognize", command=startRecognition, font="Verdana 13 bold", padx=20, bg="#000000",
            fg="white", pady=10, bd=0, highlightthickness=2,highlightbackground="#051729", activebackground="white",
            activeforeground="white").grid(row=0, column=1, padx=25, pady=25)

    #function for write detected video's timestamps in csv file
    def videoLoop(path,model, names):
        p=path
        q=ntpath.basename(p)
        filenam, file_extension = os.path.splitext(q)
        global thread_event, left_frame, webcam, img_label
        start=time.time()
#       webcam = cv2.VideoCapture(p)
        old_recognized = []
        crims_found_labels = []
        times = []
        img_label = None
        field=['S.No.', 'Time', 'Name']
        g=filenam+'.csv'
        filename = g
        num=0
        #  writing in csv file
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(field)   
            while not thread_event.is_set():
                    while (True):
                        (return_val, frame) = webcam.read()
                        if (return_val == True):
                            break
                        

                    # Flip the image (optional)
                    frame = cv2.flip(frame, 1, 0)
                    # Convert frame to grayscale Importance of grayscaling. Dimension reduction: 
#                     For example, In RGB images there are three color channels and has three dimensions while grayscale images are single-dimensional. 
#                     Reduces model complexity
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Detect Faces
                    face_coords = detect_faces(gray_frame)
                    (frame, recognized) = recognize_face(model, frame, gray_frame, face_coords, names)

                    # Recognize Faces
                    recog_names = [item[0] for item in recognized]
                    if(recog_names != old_recognized):
                        for wid in right_frame.winfo_children():
                            wid.destroy()
                        del(crims_found_labels[:])

                        for i, crim in enumerate(recognized):
                            num+=1
                            x=time.time()-start
                            crims_found_labels.append(tk.Label(right_frame, text=crim[0], bg="black",
                                                            font="Verdana 13 bold", pady=20))
                            crims_found_labels[i].pack(fill="x", padx=20, pady=10)
                            y=crim[0]
                           # print(x,y)
                            arr = [num,y,x]
                            # writing timestamps in csv file
                            csvwriter.writerow(arr)  
                        old_recognized = recog_names

                    # Display Video stream
                    img_size = min(left_frame.winfo_width(), left_frame.winfo_height()) - 20
                    # faulthandler.enable()
                    showImage(frame, img_size)
                            

    # video Observation Page ##
    def getPage4(path):
        p=path
        # print(p)
        global active_page, left_frame, right_frame, thread_event, heading
        active_page = 4
        pages[4].lift()

        basicPageSetup(4)
        # heading for video observation
        heading.configure(text="Video Observation", fg="white",highlightthickness=2,highlightbackground="white")
        # column for showing the detected criminal
        right_frame.configure(text="Detected Criminals",highlightthickness=2,highlightbackground="white", fg="white")
        left_frame.configure(pady=40)
        btn_grid = tk.Frame(right_frame,bg="#051729")
        btn_grid.pack()
        # training model (facerec file)
        (model, names) = train_model()
        print('Training Successful. Detecting Faces')

        thread_event = threading.Event()
        thread = threading.Thread(target=videoLoop, args=(p,model, names))
        thread.start()

   
    
    # function for selecting video
                            
    def selectvideo():
        global left_frame, img_label, img_read
        for wid in right_frame.winfo_children():
            wid.destroy()

        filetype = [("video", "*.mp4 *.mkv")]
        path = filedialog.askopenfilename(title="Choose a video", filetypes=filetype)
        p=''
        p=path

        if(len(path) > 0):
            # vid_read = cv2.imread(path)
            # print(vid_read)
            getPage4(p)
         else:
            messagebox.showerror("Please select a video")
                            
                            
#     def selectvideo1():
#         global left_frame, img_label, img_read
#         for wid in right_frame.winfo_children():
#             wid.destroy()

#         filetype = [("video", "*.mp4 *.mkv")]
#         path = filedialog.askopenfilename(title="Choose a video", filetypes=filetype)
#         p=''
#         p=path
# #         faulthandler.enable()
#         if(len(path) > 0):
#             # vid_read = cv2.imread(path)
#             # print(vid_read)
#             detect(p)# detect function using frontalface file for detecting from videos that if video contains human or not
#         else:
#             messagebox.showerror("Please select a video")

    ######################################## Home Page ####################################
    # heading of home page for Criminal Detection
    tk.Label(pages[0], text="Face Recognition System for Criminal Detection", fg="#ffffff", highlightbackground="white", highlightthickness=4,
        font="Helvetica 25 bold", bg="#051729", pady=10).pack(padx=50, pady=20)

    # added logo 
    logo = tk.PhotoImage(file = "logo1.png")
    tk.Label(pages[0], image=logo, bg="#051729").pack(side='top', padx=20, pady=30)
    btn_frame = tk.Frame(pages[0], bg="#051729", pady=30)
    btn_frame.pack()
    
    # added buttons with the functions
    b1 = Button(btn_frame, text="1. Register Criminal", command=getPage1)
    b2 = Button(btn_frame, text="2. Image Observation", command=getPage2)
    b4 = Button(btn_frame, text="3. Video Observation", command=getPage4)
    b1.pack()
    b2.pack()
    b4.pack()                        
    
#    setting design of button
    for btn in btn_frame.winfo_children():
        btn.configure(font="Verdana 20 bold", width=17, fg="#ffffff",
            pady=15, bd=0, highlightthickness=4, highlightbackground="#051729",)
        btn.pack(pady=30)
    pages[0].lift()
    
    # added video in front page with once view
    video_label = Label(root)
    video_label.place(x=400, y=130)
    player = tkvideo("criminal.mp4", video_label,
                    loop = 1, size = (300, 200))
    player.play()
    root.mainloop()
