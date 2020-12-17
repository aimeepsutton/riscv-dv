#!/usr/bin/python3

import argparse

# Command line arguments
parser = argparse.ArgumentParser(description='Some artificial log file processing')
parser.add_argument('logFiles', help='Test logs to process', nargs='+')

args = parser.parse_args()
totalIns = 0

for fileN in args.logFiles:
    print("\n" + fileN)
    testlog = reversed(open(fileN).readlines())
    for line in testlog:
        if "main_program_instr_cnt" in line:
            columns = line.split()
            instrCnt = columns[3]
            print("instrCnt = " + instrCnt + " ('d" + str(int(instrCnt.strip("'h"), 16)) + ")")
            totalIns = totalIns + int(instrCnt.strip("'h"), 16)
            break
        
avgInsCnt = totalIns / len(args.logFiles)
print("\naverage number of instructions = " + str(avgInsCnt))
