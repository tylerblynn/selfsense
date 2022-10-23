import empatica

device_list = ["empatica"]

print("Hello welcome to the dataloader and merger program")

print("Please select from the following list of devices")
for i in range(len(device_list)):
    print(str(i) +": " + device_list[i])

deviceSelection = input()
print("How many subjects? :")
subjectCount = input()
subjects = []
if deviceSelection == 0:
    pass