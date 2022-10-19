#The start of the application 
import pandas as pd
print("Hello welcome to CSV merger")
#This is just an example program meant to capture some of the functionality of the merging pipeline
#NOT A FINAL PROGRAM 

print("Every file-path name or file name must not have any spaces")
print("Example: 'Final_data.csv' is okay")
print("'Final data.csv' is not okay")
print("Please enter the target sampling rate")
#targetSampleRate = input()
while(True):   
    print("Please enter a CSV file containing the names of the subjects in the first column of the file")
    sfile = input()
    subjects = pd.read_csv(sfile)
    print("Please enter a CSV file containing the names of the types of sensor data you want to include")
    sfile = input()
    sensorTypes = pd.read_csv(sfile)
    numSubjects = subjects.shape[0]
    colLabels = ["date_time"]
    print("Now you will need to enter the features produced for each sensor (i.e. columns)")

    for sensors in range(sensorTypes.shape[0]):        
        print("Please enter a CSV file containing the fields, in order, for "+ sensorTypes.iloc[sensors][0])
        sfile = input()
        df = pd.read_csv(sfile)
        colLabels.append(df.iloc[0:df.shape[0],0])

    df.to_csv('example.csv')
    for subject in range(subjects.shape[0]):
        print("Here you will enter all of the datasets for subject: " + subjects.iloc[subject][0])
        keepGoing = 'y'
        while(keepGoing == 'y'):
            for sensor in range(sensorTypes.shape[0]):
                print("Please enter the file containing "+ sensorTypes.iloc[sensor][0] + " data for " + subjects.iloc[subject][0])
                sfile = input()


    


    
