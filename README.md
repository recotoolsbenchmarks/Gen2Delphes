# RTB Gen2Delphes -- Snowmass 2021

These scripts facilitate submitting HTCondor jobs that process a defined set of GEN input files through Delphes.

 * Current CMSSW = CMSSW_10_0_5
 * Current Delphes tag = 3.5.0
 * Current Delphes card **from DelphesNtuplizer** = CMS_Phase2_200PU_Snowmass2021_v0.tcl

## Overview of the important scripts

 * `submitCondor.py` is the main submitter that you will run. Arguments:
   * condor site: FNAL or CERN, choose where you will launch condor jobs
   * storage site: FNAL or CERN, choose where you will store files
   * do ntuples? True (default) or False, choose whether to run DelphesNtuplizer
   * do a test? True or False (default), choose if this should be a short test
 * `GENtoDelphes.sh` is the condor executable to run Delphes and the Ntuplizer
 * `listFiles.py` contains the dataset names to run. 
   * If you are a central submitter then you have a list with your name on it that should be uncommented. 
   * Scroll past the lists to the for loop to make sure it's looping over the list you want!


## Installation and running on FNAL cmslpc

```
cd ~/nobackup
mkdir DelphesProduction
cd DelphesProduction
git clone -b snowmass2021 https://github.com/recotoolsbenchmarks/Gen2Delphes.git 
cd Gen2Delphes

voms-proxy-init -voms cms -valid 168:00
vi/emacs/nano listFiles.py ## EDIT ME TO SHOW YOUR SAMPLES

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
vi/emacs/nano listFiles.py ## EDIT ME TO SHOW YOUR SAMPLES

python -u submitCondor.py CERN <CERN,FNAL> > submit.log 2>&1 &  ## last argument is the storage site

tail -f submit.log ## watch and see
```

**Note:** It's recommended to start with a test job by passing all four arguments, for example `submitCondor.py CERN FNAL True True`. 

**How do I choose whether to use CERN or FNAL as an argument?** You need to know/decide where the output files should be stored. Typically for Snowmass2021 this argument should be `FNAL`. If you wish to send some samples to CERN and others to FNAL, edit `listFiles.py` to only contain samples destined for the same storage site. Run the submitter once for `FNAL` and once for `CERN`. **Leave the first argument as CERN** so that settings are correct for CERN condor.

## Resubmitting jobs

The submitter is set up to check the storage site for the expected Delphes ROOT file. If this file isn't found, the job will be submitted. You can therefore resubmit jobs by simply running the submitter a second time. Currently there is no printout of **why** a job has failed, but this information might be available in either the .out or .job log files. The .err files have been suppressed due to large size. 

**NOTE**: Resubmission is based entirely on the numerical file number, so: 
 * **do not** change the number of events run per job when resubmitting. 
 * remove the EOS output folder and try again from scratch if so many jobs fail that you need to change the number of events setting.  

**If your jobs are held/crashed for going over memory:** Edit submitCondor,py to set the `morememory` flag to True before resubmitting. This will increase the request by 1 GB, you can edit the script to request more if needed but note that this will adversely affect condor priority!

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



