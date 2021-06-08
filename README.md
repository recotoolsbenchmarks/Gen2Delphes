# RTB Gen2Delphes -- Snowmass 2021

These scripts facilitate submitting HTCondor jobs that process a defined set of GEN input files through Delphes.

 * Current CMSSW = CMSSW_10_0_5
 * Current Delphes tag = 3.5.0
 * Current Delphes card **from DelphesNtuplizer** = CMS_Phase2_200PU_Snowmass2021_v0.tcl

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
**How do I choose whether to use CERN or FNAL as an argument?** You need to know/decide where the output files should be stored. Typically for Snowmass2021 this argument should be `FNAL`. If you wish to send some samples to CERN and others to FNAL, edit `listFiles.py` to only contain samples destined for the same storage site. Run the submitter once for `FNAL` and once for `CERN`. **Leave the first argument as CERN** so that settings are correct for CERN condor.

## Resubmitting jobs

The submitter is set up to check the storage site for the expected Delphes ROOT file. If this file isn't found, the job will be submitted. You can therefore resubmit jobs by simply running the submitter a second time. Currently there is no printout of **why** a job has failed, but this information should be available in either the .out or .job log files. The .err files have been suppressed due to large size. 

## To change the CMSSW or Delphes settings (ADVANCED)

Follow the instructions on the DelphesNtuplizer github repository to install both the Ntuplizer and Delphes. For simplicity, **do this on lxplus**. 
Make any edits to the card and Delphes source code:
 * Cards should be placed in the CMS_Phase2/ folder
 * Optimally, name the card: CMS_Phase2_200PU_SomeNewLabelHere.tcl
 * **In the PileupMerger section, choose the MinBias_100k line, NOT the /eos/ path!**

Form a tarball will the fully compiled code: 

`tar --exclude="DelphesNtuplizer/.git --exclude="DelphesNtuplizer/delphes/.git" --exclude="DelphesNtuplizer/CMSSW_10_0_5" --exclude="DelphesNtuplizer/delphes/tmp" -zcf /eos/cms/store/group/upgrade/RTB/delphes_tarballs/<newnamehere>.tar DelphesNtuplizer/`

Edit `GENtoDelphes.sh` to reflect these changes. In particular:
 * architecture, if needed.
 * delphes card name
 * delphes tag (for metadata only)
 * CMSSW version
 * delphes tarball name



