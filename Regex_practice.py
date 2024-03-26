import re  

# Task 1
# Look for devices IDs that begin with "r15" in devices.txt file. These characters indicate that the device is running an operating system that must be updated.
with open("\Devices.txt", "r") as file: #add respective file path
    devices = file.read()
# print("Devices:", devices)

# Creating search pattern
pattern1 = "r15\w+"

#ans
print('Devices IDs begining with "r15":', re.findall(pattern1,devices))



#Task 2: 
#Extract the valid IP addresses from the flagged IP -> log_file.txt
with open("\Log_file.txt", "r") as file: #add respective file path
    logs = file.read()

#final pattern, excluding wrong IP addresses (correct IP adds only have 1-3digits per oclet only)
final_pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

valid_IP = re.findall(final_pattern,logs)
print('Valid IP addressess:',valid_IP) #ans



#Task 3
#Filter out flagged IPs and highlight them while giving clearance message for those that are fine

#Flagged IPs
with open ("\Flagged_IPs.txt", "r") as file: #add respective file path
    flagged_IP = file.read()

Flagged_IP = flagged_IP.split()

counter = 0
#Iterate thru valid_IP(already filtered out valid IPs)
for address in valid_IP:
    counter +=1
#Checking thru if any IP adds are included in the flagged_addressess list, if so inform
    if address in Flagged_IP:
        print(counter,"The IP address",address,"has been flagged for further analysis.")
#If IP is all good, inform
    else:
        print(counter,"The IP address",address,"is fine and does not require further analysis.")