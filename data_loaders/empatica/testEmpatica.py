import pandas as pd
import os
import io
import sys
import empatica
home = os.getcwd()
os.chdir('..')
print(os.getcwd())
os.chdir('..')
os.chdir(os.path.join(os.getcwd(), "preprocessing"))
print(os.getcwd())
import split
os.chdir(home)


#from data_loaders import empaticau
#this is an example of the pipeline for testing
#first we will retrieve the name of the subject

#declare the empatica object w/ the subject name and modify the sensors that are not active


#32 hz 64 hz 
#1hz 70hz



