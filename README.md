# RTB Gen2Delphes -- Snowmass 2021

These scripts facilitate submitting HTCondor jobs that process a defined set of GEN input files through Delphes.

 * Current CMSSW = CMSSW_10_0_5
 * Current Delphes tag = 3.5.0
 * Current Delphes card **from DelphesNtuplizer** = CMS_Phase2_200PU_Snowmass2021_v0.tcl

## Overview of the important scripts

 * `submitCondor.py` is the main submitter that you will run. Arguments:
   * condor site (REQUIRED): FNAL or CERN, choose where you will launch condor jobs
   * storage site (REQUIRED): FNAL or CERN, choose where you will store files
   * do ntuples? (Optional): True (default) or False, choose whether to run DelphesNtuplizer
   * do a test? (Optional): True or False (default), choose if this should be a short test
   * submit the jobs? (Optional): True (default) or False, choose if the jobs should be submitted
 * `GENtoDelphes.sh` is the condor executable to run Delphes and the Ntuplizer
   * Uses xrdcp to pull in delphes code, compiles it
   * Runs `DelphesCMSFWLite` and then `DelphesNtuplizer`
   * Uses xrdcp to transfer ROOT files to the storage site
 * `listFiles.py` contains the dataset names to run. 
   * If you are a central submitter then you have a list with your name on it -- uncomment whichever lines you want to submit.
   * Scroll past the lists to the for loop to make sure it's looping over the list you want!
   * **Keep extensions grouped**: if a sample has extensions (`_ext1` or similar, same physics process name) keep all the extensions commented or uncommented together in the list when you submit or resubmit!

## Tutorial video: [is available here](https://youtu.be/wrVFHq6mAM8)

## Installation and running on FNAL cmslpc

```
cd ~/nobackup
mkdir DelphesProduction
cd DelphesProduction
git clone -b snowmass2021 https://github.com/recotoolsbenchmarks/Gen2Delphes.git 
cd Gen2Delphes

voms-proxy-init -voms cms -valid 168:00
vi/emacs/nano listFiles.py ## EDIT ME TO SHOW YOUR SAMPLES (see above notes on important scripts)

python -u submitCondor.py FNAL <CERN,FNAL> > submit.log 2>&1 &  ## last argument is the storage site

tail -f submit.log ## watch and see
```

**Note:** It's recommended to start with a test job by passing all four arguments, for example `submitCondor.py FNAL FNAL True True`. 

**How do I choose whether to use CERN or FNAL as an argument?** You need to know/decide where the output files should be stored. Typically for Snowmass2021 this argument should be `FNAL`. If you wish to send some samples to CERN and others to FNAL, edit `listFiles.py` to only contain samples destined for the same storage site. Run the submitter once for `FNAL` and once for `CERN`. **Leave the first argument as FNAL** so that settings are correct for FNAL condor.

## Installation and running on CERN lxplus:

```
# cd /afs/cern.ch/work/<u>/<username>/   # if you have a larger work area
mkdir DelphesProduction
cd DelphesProduction
git clone -b snowmass2021 https://github.com/recotoolsbenchmarks/Gen2Delphes.git 
cd Gen2Delphes

source environment.(c)sh
voms-proxy-init -voms cms -valid 168:00
vi/emacs/nano listFiles.py ## EDIT ME TO SHOW YOUR SAMPLES (see above notes on important scripts)

python -u submitCondor.py CERN <CERN,FNAL> > submit.log 2>&1 &  ## last argument is the storage site

tail -f submit.log ## watch and see
```

**Note:** It's recommended to start with a test job by passing all four arguments, for example `submitCondor.py CERN FNAL True True`. 

**How do I choose whether to use CERN or FNAL as an argument?** You need to know/decide where the output files should be stored. Typically for Snowmass2021 this argument should be `FNAL`. If you wish to send some samples to CERN and others to FNAL, edit `listFiles.py` to only contain samples destined for the same storage site. Run the submitter once for `FNAL` and once for `CERN`. **Leave the first argument as CERN** so that settings are correct for CERN condor.

## Checking the status

Your first tool is `condor_q`! If jobs for a certain cluster are still running, resubmission is not advised. Commands like `condor_q -held yourusername` are useful to check the reason for held jobs. 

If the jobs have finished in condor there are several possibilities: success, crashing, or automated removal for using too many resources. You can test the success status of your jobs using `errorReport.py`, which queries the condor log file for termination messages:

```
python -u errorReport.py >& errorReport.log &
```

The output for each sample might look like: 
```
=============================================
Working on sample TTZHTo4b_TuneCP5_14TeV-madgraph-pythia8_200PU
Sample has 2 log files
        Working on this log: condor_logs/TTZHTo4b_TuneCP5_14TeV-madgraph-pythia8_200PU/condor.72114647.log
                Over memory (killed) =  9 / 82
                Over memory (held) =  42 / 82 (might not be unique from over memory killed!)
                Over disk (killed) =  0 / 82
                File read error (crashed) =  12 / 82
                DONE =  27 / 82 = 32.93 %, TOTAL DONE = 32.93 %
                Unknown (running?) = 0 / 82
```

Studying whether the majority of the failures are due to running over memory, over wall time, over disk space, or file read errors can inform how you choose to resubmit jobs.

## Resubmitting jobs

The submitter is set up to check the storage site for the expected Delphes ROOT file. If this file isn't found, the job will be submitted. You can therefore resubmit jobs by simply **running the submitter a second time**. 

**NOTE**: Resubmission is based entirely on the numerical file number, so: 
 * **Do not** change the number of events run per job when resubmitting. 
 * **Wait** until all your condor jobs are finished running (held is ok, kill those) before resubmitting.
 * **Remove** the EOS output folder and try again from scratch if so many jobs fail that you need to change the number of events setting.  

**If your jobs are held/crashed for going over memory:** Edit submitCondor,py to set the `morememory` flag to True before resubmitting. This will increase the request by 1 GB, you can edit the script to request more if needed but note that this will adversely affect condor priority!

**If your jobs are experiencing file read errors:** Make sure your voms proxy is in good shape with a long lifetime so that you do not experience authorization failures (see the `voms-proxy-init` command in the installation instructions). Given a good proxy, these are likely site issues that we cannot control. 

## To change the CMSSW or Delphes settings (ADVANCED)

Follow the instructions on the DelphesNtuplizer github repository to install both the Ntuplizer and Delphes. For simplicity, **do this on lxplus**. 

Make any edits to the card and delphes source code:
 * Cards should be placed in the DelphesNtuplizer/cards/ folder
 * Optimally, name the card: CMS_Phase2_200PU_Snowmass2021_SomeNewLabelHere.tcl
 * **In the PileupMerger section, choose the MinBias_100k line, NOT the /eos/ path!**

Form a tarball will the fully compiled code: 

`tar --exclude="DelphesNtuplizer/.git --exclude="DelphesNtuplizer/delphes/.git" --exclude="DelphesNtuplizer/delphes/tmp" -zcf /eos/cms/store/group/upgrade/RTB/delphes_tarballs/<newnamehere>.tar DelphesNtuplizer/`

Edit `GENtoDelphes.sh` to reflect these changes. In particular:
 * architecture, if needed.
 * delphes card name
 * delphes tag (for metadata only)
 * CMSSW version
 * delphes tarball name



