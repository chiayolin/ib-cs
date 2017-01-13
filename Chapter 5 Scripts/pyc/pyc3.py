from functools import reduce

def checkSegment(segment):
    return segment[3].islower()                          \
           and (segment[-3:] + segment[:3]).isupper()    \
           and reduce(lambda x, y: x == y, segment[-3:]) \
           and reduce(lambda x, y: x == y, segment[:3])

with open("data.txt") as data:
    stream = data.readlines()
    
    for line in stream:
        start_offset = 0
        segment_size = 7
        
        while segment_size != len(line) - 1:
            segment = line[start_offset:segment_size]
            if checkSegment(segment):
                print(segment[3], end = '')

            start_offset += 1
            segment_size += 1
