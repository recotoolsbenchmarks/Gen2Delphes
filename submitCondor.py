# ********************************************************************************************************
#
# Submission script for Snowmass 2021 Delphes samples
#
# ASSUMPTIONS: you are running on LXPLUS or CMSLPC CONDOR
#
# ARGUMENTS: choose whether you are sending files to 
#            CERN EOS or to FNAL EOS
#    "site":  <CERN, FNAL> this is the site on which you run condor
#    "store": <CERN, FNAL> this is the site for file storage
#    "doNtuples": True/False to process DelphesNtuplizer after delphes (optional, default True)
#    "testjob": True/False to run a 2-job test (optional, default False)
#
# RUN ME: python -u submitCondor_gen.py <CERN,FNAL> <CERN,FNAL> <True/False> <True/False> >& submit.log &
#
# ********************************************************************************************************

import os,sys,time,subprocess

# Create and import the lists of samples to run
print 'Creating and importing file lists...'
from listFiles import *

# Read input arguments
runDir=os.getcwd()
site = sys.argv[1]
store = sys.argv[2]
doNtuples = True
if len(sys.argv) > 3:
    doNtuples = bool(eval(sys.argv[3]))
testjob = False
if len(sys.argv) > 4:
    testjob = bool(eval(sys.argv[4]))

# Manual flag to add more memory to the condor job
morememory = False

# Copy and execute the EOS-safe tools, particularly for FNAL
print '\nSetting up delphes jobs...'
os.system('xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/scripts/EOSSafeUtils.py '+runDir)
execfile(runDir+'/EOSSafeUtils.py')

# Set up storage locations and the delphes card
start_time = time.time()
pileup = '200PU'
card = 'CMS_PhaseII_200PU_Snowmass2021_v0.tcl'

if store == 'CERN':
    url = 'eoscms.cern.ch'
    outputDir='/store/group/upgrade/Snowmass2021/Delphes/'
    ntupleDir='/store/group/upgrade/Snowmass2021/DelphesNtuplizer/'     
else:
    url = 'cmseos.fnal.gov'
    outputDir='/store/user/snowmass/Snowmass2021/Delphes/'
    ntupleDir='/store/user/snowmass/Snowmass2021/DelphesNtuplizer/'

condorDir='condor_logs'

# HOW MANY EVENTS TO RUN???
maxEvtsPerJob = 20000 # -1 --> do not make splitting (1 job per file)

# Access the grid proxy
print 'Getting proxy...'
proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()
print 'ProxyPath:',proxyPath
if site == 'CERN':
    if 'tmp' in proxyPath: 
        print 'Run source environment.(c)sh and make a new proxy!'
        exit(1)
else:
    if len(proxyPath) == 0:
        print 'Issue voms-proxy-init -voms cms before running!'
        exit(1)

print 'Starting submission!'

# Counter for total number of jobs submitted
count=0

# list of files imported from listFiles.py
for sample in fileList:
    print '\n============================================='
    if testjob:
        print '\tTesting sample',sample
    else:
        print '\tWorking on sample',sample

    # Prep the ROOT file list by prepending xrootd accessor
    if '_'+pileup not in sample: continue
    with open(os.path.abspath(sample),'r') as rootlist:
        rootfiles = []
        rootfiles_bare = []
        for line in rootlist:
            if site == 'CERN': 
                rootfiles.append('root://xrootd-cms.infn.it/'+line.strip())
            else: 
                rootfiles.append('root://cmsxrootd.fnal.gov/'+line.strip())
            rootfiles_bare.append(line.strip())
    print '\tTotal files:',len(rootfiles)

    relPath = sample.replace('.txt','').replace('fileLists/','')
    if '_'+pileup in relPath: relPath = relPath.replace('_'+pileup,'')

    # Create the output folders
    os.system('eos root://'+url+'/ mkdir -p '+outputDir+relPath+'_'+pileup)
    os.system('eos root://'+url+'/ mkdir -p '+outputDir+relPath+'_'+pileup)
    condor_dir='%s/%s/%s_%s'%(runDir,condorDir,relPath,pileup)
    os.system('mkdir -p {}'.format(condor_dir))

    os.chdir(condor_dir)
    #print condor_dir, relPath

    # Prepare the condor submission script
    cmdfile="""# here goes your shell script
use_x509userproxy = true
universe = vanilla
Executable = {}/GENtoDelphes.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
output  = condor.$(ClusterId).$(ProcId).out
error   = /dev/null
log     = condor.$(ClusterId).log
Notification = Never
""".format(runDir)

    # Manual memory increase -- only use if resubmitting
    if morememory:
        print '\tIncreasing memory to 3100'
        cmdfile += 'requestMemory = 3100\n'

    # Specific proxy and job flavor settings for CERN
    if site == 'CERN':
        cmdfile += 'x509userproxy = '+proxyPath+'\n'
        cmdfile += '+JobFlavour = "testmatch"\n'

    # Initialize counters for this sample's jobs
    tempcount = 0;
    totaljobs = 0;
    
    # Loop over this sample's ROOT files
    for ifile, file in enumerate(rootfiles):
        if ifile%20 == 0:
            print '\tworking on file',ifile,'...'

        infile = file
        fname_bare = rootfiles_bare[ifile]

        if testjob and ifile > 2: continue 

        # If requesting a split, query DAS for number of events
        n_jobs = 1
        if maxEvtsPerJob > -1:

            command = '/cvmfs/cms.cern.ch/common/dasgoclient --query="file='+fname_bare+' | grep file.nevents" '
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            (out, err) = proc.communicate()
            try: nevents = int(out.split('\n')[0])
            except:
                try: nevents = int(out.split('\n')[1])
                except: print 'ERROR: couldnt isolate the number of events'

            n_jobs = int(nevents) / int(maxEvtsPerJob)
            if int(nevents) % int(maxEvtsPerJob) > 0:
                n_jobs += 1

        totaljobs += n_jobs

        # Split input file into multiple delphes jobs
        for i_split in range(n_jobs):

            outfile = relPath+'_'+str(ifile)+'_'+str(i_split)
            ntuplefile = relPath+'_ntuple_'+str(ifile)+'_'+str(i_split)
            dict={'RUNDIR':runDir, 'RELPATH':relPath, 'FILEIN':infile, 'FILEOUT':outfile, 'OUTPUTDIR':outputDir, 'NTUPLEDIR':ntupleDir, 
                  'NTUPLEOUT':ntuplefile, 'CARD':card, 'URL': url, 'PROXY':proxyPath}

            if maxEvtsPerJob > -1:
                maxEvents = int(maxEvtsPerJob)
                skipEvents = int(maxEvtsPerJob*i_split)
                if i_split == n_jobs-1:
                   maxEvents = nevents - maxEvtsPerJob*(n_jobs-1)

                dict={'RUNDIR':runDir, 'RELPATH':relPath, 'FILEIN':infile, 'FILEOUT':outfile, 'OUTPUTDIR':outputDir, 'NTUPLEDIR':ntupleDir, 
                      'NTUPLEOUT':ntuplefile, 'CARD':card, 'URL': url, 'PROXY':proxyPath, 'SKIPEVENTS':str(skipEvents), 'MAXEVENTS':str(maxEvents)}

            delphesfile = '{}/{}_{}/{}.root'.format(outputDir, relPath, pileup, outfile)
            #flatfile = '{}/{}_{}/{}.root'.format(ntupleDir, relPath, pileup, ntuplefile) # Later, could check for missing flat tree and run different resubmission

            # Check for the existence of the delphes file -- only submit if it's missing
            if not EOSpathExists(delphesfile,url):
                count+=1
                tempcount+=1

                print 'did not find: ', outfile, '  --> (re-)submitting ... '
           
                argstr="Arguments = %(CARD)s %(FILEIN)s %(OUTPUTDIR)s/%(RELPATH)s_200PU %(FILEOUT)s.root %(NTUPLEOUT)s.root %(NTUPLEDIR)s/%(RELPATH)s_200PU 200PU %(URL)s"%dict
                if maxEvtsPerJob > -1: argstr +=" %(MAXEVENTS)s %(SKIPEVENTS)s"%dict
                if doNtuples: argstr +=" 1"
                argstr+="\n"
                
                # Finalize the condor submitter with a set of arguments to queue
                cmdfile += argstr
                cmdfile += 'queue\n'


    # Write the condor submission file
    with open('condor_delphes.sub' , "w") as f:
        f.write(cmdfile)

    # Submit the jobs
    if not testjob:
        print '\tFound totaljobs =',totaljobs,'and submiting',tempcount
        print '\tSample is',round(100.0*(totaljobs-tempcount)/float(totaljobs),2),'% complete'
    print '\tsubmitting {} jobs ... '.format(relPath)
    os.system('condor_submit condor_delphes.sub')

    os.chdir('%s'%(runDir))

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))

