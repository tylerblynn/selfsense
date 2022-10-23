# Self-Sense: Self-Supervised Labeling of Sensor-Generated Time-Series Data

https://txst-my.sharepoint.com/:w:/r/personal/v_m137_txstate_edu/_layouts/15/Doc.aspx?sourcedoc=%7B99D03B23-BA4F-4521-9759-95451C05E425%7D&file=Requirements%20Specifications.docx&action=default&mobileredirect=true

## Installation
* git clone https://git.txstate.edu/imics-lab/self-sense.git
* Ensure you have the correct imports downloaded
  * pip install *import name*
  * Pandas, Plotly, Ipywidgets, IPython, Datetime, Voila, Numpy, Keras, Tensorflow, Jupyter, Scikitlearn, os, sys, and io.

## Getting Started:
* Preprocess the data
  * Use the empatica class:
    * import the empatica class 
    * Instantiate object with subject/group identifier
    * Turn off sensors you do not want to include by toggling the sensor attributes: emp.temp = False
    * Use the processFile function to get sensor files into a datetime indexed dataframe
    * Use setMainFrame() function for setting the dataframe attribute of the Empatica class equal to a dataframe
      * Example: emp = Empatica("Subject Name")
                 emp.setMainFrame(emp.processFile(path))
    * Call updateMainFrame() for each sensor file you want to add
    * Call finalizeFrame() to set column labels equal to the active sensor's data fields and create the subject column
    * Save the processed data: emp.mainFrame.to_csv(filename)
* Load the data file into first Jupyter Notebook
  * Navigate to ‘gui\labeling_web_interface.ipynb’
  * Click Voila button at the top of the notebook (In taskbar, under 'Help')
  * Give the path for the data file and label file in the section “2. Upload CSV File"

## Visualize Raw Time-Series & Manually Add Labels to Data:
* Once the data file is loaded you can run the cell “3. Visualize raw time-series”
  * After this cell is run, it will produce a raw time-series plot and a labeling UI under it.
  * To use the UI, you need to supply a start time and end time in datetime (YYYY-MM-DD HH:MM:SS) format.
    * Need to hit the ‘Enter’ key after filling in the text fields for it to read the value
  * Choose a label within the label selection box
    * This is a selection field that holds all the labels within the label file uploaded
* Once you supply the UI with a start time, end time, and label selection, you click the ‘Add Label’ button to apply the chosen label between that time range.
  * The graph will update and plot a new graph with the UI moving under the updated graph.
  * Once you manually add all desired labels, within the section ‘3.5 Visualize Labels’ you can view all the labels added
  * Once labels are finalized, click the ‘Finalize Added Labels’ button to show these labels.

## Get User Specifications for Numpy Arrays:
* After running this cell it will create:
  * A check box to select on/off if you want validation or not.
  * A text field for the user to input a window size and steps

## Segment Time-series Section:
*After running this cell it will create:
  * A text input field for you to name the model
  * Once the model is named you can select the build button
  * The build button will assemble the layers of the model and train the model on the data

## Model Creation:
* After running this cell it will create:
  * A button named ‘Save Model’ you can click
  * If a models folder is not already present, it will generate a folder in the directory where the Jupyter notebook is running, called “models”, and saves the model in that folder as a .h5 file.

## Model Upload: 
* Navigate to the second jupyter notebook entitled "gatherData.ipynb"
* Run the top cell that will import all of the required libraries for the project
* Run the second cell:
  * After running this cell two things will be displayed to you:
    * The model selection or upload box: If you created models using the previous interface this cell will read in and display the names         of the models you created. You can select which model you want by clicking the corresponding bubble. If the models folder is not           dected then it will ask you to enter the path to the model you would like to upload.
    * Input the data path for the new data set you wish to label. This data must already be preprocessed into the same datetime indexed         format that the data from last notebook ended up in. 
* Run the remaining cells: 
  * These cells will take the data youve chosen to upload and run it through the model.
  * The model will then output its predictions which are converted back into their label text based forms. 
  * These predictions are then used to label each corresponding time segment of the data that was uploaded.
