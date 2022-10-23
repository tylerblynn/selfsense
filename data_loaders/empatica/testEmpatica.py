import sys
sys.path.append('.')
import empatica
import pandas as pd
from preprocessing import split
from prediction import model

#this is an example of the pipeline for testing
#first we will retrieve the name of the subject
subject = "tyler"

#declare the empatica object w/ the subject name and modify the sensors that are not active
emp = empatica.Empatica(subject)
emp.eda = False
emp.hr = False
emp.temp = False
emp.bvp = False

#get index type for upload mainframe.
#index.dtype()

#retrive the path for the session 
#in this case we are uploading an already processed CSV and setting it as our dataframe

path = input()

emp.setMainFrame(emp.processFile(path))
emp.finalizeFrame()
print(emp.mainFrame.head)
emp.mainFrame.to_csv('acceleration_newexample')

"""
#now we break it into NP arrays
nps = split.NParrays(96, 96)
nps.setArrays(emp.mainFrame)
nps.finalizeArrays()

print(nps.x.shape)
print(nps.y.shape)
print(nps.sub.shape)
print(nps.time.shape)

#instantiate the model and split the data into test and training sets 
cnnModel = model.CNN()
cnnModel.importNPV(*nps.trainTestSplit(incl_val_group=True, incl_rms_accel=True))

#build, train, and test the model
cnnModel.build()
cnnModel.train()
cnnModel.run()
"""





