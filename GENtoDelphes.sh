#!/bin/bash

#################################### Wrapper submit script for Upgrade production 
#Written by Alexis Kalogeropoulos - July 2014
#Adapted by Julie Hogan - summer 2016, jmhogan@fnal.gov

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

startTime=`date +%s`

# Condor arguments
CARD=$1
FILEIN=$2
OUTPUT=$3
FILEOUT=$4
NTUPLE=$5
NTUPLEOUT=$6
PILEUP=$7
URL=$8
SKIPEVT=$9
MAXEVT=$10

echo "Starting job on " `date`
echo "Running on " `uname -a`
echo "System release " `cat /etc/redhat-release`

if [[ $# -eq 7 ]] ; then
    echo "Setting SkipEvents to 0, no argument given"
    SKIPEVT=0
    echo "Setting MaxEvents to -1, no argument given"
    MAXEVT=-1
fi

# Set variables
#detCard=CMS_PhaseII_200PU_Snowmass2021_v0.tcl
energy=14
DelphesVersion=tags/3.4.3pre12
nPU=`echo $CARD | cut -d '_' -f 2 | cut -d '.' -f 1`
process=`echo $FILEIN | cut -d '_' -f 1-2`
configuration=`echo $CARD | cut -d '_' -f 1-2`
DelphesOutput=CMSP2_${nPU}_`echo $FILEIN`.root

# Copy and unpack the tarball
echo "xrdcp source tarball and pileup file"
xrdcp -f root://eoscms.cern.ch//store/group/upgrade/RTB/delphes_tarballs/Delphes343pre12_NtuplizerV0.tar tarball.tar
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of Delphes tarball"
    exit $XRDEXIT
fi

tar -xf tarball.tar
rm -f tarball.tar 
cd DelphesNtuplizer/

# Create CMSSW
scram project CMSSW_10_0_5
cd CMSSW_10_0_5/src
eval `scram runtime -sh`
cd -

# Copy in the MinBias file
xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/MinBias_100k.pileup delphes/
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of MinBias_100k.pileup"
    exit $XRDEXIT
fi

setupTime=`date +%s`

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#run MiniAOD through Delphes
# Delphes is already compiled in the tarball

echo "Running delphes with DelphesNtuplizer/cards/$CARD"

## THESE AREN'T ACTUALLY DOING ANYTHING RIGHT NOW IN THE CARD
sed -i "s|MAXEVENTS|${MAXEVT}|g" cards/$CARD
sed -i "s|SKIPEVENTS|${SKIPEVT}|g" cards/$CARD

cd delphes/
./DelphesCMSFWLite ../cards/$CARD ${FILEOUT} ${FILEIN}
DELPHESEXIT=$?
if [[ $DELPHESEXIT -ne 0 ]]; then
    echo "exit code $DELPHESEXIT, failure in DelphesCMSFWLite (maybe from xrootd)"
    exit $DELPHESEXIT
fi

DelphesTime=`date +%s`

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#metadata

echo "User: " `eval whoami`
echo "Date: " `date` 
echo 

echo "Process: " $process 
echo "Pileup Conditions: " $nPU 
echo "Configuration: " $configuration 
echo "Energy: " $energy 
echo 

echo "Input MiniAOD: " $FILEIN
echo "Skipped Events: " $SKIPEVT 
echo "Run Events: " $MAXEVT 
echo 

echo "Delphes Output: " $FILEOUT
echo "Delphes Version: " $DelphesVersion 
echo "Detector Card: " $CARD 
echo 

echo "Minutes spent setting up job: " `expr $setupTime / 60 - $startTime / 60` 
echo "Minutes spent running Delphes: " `expr $DelphesTime / 60 - $setupTime / 60` 
echo 

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Run DelphesNtuplizer

echo "Running Delphes Ntuplizer on $FILEOUT"

cd ../
python bin/Ntuplizer.py -i delphes/$FILEOUT -o $NTUPLE

NtupleTime=`date +%s`

echo "Minutes spent running Ntuplizer: " `expr $NtupleTime / 60 - $DelphesTime / 60`
echo 

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# copy output to eos

echo "xrdcp -f ${FILEOUT} root://${URL}/${OUTPUT}/${FILEOUT}"

xrdcp -f delphes/${FILEOUT} root://${URL}/${OUTPUT}/${FILEOUT} 2>&1  ## FNAL
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of Delphes ROOT file"
    exit $XRDEXIT
fi

xrdcp -f ${NTUPLE} root://${URL}/${NTUPLEOUT}/${NTUPLE} 2>&1  ## FNAL
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of Delphes ROOT file"
    exit $XRDEXIT
fi

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
endTime=`date +%s`
echo "Time spent copying output (s): " `expr $endTime - $NtupleTime`
echo "Total runtime (m): " `expr $endTime / 60 - $startTime / 60`

echo "removing inputs from condor"
rm -f ${FILEOUT}
rm -f ${NTUPLE}
rm -f *.root MinBias_100k.pileup
