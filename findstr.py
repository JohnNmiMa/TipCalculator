def findstr(instr):
    str = 'This is such a long string that I would like to find a substring of'
    print str
    if str.find(instr) >= 0:
        print "Found %s" % instr
    else:
        print "Did not find %s" % instr

