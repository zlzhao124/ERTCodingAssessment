from datetime import datetime

#I create 2 functions, a generic mergesort and a mergesort specific to sorting the date and time of the line bits
def mergesort(vals):
    if len(vals) == 1:
        return vals
    else:
        vals_sorted = []
        left = vals[0:int(len(vals)/2)]
        right = vals[int(len(vals)/2):len(vals)]
        leftsorted = mergesort(left)
        rightsorted = mergesort(right)
        i = 0
        j = 0
        while (i < len(leftsorted) or j < len(rightsorted)):
            if i < len(leftsorted) and (j >= len(rightsorted) or leftsorted[i] <= rightsorted[j]):
                vals_sorted.append(leftsorted[i])
                i += 1
            elif j < len(rightsorted) and (i >= len(leftsorted) or leftsorted[i] > rightsorted[j]):
                vals_sorted.append(rightsorted[j])
                j += 1
        return vals_sorted

def mergesortlbs(vals):
    if len(vals) == 1:
        return vals
    else:
        bits_sorted = []
        left = vals[0:int(len(vals)/2)]
        right = vals[int(len(vals)/2):len(vals)]
        leftsorted = mergesortlbs(left)
        rightsorted = mergesortlbs(right)
        i = 0
        j = 0
        #i use the date ID instead of the actual date because that seemed easier
        #If 2 rows have the different date IDs, add the smaller one first
        #If 2 rows have the same date ID, add the earlier one first
        while (i < len(leftsorted) or j < len(rightsorted)):
            if i < len(leftsorted) and (j >= len(rightsorted) or leftsorted[i][1] <= rightsorted[j][1] or 
                                        (leftsorted[i][1] == rightsorted[j][1] and leftsorted[i][2] <= rightsorted[j][2])):
                bits_sorted.append(leftsorted[i])
                i += 1
            elif j < len(rightsorted) and (i >= len(leftsorted) or leftsorted[i] > rightsorted[j] or 
                                          (leftsorted[i][1] == rightsorted[j][1] and leftsorted[i][2] > rightsorted[j][2])):
                bits_sorted.append(rightsorted[j])
                j += 1
        return bits_sorted

#open the txt file and read
with open('AU930_ROAM.TXT') as f:
    lines = f.readlines()
#take out the title line
lines = lines[2:]
foF2vals = []
hmF2vals = []

#split each line into an array of values where each array bucket has some information
linebits = []
for line in lines:
    linebits.append(line.split())
for linebit in linebits:
    #convert 1st column to date
    linebit[0] = datetime.strptime(linebit[0], '%Y.%m.%d').date()
    #remove parentheses from 2nd column and convert 2nd column to integer
    linebit[1] = int(linebit[1][1:4])
    #convert 3rd column to time
    linebit[2] = datetime.strptime(linebit[2], '%H:%M:%S').time()
    #convert 4th column to integer
    linebit[3] = int(linebit[3])
    #convert all the rest of the columns to floats, as long as value is not "---"
    for i in range(4,14):
        if linebit[i] != '---':
            linebit[i] = float(linebit[i])
            #if we're iterating through the 5th column, which is foF2 value, add that value to foF2vals
            if i == 4:
                foF2vals.append(linebit[i])
            #if we're iterating through the 10th column, which is hmF2 value, add that value to hmF2vals
            if i == 9:
                hmF2vals.append(linebit[i])

#sort foF2vals and hmF2vals and print the middle index of the sorted list, this is our median
foF2vals_sorted = mergesort(foF2vals)
median_foF2 = foF2vals_sorted[int(len(foF2vals_sorted)/2)]
print("The median foF2 value is: ", median_foF2)
hmF2vals_sorted = mergesort(hmF2vals)
median_hmF2 = hmF2vals_sorted[int(len(hmF2vals_sorted)/2)]
print("The median hmF2 value is: ", median_hmF2)

#sort the lines and print the sorted list out
lines_sorted = mergesortlbs(linebits)
print(lines_sorted)
