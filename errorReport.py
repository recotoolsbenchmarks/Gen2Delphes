import os,re,subprocess

# Create and import the lists of samples to run
print 'Creating and importing file lists...'
from listFiles import *

# Read input arguments
runDir=os.getcwd()

for sample in fileList:
    sample = sample.replace('fileLists/','').replace('.txt','')
    print '\n============================================='
    print 'Working on sample',sample

    command = 'ls -tr condor_logs/'+sample+'/*.log'
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (logs, err) = proc.communicate()
    logs = logs.strip()

    starts = [0]
    starts += [m.start() for m in re.finditer('\n',logs)]
    print 'Sample has',len(starts),'log files'

    totaljobs = 0
    totaldone = 0
    for ilog in range(len(starts)):        
        start = starts[ilog]
        if start > 0: start = start+1
        try:
            end = starts[ilog+1]
            thislog = "".join(logs[start:end])
        except:
            thislog = "".join(logs[start:])
        print '\tWorking on this log:',thislog
        
        command = 'grep "Job submitted" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        jobs = int("".join(out[0:digits]))
        if totaljobs < jobs: totaljobs = jobs 
        
        command = 'grep "exceeding requested memory" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        omem = int("".join(out[0:digits]))
        print '\t\tOver memory (killed) = ',omem,'/',jobs
        
        command = 'grep "Job was held" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        omemdocker = int("".join(out[0:digits]))
        print '\t\tOver memory (held) = ',omemdocker,'/',jobs,'(might not be unique from over memory killed!)'
        
        command = 'grep "disk" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        odisk = int("".join(out[0:digits]))
        print '\t\tOver disk (killed) = ',odisk,'/',jobs
        
        command = 'grep "(return value 1)" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        crash = int("".join(out[0:digits]))
        command = 'grep "Abnormal termination" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        crash += int("".join(out[0:digits]))
        print '\t\tFile read error (crashed) = ',crash,'/',jobs
        
        command = 'grep "(return value 0)" '+thislog+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        digits = out.find(' ')
        done = int("".join(out[0:digits]))
        totaldone += done
        print '\t\tDONE = ',done,'/',jobs,'=',round(100*float(done)/float(jobs),2),'%, TOTAL DONE =',round(100*float(totaldone)/float(totaljobs),2),'%'
        
        print '\t\tUnknown (running?) =',max(0,jobs-done-crash-odisk-omemdocker-omem),'/',jobs

