import pandas as pd
import os
import io
import sys
sys.path.append('..')
import empatica
path = os.path.join(os.getcwd(), '1574621345_A01F11.zip')
emp = empatica.Empatica("Lee")
emp.setMainFrame(emp.processFile(path))

emp.updateMainFrame(df)
#from data_loaders import empaticau
#this is an example of the pipeline for testing
#first we will retrieve the name of the subject

#declare the empatica object w/ the subject name and modify the sensors that are not active


#32 hz 64 hz 
#1hz 70hz



