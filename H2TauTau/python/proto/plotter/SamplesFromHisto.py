from CMGTools.H2TauTau.proto.plotter.PlotConfigs import BasicHistogramCfg
from CMGTools.H2TauTau.proto.plotter.HistCreator import setSumWeights

from CMGTools.H2TauTau.proto.samples.fall15.htt_common import TT_pow_ext, DYJetsToLL_M50_LO, WJetsToLNu, WWTo2L2Nu, T_tWch, TBar_tWch, TToLeptons_tch_amcatnlo, ZZTo4L, WZTo3L, WZTo1L3Nu, WWTo1L1Nu2Q, TBarToLeptons_tch_powheg, TToLeptons_tch_powheg, mssm_signals


def createSampleListsFromHisto(analysis_dir='/afs/cern.ch/user/s/steggema/work/public/mt/NewProd',
                      channel='mt', 
                      ztt_cut='(l2_gen_match == 5)', zl_cut='(l2_gen_match < 5)',
                      zj_cut='(l2_gen_match == 6)'):
    # -> Possibly from cfg like in the past, but may also make sense to enter directly
    if channel == 'mt':
        tree_prod_name='H2TauTauTreeProducerTauMu'
    elif channel == 'et':
        tree_prod_name='H2TauTauTreeProducerTauEle'
    elif channel == 'mm':
        tree_prod_name='H2TauTauTreeProducerMuMu'
    elif channel == 'tt':
        tree_prod_name='H2TauTauTreeProducerTauTau'
    elif channel == 'em':
        tree_prod_name='H2TauTauTreeProducerMuEle'

    # -> Possibly from cfg like in the past, but may also make sense to enter directly
    samples_essential = [
        #BasicHistogramCfg(name='ZTT', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents),
        #BasicHistogramCfg(name='ZL', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents),
        #BasicHistogramCfg(name='ZJ', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents),
        BasicHistogramCfg(name='ZL', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents),
        BasicHistogramCfg(name='W', dir_name='WJetsToLNu', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=WJetsToLNu.xSection, sumweights=WJetsToLNu.nGenEvents),
        #SampleCfg(name='TT', dir_name='TT_pow_ext' if 'TauEle' in tree_prod_name else 'TT_pow', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TT_pow.xSection, sumweights=TT_pow.nGenEvents),
        BasicHistogramCfg(name='TT', dir_name='TT_pow_ext', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=TT_pow_ext.xSection, sumweights=TT_pow_ext.nGenEvents),
        BasicHistogramCfg(name='T_tWch', dir_name='T_tWch', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=T_tWch.xSection, sumweights=T_tWch.nGenEvents),
        BasicHistogramCfg(name='TBar_tWch', dir_name='TBar_tWch', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=TBar_tWch.xSection, sumweights=TBar_tWch.nGenEvents),
        #BasicHistogramCfg(name='QCD', dir_name='QCD_Mu15', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=QCD_Mu15.xSection)
    ]
    samples_data = []
    if channel in ['mt', 'mm']:
        samples_data = [
            BasicHistogramCfg(name='data_obs', dir_name='SingleMuon_Run2015D_16Dec', ana_dir=analysis_dir, histo_file_name='', histo_name='', is_data=True),
        ]
    elif channel in ['et']:
        samples_data = [
            BasicHistogramCfg(name='data_obs', dir_name='SingleElectron_Run2015D_16Dec', ana_dir=analysis_dir, histo_file_name='', histo_name='', is_data=True),
        ]
    elif channel in ['tt']:
        samples_data = [
            BasicHistogramCfg(name='data_obs', dir_name='Tau_Run2015D_16Dec', ana_dir=analysis_dir, histo_file_name='', histo_name='', is_data=True),
        ]


    samples_additional = [
        # SampleCfg(name='TToLeptons_tch', dir_name='TToLeptons_tch_amcatnlo', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TToLeptons_tch_amcatnlo.xSection, sumweights=TToLeptons_tch_amcatnlo.nGenEvents),
        #SampleCfg(name='TToLeptons_tch_powheg', dir_name='TToLeptons_tch_powheg', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TToLeptons_tch_powheg.xSection, sumweights=TToLeptons_tch_powheg.nGenEvents),
        #SampleCfg(name='TBarToLeptons_tch_powheg', dir_name='TBarToLeptons_tch_powheg', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TBarToLeptons_tch_powheg.xSection, sumweights=TBarToLeptons_tch_powheg.nGenEvents),
    ]
    #if 'TauMu' in tree_prod_name or 'MuMu' in tree_prod_name:
            #samples_additional += [SampleCfg(name='ZZ', dir_name='ZZp8', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=ZZp8.xSection, sumweights=ZZp8.nGenEvents),
            #SampleCfg(name='WZ', dir_name='WZ', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WZp8.xSection, sumweights=WZp8.nGenEvents),
            #SampleCfg(name='WW', dir_name='WWTo2L2Nu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WWTo2L2Nu.xSection, sumweights=WWTo2L2Nu.nGenEvents),
            #]
    #else:
    samples_additional += [
        BasicHistogramCfg(name='ZZTo4L', dir_name='ZZTo4L', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=ZZTo4L.xSection, sumweights=ZZTo4L.nGenEvents),
        #BasicHistogramCfg(name='ZZTo2L2Q', dir_name='ZZTo2L2Q', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=ZZTo2L2Q.xSection, sumweights=ZZTo2L2Q.nGenEvents),
        #BasicHistogramCfg(name='WZTo3L', dir_name='WZTo3L', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=WZTo3L.xSection, sumweights=WZTo3L.nGenEvents),
        #BasicHistogramCfg(name='WZTo2L2Q', dir_name='WZTo2L2Q', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=WZTo2L2Q.xSection, sumweights=WZTo2L2Q.nGenEvents),
        BasicHistogramCfg(name='WZTo1L3Nu', dir_name='WZTo1L3Nu', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=WZTo1L3Nu.xSection, sumweights=WZTo1L3Nu.nGenEvents),
        #BasicHistogramCfg(name='WZTo1L1Nu2Q', dir_name='WZTo1L1Nu2Q', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=WZTo1L1Nu2Q.xSection, sumweights=WZTo1L1Nu2Q.nGenEvents),
        #BasicHistogramCfg(name='VVTo2L2Nu', dir_name='VVTo2L2Nu', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=VVTo2L2Nu.xSection, sumweights=VVTo2L2Nu.nGenEvents),
        BasicHistogramCfg(name='WWTo1L1Nu2Q', dir_name='WWTo1L1Nu2Q', ana_dir=analysis_dir, histo_file_name='', histo_name='', xsec=WWTo1L1Nu2Q.xSection, sumweights=WWTo1L1Nu2Q.nGenEvents),
    ]


    samples_mc = samples_essential + samples_additional
    samples = samples_essential + samples_data
    all_samples = samples_mc + samples_data
    # -> Can add cross sections for samples either explicitly, or from file, or from cfg
    for sample in samples_mc:
        setSumWeights(sample)

    sampleDict = {s.name:s for s in all_samples}

    return samples_mc, samples_data, samples, all_samples, sampleDict

#samples_mc, samples_data, samples, all_samples, sampleDict = createSampleListsFromHisto()

