### Converting txt file to csv file.

# open and read the txt file.
text_file = open("Radio_Log.txt", "r")

# Read each line of text file and save it in lines. 
lines = text_file.readlines()

# print lines
#print len(lines)
text_file.close()

# Call CSV Library
import csv

with open('OutPut.csv', 'w', newline='') as csvfile:
    mycsv = csv.writer(csvfile, delimiter=',')
    mycsv.writerow(['Channel', 'Channel Name', 'Start Time', 'Duration', 'Date'])
    for line in lines:
        if "Date:" in line:
            date = line.split(":")[1]
            date = date[1:11]
        if "N/A" in line:
            print(line)
            #print(date)
            channel = line[6]
            channel_name = line[15:17]
            start_time = line[17:25]
            duration = line[25:33]
            
            mycsv.writerow([channel, channel_name, start_time, duration, date])
            