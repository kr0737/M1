# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:59:07 2023
@author: shbur
"""
import sys
from sys import exit
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import random
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from tkinter import messagebox
from tkinter import filedialog
import os.path
plt.rcdefaults()
import matplotlib.pyplot as plt

#main variables
global dirname
dirname = ''
global stats
stats = ''

#color each screen
colors = ['red','blue','cyan','orange','green','yellow','grey','black']

#functions 
b = 'b*6 - a**2 + 34*a*b**3'
h = 'b*np.sin((a/5))'
l = 'a*5 - b**3 + 2*a*b**4'
m = 'np.subtract(b,np.sqrt(a**2)*1.9)'
o = 'b*np.sin((a/40))'
n = 'a*np.sin((b/50))'
flist = [h,b,m,l,n,o]
f = random.choice(flist)  

# Function to open a URL in a web browser
def open_url():
    url = "https://canvas.education.lu.se/courses/26695/pages/screening-experiment-app"  
    webbrowser.open(url)

# Functions for the four main buttons
def function1(): #find working dir and test for files
    global dirname
   
    #get path
    dirname = filedialog.askdirectory()
    dirname = dirname + '/'
    
    #test if all files are there
    ans = testfolder(dirname)
    if ans == 'y':
        messagebox.showerror("A Problem occurred", "You should have your screen_design.csv file in this work folder. Is your file spelled right and lower case?")
        root.destroy()
    else: 
        #make folders
        resultsdir = dirname + 'Results/'
        
        #make work folders
        folds = [resultsdir]
        for fold in folds:
            if not os.path.exists(fold):
                os.makedirs(fold)
        
        #finish
        #messagebox.showinfo("1. Located Document", "Edit the screen_esign.csv file, adding tests (rows) then run!")
            
def function2(): #initial analysis and stats generation
    global stats
    start_animation()
    
    if len(dirname) > 0:
        screen(dirname)
        stats = 'y'
    else:
        messagebox.showerror("A Problem occurred", "Either the path is incorrect, or your document is missing. See Support.")
        root.destroy()
    #end
    stop_animation()
    messagebox.showinfo("2. Ran the screen", "Check the Results folder for the initial analysis. Continue to screen or do the main analysis, then proceed to step 3.")

def function3(): #final results
    start_animation()
    
    if len(dirname) > 0 and len(stats) > 0:
        finalresults(dirname)
    else:
        if len(dirname) ==  0 or len(stats) == 0:
            messagebox.showerror("Problem!", "Either you have an issue with choosing the work folder path (step 1) or running (step 2). Please start over.")
            root.destroy()

    #end
    stop_animation()
    messagebox.showinfo("3. Examine Results", "Examine your screen designs and compare to all possible responses. Did you find the linear region and have enough experimental units to do linear regression?")

# Function to start the animation
def start_animation():
    animation_label.config(text="Please Wait....")
    animation_label.update()

# Function to stop the animation
def stop_animation():
    animation_label.config(text="")
    animation_label.update()

#open a file
def getit(pathandfile):
    FH1 = open(pathandfile, 'r')
    lines = FH1.readlines()
    return lines

#*********************************************************

# Create the main window
root = tk.Tk()
root.title("Apple App-Style GUI")

# Open and display a PNG image
bg_image = Image.open("background.png")
bg_image2 = Image.open("background2.png")

#for minipic
intropic = bg_image.resize((100, 100))
minipic = ImageTk.PhotoImage(intropic)

#and for background
bg_image2 = bg_image2.resize((450, 400))
bg_photo = ImageTk.PhotoImage(bg_image2)

# Create a canvas with the same dimensions as the image
canvas = tk.Canvas(root, width=bg_image2.width, height=bg_image2.height)
canvas.pack()

# Display the background image on the canvas
canvas.background = bg_photo
bg = canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# Create a frame for the buttons and animation
frame = tk.Frame(root,bg='#d2b48c')
frame.pack()
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add a title label with the Apple-style font
title_label = tk.Label(frame, text="Run Screening Experiments!", font=("Helvetica", 12, "bold"),bg='#d2b48c') #image = bg_photo,
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 20))

# Create four rounded buttons in a 2x2 grid
button1 = tk.Button(frame, text="1. Locate your document folder", padx=20, pady=10, command=function1, font=("Helvetica", 10), fg="white", bg="#c37c4d", relief="raised")
button2 = tk.Button(frame, text="2. Run", padx=20, pady=10, command=function2, font=("Helvetica", 10), fg="white", bg="#c37c4d", relief="raised")
button3 = tk.Button(frame, text="3. View final results", padx=20, pady=10, command=function3, font=("Helvetica", 10), fg="white", bg="#c37c4d", relief="raised")

# Arrange buttons in a 2x2 grid
button1.grid(row=2, column=0, padx=20, pady=20)
button2.grid(row=2, column=1, padx=20, pady=20)
button3.grid(row=3, column=0, padx=20, pady=20)

# Create a button for the URL link
url_button = tk.Button(frame, text="Support", padx=20, pady=10, command=open_url, font=("Helvetica", 10), fg="white", bg="#b8860b", relief="raised")
url_button.grid(row=1, column=0, columnspan=1, padx=20, pady=20)

# pic to upper right
forintropic = tk.Label(frame, image=minipic,borderwidth=0)
forintropic.grid(row=1, column=1, columnspan=1)

# Create a label for animation
animation_label = tk.Label(frame, text="", font=("Helvetica", 10, "italic"), bg='#d2b48c', fg="black")
animation_label.grid(row=4, column=0, columnspan=1, pady=10)

# Add a title label with the Apple-style font
info = tk.Label(frame, text="Burleigh, Food Technololgy, 2023, v1    ", font=("Helvetica", 8),bg='#d2b48c') #image = bg_photo,
info.grid(row=4, column=1, columnspan=2)

# Adjust the padding and weights for the frame
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

#*************************************************************************

def testfolder(dirname):
    errors = 'n'
    
    #musthave.txt
    tst = [os.path.join(root, name)
                 for root, dirs, files in os.walk(dirname)
                 for name in files
                 if name.endswith(("screen_design.csv"))]
    if len(tst) == 0:
        errors = 'y'           
    return errors


#functions
def myrand(val):

    proportion = random.uniform(0, 0.25)
    print(proportion)
    extra = val * proportion
    
    #plus or minus
    if random.random() < 0.5:
        mult = -1
    else:
        mult = 1
    
    #add it together
    extra = extra * mult
    val2 = val + extra
    print(val,val2)
    return round(val2,2)

#Day1+2
def f1(x,y,f):
    response = []
    
    #as lists
    for i in range(len(x)):
        a = x[i]
        b = y[i]
       
        #random
        c2 = myrand(eval(f))
        response.append(c2)
    return response

#meshgrid of function
def f2(a,b,f):
    z = eval(f)
    return z

#graph without mesh
def graphA(df,PROJ,resultsdir,eus,f,colors):

    #remaining
    remaining = eus - len(df.index)
    
    if remaining < 0:
        messagebox.showerror("Problem!", "You used over 30 experimental units (see your screen_design.csv).")
        root.destroy()
    
    #identify how many EUs used so far
    screeninfo = df['Screen'].tolist()
    screens = []
    for sc in screeninfo:
        if sc not in screens:
            screens.append(sc)        
    
    #make two graphs at different angles
    allresponses = []
    for i in range(4):
        fig = plt.figure()                     
        ax = fig.add_subplot(projection='3d')   

        #loop through each screen sp they each get a different color
        for k in range(len(screens)):
            scr = k + 1
            test = 'Screen' + str(scr)    
            df2 = df[df['Screen'] == screens[k]] 

            #data
            cats = list(df2)  #column headers
            labelx = cats[1] #Screen is 0
            labely = cats[2]
            
            #test
            x = df2[labelx].tolist()
            y = df2[labely].tolist()
            response = f1(x,y,f)
            allresponses = allresponses + response #for saving
            ax.scatter(x, y, response,s=60, edgecolor='black', color= colors[k],alpha = 0.5,label=test)
        
        #finish
        zmin = min(allresponses) -0.05 * min(allresponses)
        zmax = max(allresponses) + 0.05 * max(allresponses)
        ax.set_zlim(zmin,zmax)        
        ax.set_xlabel(labelx)
        ax.set_ylabel(labely)
        ax.set_zlabel('Response')
        ax.invert_zaxis() 
        if i == 0:
            ax.view_init(-150, 10)
        elif i == 1:
            ax.view_init(-160, 30)
        elif i == 2:
            ax.view_init(-170, 50)
        else:
            ax.view_init(-150, 65)
                        
        #remaining
        thetitle = PROJ + ', ' + test + ', remaining: ' + str(remaining)
        plt.title(thetitle)
        plt.legend()
        label = resultsdir + PROJ + '_' + test + '_view' + str(i) + '.png'
        plt.savefig(label, format='png', dpi=1200)
        plt.show()
        plt.close()   

        #write to csv
        if i == 0:
            x = df[labelx].tolist()
            y = df[labely].tolist()           
            df3 = pd.DataFrame({"Screen": screeninfo , labelx: x , labely: y ,'Response': allresponses })
            fil = resultsdir + PROJ + '_results.csv'
            df3.to_csv(fil, index=False, sep=",") 
        

#graph with mesh
def graphB(df,PROJ,resultsdir,f,colors):

    allresponses = []
    #two graphs at different angles
    for i in range(4):
        
        #identify how many screens
        screeninfo = df['Screen'].tolist()
        screens = []
        for sc in screeninfo:
            if sc not in screens:
                screens.append(sc)         
        
        #all sampling data to make the meshgrid
        cats = list(df)  #column headers
        labelx = cats[1] #Screen is 0
        labely = cats[2]        
        x = df[labelx].tolist()
        y = df[labely].tolist()        
        ax = plt.axes(projection='3d')
        xlow = min(x)
        xhigh = max(x)
        ylow = min(y)
        yhigh = max(y)            
        x = np.linspace(xlow, xhigh, 100)
        y = np.linspace(ylow, yhigh, 100)
        X, Y = np.meshgrid(x,y) 
        Z = f2(X,Y,f)        
        ax.contour3D(X, Y, Z, 50, cmap='plasma')          
        
        #loop through each screen sp they each get a different color
        for k in range(len(screens)):
            test = 'All possible responses'
            df2 = df[df['Screen'] == screens[k]] 

            #data the sampling
            x = df2[labelx].tolist()
            y = df2[labely].tolist()
            response = df2['Response'].tolist()
            allresponses = allresponses + response #for zrange
            ax.scatter(x, y, response,s=60, edgecolor='black', color= colors[k],alpha = 0.4,label=test)
        
        #finish
        zmin = min(allresponses) - 0.05 * min(allresponses)
        zmax = max(allresponses) + 0.05 * max(allresponses)
        ax.set_zlim(zmin,zmax)                
        ax.set_xlabel(labelx)
        ax.set_ylabel(labely)
        ax.set_zlabel('Response')
        ax.invert_zaxis() 
        
        if i == 0:
            ax.view_init(-150, 10)
        elif i == 1:
            ax.view_init(-160, 30)
        elif i == 2:
            ax.view_init(-170, 50)
        else:
            ax.view_init(-150, 65)
        
        #finish
        thetitle = PROJ + ', ' + test
        plt.title(thetitle)
        label = resultsdir + PROJ + '_final_view' + str(i) + '.png'
        plt.savefig(label, format='png', dpi=1200)
        plt.show()
        plt.close()          

#functions
def screen(mypath):   
    resultsdir = mypath + 'Results/'

    #files
    fil = mypath + 'screen_design.csv'
    df = pd.read_csv(fil, sep = ",")

    #get PROJ
    bits = fil.split('/')
    PROJ = bits[-2]

    #experimental units left
    eus = 30
    
    #graph
    graphA(df,PROJ,resultsdir,eus,f,colors)    
    
    #finish
    answer = 'Done with initial analysis!'
    return answer     


#functions
def finalresults(mypath):
    resultsdir = mypath + 'Results/'

    #get PROJ
    bits = mypath.split('/')
    PROJ = bits[-2]  

    #get *final* results
    fil = resultsdir + PROJ + '_results.csv'
    df = pd.read_csv(fil, sep = ",")


    #main analysis
    graphB(df,PROJ,resultsdir,f,colors)   
    
    #finish
    answer = 'Done with final analysis!'
    return answer          
         

# Start the main loop
root.mainloop()