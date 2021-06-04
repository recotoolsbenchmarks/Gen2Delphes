# *****************************************************************
#
# Submission script for Snowmass 2021 Delphes samples
#
# ASSUMPTIONS: you are running on LXPLUS CONDOR
#
# CHOICES: choose whether you are sending files to 
#          CERN EOS or to FNAL EOS
#
# RUN ME: python -u submitCondor_gen.py <CERN,FNAL> >& submit.log &
#
# ******************************************************************

import os,sys,time
from listFiles import *

runDir=os.getcwd()
site = sys.argv[1]

#os.system('xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/scripts/EOSSafeUtils.py '+runDir)
execfile(runDir+'/EOSSafeUtils.py')

start_time = time.time()
pileup = '200PU'
card = 'CMS_PhaseII_200PU_Snowmass2021_v0.tcl'

if site == 'CERN':
    url = 'eoscms.cern.ch'
    outputDir='/store/group/upgrade/RTB/Snowmass2021_test/Delphes/'
    ntupleDir='/store/group/upgrade/RTB/Snowmass2021_test/DelphesNtuplizer/'     
else:
    url = 'cmseos.fnal.gov'
    outputDir='/store/user/snowmass/Snowmass2021_test/Delphes/'
    ntupleDir='/store/user/snowmass/Snowmass2021_test/DelphesNtuplizer/'

condorDir='condor_logs'

maxEvtsPerJob = -1 #50000 for production ## -1 --> do not make splitting (1 job per file)

## Proxy settings differ between CERN and Fermilab...
print 'Getting proxy'
proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()
print 'ProxyPath:',proxyPath
if 'tmp' in proxyPath: 
    print 'Run source environment.(c)sh and make a new proxy!'
    exit(1)

print 'Starting submission'
count=0

# list of files imported from listFiles.py
print 'Samples:',fileList

for sample in fileList:
    if '_'+pileup not in sample: continue
    with open(os.path.abspath(sample),'r') as rootlist:
        rootfiles = []
        rootfiles_bare = []
        for line in rootlist:
            # CERN condor: assume we should read from europe
            rootfiles.append('root://xrootd-cms.infn.it/'+line.strip())
            rootfiles_bare.append(line.strip())
 
    relPath = sample.replace('.txt','').replace('fileLists/','')
    if '_'+pileup in relPath: relPath = relPath.replace('_'+pileup,'')

    # Create the output folders
    os.system('eos root://'+url+'/ mkdir -p '+outputDir+relPath+'_'+pileup)
    os.system('eos root://'+url+'/ mkdir -p '+outputDir+relPath+'_'+pileup)
    condor_dir='%s/%s/%s_%s'%(runDir,condorDir,relPath,pileup)
    os.system('mkdir -p {}'.format(condor_dir))


    os.chdir(condor_dir)
    print condor_dir, relPath

    cmdfile="""# here goes your shell script
use_x509userproxy = true
x509userproxy = {}
universe = vanilla
+JobFlavour = tomorrow
Executable = {}/GENtoDelphes.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
output  = condor.$(ClusterId).$(ProcId).out
error   = condor.$(ClusterId).$(ProcId).err
log     = condor.$(ClusterId).log
#output = /dev/null
#error= /dev/null
#log = /dev/null
Notification = Never
""".format(proxyPath,runDir)

    tempcount = 0;
    for ifile, file in enumerate(rootfiles):
        infile = file

        #print infile
        tempcount+=1
        if tempcount > 2: continue   # OPTIONAL to submit a test job

        fname_bare = rootfiles_bare[ifile]
        #print fname_bare

        ### usual submitter if no splitting
        if not maxEvtsPerJob > -1:
            outfile = relPath+'_'+str(tempcount)
            ntuplefile = relPath+'_ntuple_'+str(tempcount)
            dict={'RUNDIR':runDir, 'RELPATH':relPath, 'FILEIN':infile, 'FILEOUT':outfile, 'OUTPUTDIR':outputDir, 'NTUPLEDIR':ntupleDir, 
                  'NTUPLEOUT':ntuplefile, 'CARD':card, 'URL': url, 'PROXY':proxyPath}

            delphesfile = '{}/{}_{}/{}.root'.format(outputDir, relPath, pileup, outfile)
            #flatfile = '{}/{}_{}/{}.root'.format(ntupleDir, relPath, pileup, ntuplefile) # Later, could check for missing flat tree and run different resubmission

            if not EOSpathExists(delphesfile,url):
                count+=1
                print 'did not find: ', outfile, '  --> (re-)submitting ... '
           
                argstr="Arguments = %(CARD)s %(FILEIN)s %(OUTPUTDIR)s/%(RELPATH)s_200PU %(FILEOUT)s.root $(NTUPLEOUT)s %(NTUPLEDIR)s/%(RELPATH)s_200PU 200PU %(URL)s\n"%dict
                cmdfile += argstr
                cmdfile += 'queue\n'
        else:
            print 'You want to split this job into chunks and they need to implement that!'
            exit(1)

    with open('condor_delphes.sub' , "w") as f:
        f.write(cmdfile)

    # submitting jobs
    print 'submitting {} jobs ... '.format(relPath)
    os.system('condor_submit condor_delphes.sub')

    ## go back to run dir 
    os.chdir('%s'%(runDir))

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))

