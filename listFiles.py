import os,sys

# --------------------------------------------------------
#
# Script to query DAS and get sample information
#
# Set up a list of dataset paths that you want to run by uncommenting lines
#
# GO DOWN TO THE FOR LOOP AND CHOOSE WHICH LIST TO USE!!!!
#
# --------------------------------------------------------

# Put things here in order to run a small test (or just comment things out in a longer list!)
samplelist_test = [
]

samplelist_julie = [
    # New Oct 29 -- for CERN storage
    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',

    ## do with 5100
    #'/TTTJ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    #'/TTTJ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',

    ## do with 4100
    '/TT4b_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/TTZHTo4b_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/TTZToLLNuNu_M-10_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo4B_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    
    ## do with 2100
    '/VBFHHTo4B_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo4B_CV_1_C2V_1_C3_1_withDipoleRecoil_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

    ## do with 2100, 25000 events
    '/TprimeTprime_M-2000_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/TprimeTprime_M-2500_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/TprimeTprime_M-3000_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2Tau_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    '/VBFHHTo2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    '/VBFHHTo2B2Tau_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',

    ## do with 4100, 5000 events
    '/GluGluToHHTo4B_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo4B_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

    # done
    #'/VBFHHTo2B2Tau_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    #'/VBFHHTo2B2Tau_CV_1_C2V_1_C3_1_withDipoleRecoil_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    #'/VBFHHTo2B2Tau_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    #'/VBFHHTo2B2Tau_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    #'/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN', # 20000 events
    #'/TprimeTprime_M-1000_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/TprimeTprime_M-1500_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/DarkPhotonToMuMu_M_0p5_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/DarkPhotonToMuMu_M_0p9_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/DarkPhotonToMuMu_M_2p0_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/SMS-TStauStau_mStau-100_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    #'/GluGluToHHTo2B2Tau_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/TTZJetsToQQ_Dilept_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/TTHHTo4b_5f_LO_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/ggZH_HToGG_ZToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    #'/GluGluToHHTo4B_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/GluGluToHHTo4B_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo4B_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo4B_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo4B_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',

    # WAIT until later, not on disk yet!
    '/TTZZTo4b_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

]

samplelist_sid = [ # Not working anymore, Julie will follow up
    '/DY0Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DY1Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
]

samplelist_julian = [ # Working again Sept? 
    '/DYJetsToLL_0J_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/DYJetsToLL_1J_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_2J_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/DYJetsToLL_3J_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
]

samplelist_soumya = [
    # New 10/29!   Note: Julie took the TT inclusive extension to submit at CERN
    # LEAVE THE ORIGINAL SAMPLES UNCOMMENTED BEFORE THE EXTENSIONS!!!! Otherwise files will get overwritten
    '/TTGamma_Hadronic_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_Hadronic_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    
    # Extensions to submit
    # LEAVE THE ORIGINAL SAMPLES UNCOMMENTED BEFORE THE EXTENSIONS!!!! Otherwise files will get overwritten
    '/TTGamma_Dilept_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_Dilept_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v4/GEN',
    '/TTGamma_Dilept_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext2-v3/GEN',
    
    # Needs follow-up in spreadsheet for number of events processed and/or path to files
    '/DiPhotonJetsBox_MGG-80toInf_14TeV-Sherpa/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/TGJets_leptonic_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGG_0Jets_TuneCUETP8M1_14TeV_amcatnlo_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    ## NOTE about the 3 below: below comment out "if _ext not in sample" to get them to submit successfully!!
    '/TGGJets_leptonic_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN',
    '/TGJets_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/TGJets_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext2-v4/GEN',
    
    #'/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    #'/GluGluToHHTo2B2G_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/GluGluToHHTo2B2G_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v3/GEN',
    #'/GluGluToHHTo2B2G_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_1_C2V_1_C3_1_withDipoleRecoil_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2B2G_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
   
    ]

samplelist_jess = [
    # READY NOW 10/29
    '/QCD_Pt-470to600_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/TGJets_lept_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/QCD_bEnriched_HT200to300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT300to500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT500to700_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',    
    '/WWJJTo2L2Nu2J_SS_EWK_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WWWTo3L3Nu_aQGC_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WWW_4F_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WWZ_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WZTo3LNu_0Jets_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/WZZ_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WminusH_HToBB_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WminusH_HToZZTo4L_M125_14TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WW_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DiPhotonJetsBox_MGG-40to80_14TeV-Sherpa/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-20to7000_EMEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN'
    '/QCD_Pt-15to7000_bcToE_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-5toInf_MuEnrichedPt5_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-0to300_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-600to800_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-1000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCDCCbar_Pt-15to7000_MuEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/WplusH_HToZZTo4L_M125_14TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    
    '/QCD_Pt-300to470_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-800to1000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-15to7000_MuEnrichedPt5_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCDBBar_Pt-15to7000_MuEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToQQ_HT180toInf_14TeV-madgraphMLM-pythia8_GenPt_250GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/DYJetsToQQ_HT180toInf_14TeV-madgraphMLM-pythia8_GenPt_500GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/DYJetsToTauTau_M-50_GenMET-100_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',

]

samplelist_Wenyu = [
    ## NOT REPLICATED 100% as of 10/29
    #'/GluGluToHHTo2G2l2nu_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/GluGluToHHTo2G2l2nu_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    
    # new Sep 01
    '/GluGluToHHTo2G2Z_Inc_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Z_Inc_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2l2nu_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    
    # new Aug 19
    '/GJets_SM_5f_withDipoleRecoil_TuneCP5_QCDInterference_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Qlnu_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Qlnu_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Qlnu_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v3/GEN',
    '/GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v3/GEN',
    '/GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v3/GEN',
    '/GluGluToHHTo2G2Z_Inc_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2Z_Inc_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G2l2nu_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G4Q_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G4Q_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G4Q_node_cHHH2p45_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluToHHTo2G4Q_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/THQ_ctcvcp_HToGG_M125_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/TTHHTo4b_5f_LO_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/TTZJetsToQQ_Dilept_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

    '/QCD_HT1000to1500_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/QCD_HT100to200_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/QCD_HT1500to2000_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/QCD_HT2000toInf_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/QCD_HT500to700_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/QCD_HT50to100_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/QCD_HT700to1000_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/QCD_bEnriched_HT1000to1500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT1500to2000_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT2000toInf_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT700to1000_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/EWKWMinus2Jets_WToLNu_M-50_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/EWKWPlus2Jets_WToLNu_M-50_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/EWKZ2Jets_ZToLL_M-50_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/EWKZ2Jets_ZToNuNu_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',

    # WAIT until later, not on disk yet!
    #'/QCD_HT200to300_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',


]

samplelist_jack = [ # working again in Sept
    # READY TO SUBMIT 10/29
    # LEAVE THE ORIGINAL SAMPLES UNCOMMENTED BEFORE THE EXTENSIONS!!!! Otherwise files will get overwritten
    '/ST_tW_antitop_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN', # started this one already
    '/ST_tW_antitop_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN', # resubmit as pair w/ this one
    '/ST_s-channel_4f_leptonic_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ST_s-channel_4f_leptonic_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ST_tch_14TeV_antitop_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ST_tch_14TeV_antitop_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN',
    
    ## WAIT to resubmit this one -- NOT REPLICATED 100% on 10/29
    '/ST_tW_top_5f_NoFUllyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_top_5f_NoFUllyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    
    # New Sept 8
    '/ST_s-channel_4f_InclusiveDecays_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ST_s-channel_4f_InclusiveDecays_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ST_tW_top_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_top_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ST_tch_14TeV_top_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v3/GEN',
    '/ST_tch_14TeV_top_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN',
    
    '/GluGluHToBB_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToGG_M70_14TeV_amcatnloFXFX_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GluGluHToMuMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToTauTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToWWTo2L2Nu_M125_14TeV_amcatnloFXFX_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GluGluHToZZTo4L_M125_14TeV_powheg2_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToZZTo4L_M125_14TeV_powheg2_minloHJJ_JHUGenV7011_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GluGluToHHTo2B2G_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2G_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2Tau_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2Tau_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2VTo2L2Nu_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2VTo2L2Nu_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2ZTo4L_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/GluGluToHHTo4B_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo4B_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    
   
    ]

samplelist_Emmanuele = [
    ]

samplelist_Sandhya = [
    ## EXTENSION READY 10/29
    # LEAVE THE ORIGINAL SAMPLE UNCOMMENTED BEFORE THE EXTENSIONS!!!! Otherwise files will get overwritten
    '/TTWW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    
    # New Oct 13
    '/ttHToNonbb_M125_TuneCUETP8M2_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ttHTobb_M125_TuneCUETP8M2_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ttH_HToZZ_4L_M125_14TeV_powheg2_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    
    # New Aug 19
    '/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToMuMu_M125_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-BSzpz35_110X_mcRun4_realistic_v3-v2/GEN',

    '/THQ_Hincl_14TeV-TuneCUETP8M1-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/THW_Hincl_14TeV_TuneCUETP8M1-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/TTHH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTHH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTJets_DiLept_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTJets_DiLept_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTTT_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTTT_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTTW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTTW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v4/GEN',
    '/TTWH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v4/GEN',
    '/TTWJetsToLNu_TuneCUETP8M1_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWJetsToLNu_TuneCUETP8M1_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTWW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTZH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTZH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTZJets_TuneCUETP8M2_14TeV_madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTZJets_TuneCUETP8M2_14TeV_madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTZToLL_M-1to10_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/TTZZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTZZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',

    ]

samplelist_Oguz = [
    ## NOT READY to resubmit as of 10/29
    #'/VBFHHTo2G4Q_CV_1_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2G4Q_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',    
    #'/GluGluHToGG_M126_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/TT_Mtt1000toInf_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    #'/ggZH_HToBB_ZToNuNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
   
    # New Oct 13
    '/ggZH_HToBB_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToBB_ZToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',    
    '/ggZH_HToGG_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToGG_ZToNuNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    
    # New July 28
    '/GluGluHToGG_M120_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToGG_M123_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToGG_M124_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToGG_M125_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToGG_M125_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-BSzpz35_110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToGG_M127_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGluHToGG_M130_TuneCP5_14TeV-amcatnloFXFX-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_1_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Qlnu_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_1_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2l2nu_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G4Q_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G4Q_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G4Q_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G4Q_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G4Q_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHToGG_M120_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHToGG_M130_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/ttHJetToGG_M120_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/ttHJetToGG_M125_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/ttHJetToGG_M130_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',    

    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8-GenJetPt-350GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8-GenJetPt-950GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/W0JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/W1JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/W2JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/W3JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/WJetsToQQ_HT180toInf_14TeV-madgraphMLM-pythia8_GenPt_250GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WToLNu_1J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WToLNu_2J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WToLNu_3J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WTolNu01234Jets_5f_LO_MLM_madgraph_V5_2p4p2/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',

    # WAIT until later, not on disk yet!
    #'/WGToLNuG_PtG-40_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    #'/WJetsToLNu_GenMET-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    #'/WJetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    ]

samplelist_Michele = [
    # Updated list Oct 13, already submitted 
    '/DYJets_incl_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    
    # New Sept 16
    '/DoublyChargedHiggsTo4L_M-1100_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/DoublyChargedHiggsTo4L_M-1300_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/DoublyChargedHiggsTo4L_M-300_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/DoublyChargedHiggsTo4L_M-500_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/DoublyChargedHiggsTo4L_M-700_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/DoublyChargedHiggsTo4L_M-900_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/DoublyChargedHiggsToMuMu_M-800_TuneCP5_14TeV-pythia8/SnowmassWinter21GEN-110X_mcRun4_realistic_v3-v1/GEN',

    # New Aug 19
    '/GluGluToHHTo2B2Tau_node_cHHH0_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    '/GluGluToHHTo2B2Tau_node_cHHH1_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v2/GEN',
    '/GluGluToHHTo2B2Tau_node_cHHH5_TuneCP5_14TeV-powheg-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v6/GEN',
    '/VBFHHTo2B2G_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2G_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2G_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2G_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2G_CV_1_C2V_1_C3_1_withDipoleRecoil_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2G_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2B2G_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

    '/VBFHHTo2B2G_CV_1_C2V_1_C3_1_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/VBFHHTo4B_CV_1_C2V_1_C3_1_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/VBFHHToHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/VBFHHToHHTo2B2ZTo4L_CV_1_C2V_1_C3_1_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/VBFHToBB_M-125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBFHToGG_M70_14TeV_amcatnlo_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VBFHToMuMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBFHToTauTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBF_HToInvisible_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/VBF_HToWWTo2L2Nu_M125_14TeV_powheg2_JHUgenV714_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/VBF_HToZZTo4L_M125_14TeV_powheg2_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBF_LFV_HToEMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v3/GEN',
    '/VBF_LFV_HToETau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBF_LFV_HToMuTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VHToGG_M70_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VHToNonbb_M125_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VVTo2L2Nu_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    ]

samplelist_Nan = [
    ## NOT READY to resubmit as of 10/29
    #'/VBFHToGG_M124_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VBFHHTo2G2Tau_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/VHToGG_M127_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    
    ## Need an update in the spreadsheet!! 10/29
    '/VBFHToGG_M123_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHToGG_M126_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHToGG_M127_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',   
    
    # New Aug 19
    '/VBFHHTo2G2Tau_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Tau_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Tau_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Tau_CV_1_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Tau_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Tau_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_0_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_1_5_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_1_C2V_0_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_1_C2V_1_C3_0_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_1_C2V_1_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_1_C2V_1_C3_2_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHHTo2G2Z_Inc_CV_1_C2V_2_C3_1_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VBFHToGG_M125_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

    '/VHToGG_M120_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VHToGG_M123_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VHToGG_M124_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VHToGG_M125_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VHToGG_M126_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/VHToGG_M130_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
]

samplelist_Gamze = [
    ## NOT READY to resubmit as of 10/29
    #'/ttHJetToGG_M127_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    #'/ZGTo2LG_TuneCUETP8M1_14TeV-amcatnloFXFX-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    
    # New Sept 19
    '/WW_DoubleScattering_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUEP8M2T4_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-5toInf_EMEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Mdijet-1000toInf_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',

    # New Aug 19
    '/WGGJets_TuneCP5_14TeV_madgraphMLM_pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/WGJJToLNu_EWK_QCD_TuneCP5_14TeV-madgraph-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/ttHJetToGG_M123_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/ttHJetToGG_M124_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/ttHJetToGG_M126_TuneCP5_14TeV-amcatnloFXFX-madspin-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',

    '/WWG_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WWJJTo2L2Nu2J_SS_QCD_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WWZTo4L2Nu_aQGC_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v3/GEN',
    '/WZG_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WZTo3LNu_1Jets_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/WminusH_HToBB_WToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WminusH_HToCC_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToBB_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToBB_WToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToCC_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZATo2LA01j_5f_pta130_14TeV_NLO_FXFX/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZATo2LA01j_5f_pta500_14TeV_NLO_FXFX/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
]

samplelist_sezen = [
    ## NOT READY to submit/resubmit as of 10/29
    #'/ZH_HToCC_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    
    # New Oct 13
    '/tZq_ll_4f_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/tZq_nunu_4f_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v3/GEN',
    '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    
    # New Aug 19
    '/DY2Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DY3Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-100_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-4to10_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',

    '/ZH_HToBB_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZH_HToBB_ZToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/ZH_HToZZ_M125_14TeV_powheg2-minlo-HZJ_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-100To200_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-1200To2500_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-200To400_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-400To600_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-600To800_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-800To1200_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZZTo2L2Q_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZZTo4L_0Jets_ZZOnShell_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/ZZTo4L_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZZTo4L_1Jets_ZZOnShell_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/ZZZ_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
]

samplelist_meenakshi = [
    ]      

samplelist_TBA = [ #to be assigned later!

]


if not os.path.exists(os.getcwd()+'/fileLists'): os.system('mkdir fileLists')

fileList=[]
    
# CHOOSE WHICH LIST TO RUN OVER HERE!
for sample in samplelist_test:

    print '------------------------------------------'
    print 'Listing',sample

    # print file list to a .txt                                                                              
    if '_ext' not in sample:   ## Broken for samples that are extensions "alone"...comment this out if that's the case!
        os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" > fileLists/'+sample.split('/')[1]+'_200PU.txt')
        fileList.append('fileLists/'+sample.split('/')[1]+'_200PU.txt')
    else:
        os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" >> fileLists/'+sample.split('/')[1]+'_200PU.txt')

    # ----------------------------------------------------------------
    # Theses are utilities that are helpful in case of need...
    #
    # check if this sample has a full file replica
    # os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=-1 --query="site dataset = '+sample+' | grep site.kind, site.name, site.block_fraction, site.block_completion, site.replica_fraction" | awk \'{if ($1=="DISK") print $2, BF $3, BC $4, RF $5}\'')
    #
    # check if this sample is on a T2 or T3...                                                                     
    # os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="site dataset = '+sample+' "')        
    #
    # print number of events                                                                                 
    # os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="dataset = '+sample+' | grep dataset.nevents" ')                       




samplelist_lowpriority = [
    '/DYToLL-M-50_0J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/DYToLL-M-50_1J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/DYToLL-M-50_2J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/DYToLL-M-50_3J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ttHJetToGG_M70_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTZToLLNuNu_M-10_TuneCP5_14TeV-amcatnlo-pythia8/SnowmassWinter21wmLHEGEN-110X_mcRun4_realistic_v3-v1/GEN',
    '/GluGlu_LFV_HToEMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGlu_LFV_HToETau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGlu_LFV_HToMuTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1000_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1400_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1600_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2000_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2300_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-250_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2600_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2900_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-400_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-450_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-500_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-600_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-800_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-900_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M1000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M1500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M2000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M2500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M1000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M1500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M2000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M2500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M1000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M1500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M2000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M2500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-T2HJ_aTleptonic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-T2HJ_aTleptonic_HTobb_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HTobb_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HTobb_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-test_93X_upgrade2023_realistic_v5_ext1-v1/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VLF_MF_100_MS_80_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_100_MS_80_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_100_MS_90_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/VLF_MF_100_MS_90_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_100_MS_95_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VLF_MF_100_MS_95_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_130_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_130_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_140_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_140_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_145_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_145_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_180_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_180_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_190_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_190_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_195_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_195_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/ZPrimeToTTJets_M_10000GeV_W3000GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZPrimeToTTJets_M_2000GeV_W20GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_2000GeV_W600GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_2000GeV_W60GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_3000GeV_W900GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_3000GeV_W90GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_4000GeV_W1200GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_4000GeV_W120GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZPrimeToTTJets_M_4000GeV_W40GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_5000GeV_W1500GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_5000GeV_W150GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_6000GeV_W1800GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_6000GeV_W180GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/ZPrimeToTTJets_M_8000GeV_W2400GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN',
    '/SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17GenOnly-GridpackScan_93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TChiWW_mWMin-0p1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17GenOnly-GridpackScan_93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-100_mLSP-25_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-100_mLSP-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-100_mLSP-75_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-200_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-200_mLSP-150_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-200_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-250_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TA_Tleptonic_kappa_act-Madgraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TA_Tleptonic_kappa_aut-Madgraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Thadronic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Thadronic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HTobb_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-T_Tleptonic_kappa_gct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-T_Tleptonic_kappa_gut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/RSGluonToTTbar_M3000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/RSGluonToTTbar_M4000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/RSGluonToTTbar_M5000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/RSGluonToTTbar_M6000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m1000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m3500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m3750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m6000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m6250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m6500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m1000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m3500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m3750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m6000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m6250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m6500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-250_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-350_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-400_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-450_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-500_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-700_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-800_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-900_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1000_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1400_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1800_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2000_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2300_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2900_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',

    # to be updated in Snowmass2021 campaign
    #'/THW_ctcvcp_HToGG_M125_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    #'/GluGluHToGG_M125_14TeV_amcatnloFXFX_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    #'/VBFHToGG_M125_14TeV_amcatnlo_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    #'/VHToGG_M125_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v3/GEN',
    #'/ttHJetToGG_M125_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
]
