# SweePy
A Smart File Organizer using Python

## Contents
- [Introduction](#introduction)
- [Modules](#modules)
- [Setup](#setup)
- [Usage - GUI-based Application](#usage---gui-based-application)
- [Creating an Executable](#creating-an-executable)
- [Flags Explained](#flags-explained)

# Introduction
SweePy helps to organize the directories by moving files into folders based on their type. This application is written in Python3 and can be used as either a stand-alone python script that can be run with python runtime or a GUI-based version which is ready-to-run available.

# Modules
This application is very simple that it does not use any external libraries but python built-in library Tkinter for UI. 

# Setup
You can clone the repository from the git command line as

  ```shell
  git clone https://github.com/Pooventhiran/SweePy.git
  ```
If you have GitHub desktop, clone the repository from "File -> Clone Repository".
 
# Usage - GUI-based Application
The GUI application is available as **SweePy.exe** in the repository. Just open it to work with.

![sweepy](https://github.com/Pooventhiran/SweePy/blob/master/images/sweepy-main.PNG)

# Creating an Executable
You can create the executable file on your own using **pyinstaller**. It will create the executable corresponding to the underlying operating system only i.e. it cannot create debian executable on windows or so.

Pyinstaller can be installed using **pip**.

  ```
  pip install pyinstaller
  ```

To create an executable on your own, run the following command in the command prompt.

  ```
  pyinstaller --onefile --windowed app.py -n <namae-of-exe>
  ```
 
 This command also creates a spec file that can be used to configure the features which cannot be specified through the command line.
 The application will be inside dist folder of this directory.
 
The **spec** file corresponding to windows is uploaded to the repository. To use it, just run pyinstaller with the spec file instead of the python file.
 
 ### Flags explained
 - **onefile**: It is to create a one-file executable. Pyinstaller will create all libraries and required files separately if not specified.
 - **windowed**: It is to hide the console that usually appears on the background when the application is run.


