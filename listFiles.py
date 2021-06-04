import os,sys

samplelist = [

    # samples we've been using
    '/MultiTau_PT15to500/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v3/FEVT',
    '/DoublePhoton_FlatPt-1To100/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v3/FEVT',
    '/DoubleElectron_FlatPt-1To100/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/GEN-SIM-DIGI-RAW-MINIAOD',
    '/DoubleMuon_gun_FlatPt-1To100/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/TT_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/FEVT',
    '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_pilot_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/GluGluHToTauTau_M125_14TeV_powheg_pythia8_TuneCP5/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD',
    '/GluGluHToGG_M125_14TeV_powheg_pythia8_TuneCP5/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_withNewMB_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD'
    '/GluGluToHHTo2B2Tau_node_SM_TuneCP5_14TeV-madgraph-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext1-v3/FEVT',
    '/GluGluToHHTo2B2G_node_SM_TuneCP5_14TeV-madgraph_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_castor_111X_mcRun4_realistic_T15_v1-v1/FEVT',

    # more leptons and taus, hopefully in barrel+endcap
]

samplelist_rev = [
    # samples we've been using
    '/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_castor_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/GluGluToHHTo2B2G_node_SM_TuneCP5_14TeV-madgraph_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/GluGluHToGG_M125_14TeV_powheg_pythia8_TuneCP5/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_withNewMB_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD'
    '/GluGluToHHTo2B2Tau_node_SM_TuneCP5_14TeV-madgraph-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext1-v3/FEVT',
    '/GluGluHToTauTau_M125_14TeV_powheg_pythia8_TuneCP5/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD',
    '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_pilot_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/TT_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/FEVT',
    '/DoubleMuon_gun_FlatPt-1To100/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/DoubleElectron_FlatPt-1To100/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/GEN-SIM-DIGI-RAW-MINIAOD',
    '/DoublePhoton_FlatPt-1To100/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v3/FEVT',
    '/MultiTau_PT15to500/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v2/FEVT',
]


samplelist_test = [
    #'/MultiTau_PT15to500/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v2/FEVT',
    #'/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_pilot_111X_mcRun4_realistic_T15_v1-v1/FEVT',
    '/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToMuMu_M125_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-BSzpz35_110X_mcRun4_realistic_v3-v2/GEN',
    #'/GluGluToHHTo2B2G_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/TT_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-Pilot_110X_mcRun4_realistic_v3-v1/GEN',
]

if not os.path.exists(os.getcwd()+'/fileLists'): os.system('mkdir fileLists')


fileList=[]
    
#for sample in samplelist:
#for sample in samplelist_rev:
for sample in samplelist_test:

    print '------------------------------------------'
    print 'Listing',sample

    # print file list to a .txt                                                                              
    #if 'PU200' in sample:
    if '_ext' not in sample and '_pilot2' not in sample:            
        print '/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" > fileLists/'+sample.split('/')[1]+'_200PU.txt'
        os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" > fileLists/'+sample.split('/')[1]+'_200PU.txt')
        fileList.append('fileLists/'+sample.split('/')[1]+'_200PU.txt')
    else:
        os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" >> fileLists/'+sample.split('/')[1]+'_200PU.txt')
        fileList.append('fileLists/'+sample.split('/')[1]+'_200PU.txt')

    # elif 'NoPU' in sample:
    #     if '_ext' not in sample:
    #         os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" > fileLists/'+sample.split('/')[1]+'_0PU.txt')
    #         fileList.append('fileLists/'+sample.split('/')[1]+'_0PU.txt')
    #     else:
    #         os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" >> fileLists/'+sample.split('/')[1]+'_0PU.txt')
    #         fileList.append('fileLists/'+sample.split('/')[1]+'_0PU.txt')

    # check if this sample is on a T2 or T3...                                                                     
    #os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="site dataset = '+sample+'"')        

    # print number of events                                                                                 
    #os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="dataset = '+sample+' | grep dataset.nevents" ')                       


