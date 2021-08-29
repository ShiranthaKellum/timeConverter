
def convert (fTime):
    hour = int(fTime[0] + fTime[1])         # convert hours part into an integer
    minutes = int(fTime[3] + fTime[4])      # convert minutes part into an integer
    seconds = int(fTime[6] + fTime[7])      # convert seconds part into an integer

    if fTime [len (fTime) - 2] == "P":      # afternoon convertion
        if hour != 12:
            hour = hour + 12
            
    else:
        if hour == 12:                      # check for midnight (12:00:00PM = 00:00:00)
            hour = 0

    print(f"{hour :02d}", ":", f"{minutes :02d}", ":", f"{seconds :02d}",  sep="")


    
time = '12:05:45AM'
convert (time)
