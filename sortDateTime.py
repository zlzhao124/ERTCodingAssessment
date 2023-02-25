from datetime import datetime

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


with open('AU930_ROAM.TXT') as f:
    lines = f.readlines()
linebits = []
lines = lines[2:]
foF2vals = []
hmF2vals = []
for line in lines:
    linebits.append(line.split())
for linebit in linebits:
    linebit[0] = datetime.strptime(linebit[0], '%Y.%m.%d').date()
    linebit[1] = int(linebit[1][1:4])
    linebit[2] = datetime.strptime(linebit[2], '%H:%M:%S').time()
    linebit[3] = int(linebit[3])
    for i in range(4,14):
        if linebit[i] != '---':
            linebit[i] = float(linebit[i])
            if i == 4:
                foF2vals.append(linebit[i])
            if i == 9:
                hmF2vals.append(linebit[i])

foF2vals_sorted = mergesort(foF2vals)
median_foF2 = foF2vals_sorted[int(len(foF2vals_sorted)/2)]
print("The median foF2 value is: ", median_foF2)
hmF2vals_sorted = mergesort(hmF2vals)
median_hmF2 = hmF2vals_sorted[int(len(hmF2vals_sorted)/2)]
print("The median hmF2 value is: ", median_hmF2)
lines_sorted = mergesortlbs(linebits)
print(lines_sorted)
