import copy

from CMGTools.H2TauTau.proto.plotter.PlotConfigs import HistogramCfg, VariableCfg, BasicHistogramCfg
from CMGTools.H2TauTau.proto.plotter.categories_TauMu import cat_Inc
from CMGTools.H2TauTau.proto.plotter.HistCreator import createHistogram, setSumWeights
from CMGTools.H2TauTau.proto.plotter.HistDrawer import HistDrawer
from CMGTools.H2TauTau.proto.plotter.Variables import all_vars, getVars
from CMGTools.H2TauTau.proto.plotter.helper_methods import getPUWeight

from CMGTools.H2TauTau.proto.plotter.Samples import createSampleLists

from CMGTools.H2TauTau.proto.plotter.binning import binning_svfitMass_finer,binning_svfitMass_mssm 

from FakeFactors import fake_factors_minimal, signal_selection, inverted_selection

int_lumi = 2094.2 # from Alexei's email

#fakeFactorsType = 'ZMuMu'
#histo_version = 'v_2_2016-02-04'
#
#fakeFactorsType = 'HighMT'
#histo_version = 'v_5_2016-02-04'
#
#fakeFactorsType = 'QCDSS'
#histo_version = 'v_2_2016-02-04'
#
#fakeFactorsType = 'Combined'
#histo_version = 'v_2_2016-02-04'
#
fakeFactorsTypes = ['ZMuMu','HighMTRaw','HighMT','QCDSS','Combined']
histo_version = 'v_2_2016-02-08'

analysis_dir = '/afs/cern.ch/work/j/jsauvan/public/HTauTau/Trees/mt/151215/'
samples_mc, samples_data, samples, all_samples, sampleDict = createSampleLists(analysis_dir=analysis_dir)

for sample in all_samples:
    setSumWeights(sample, directory='MCWeighter')

## Output
version  = 'v160208'
plot_dir = "signalRegion/FakeRateEstimation/FakeFactorType_{FAKETYPE}/{VERSION}/"
#publish_plots = True
#publication_dir = "/afs/cern.ch/user/j/jsauvan/www/H2Taus/FakeRate/SignalRegion/FakeRateEstimation/FakeFactorType_{FAKETYPE}/{VERSION}/".format(VERSION=version)

## templates for histogram and file names
#histo_base_dir = '/afs/cern.ch/work/j/jsauvan/Projects/Htautau_Run2/Histos/StudyFakeRate/MuTau/{FAKETYPE}'.format(FAKETYPE=fakeFactorsType)
histo_base_dir = '/afs/cern.ch/work/j/jsauvan/Projects/Htautau_Run2/Histos/StudyFakeRate/MuTau/AllFakeFactors/'
histo_file_template_name = histo_base_dir+'/{SAMPLE}/'+histo_version+'/fakerates_MuTau_{SAMPLE}.root'
histo_template_name = '{DIR}hFakeRate_{SEL}_{VAR}'

# samples to be used
Name = "Name"
DirName = "DirName"
HistoDir = 'HistoDir'
XSection = "XSection"
SumWeights = "SumWeights"
IsData = 'IsData'
histo_samples = [
    {Name:'data_obs'    , DirName:'SingleMuon_Run2015D_v4'   , HistoDir:'Data_Run15D_v4', IsData:True},
    {Name:'data_obs'    , DirName:'SingleMuon_Run2015D_05Oct', HistoDir:'Data_Run15D_05Oct', IsData:True},
    {Name:'fakes_data'  , DirName:'SingleMuon_Run2015D_v4'   , HistoDir:'Data_Run15D_v4', IsData:True},
    {Name:'fakes_data'  , DirName:'SingleMuon_Run2015D_05Oct', HistoDir:'Data_Run15D_05Oct', IsData:True},
    {Name:'ZTT'         , DirName:'DYJetsToLL_M50_LO'  , HistoDir:'ZTT'          , XSection:sampleDict['ZJ'].xsec          , SumWeights:sampleDict['ZJ'].sumweights          },
    {Name:'ZL'          , DirName:'DYJetsToLL_M50_LO'  , HistoDir:'ZL'           , XSection:sampleDict['ZJ'].xsec          , SumWeights:sampleDict['ZJ'].sumweights          },
    #{Name:'W'           , DirName:'WJetsToLNu_LO'      , HistoDir:'W_L', XSection:sampleDict['W'].xsec           , SumWeights:sampleDict['W'].sumweights           },
    {Name:'TT'          , DirName:'TT_pow'             , HistoDir:'TT_L'         , XSection:sampleDict['TT'].xsec          , SumWeights:sampleDict['TT'].sumweights          },
    {Name:'T_tWch'      , DirName:'T_tWch'             , HistoDir:'T_tWch_L'     , XSection:sampleDict['T_tWch'].xsec      , SumWeights:sampleDict['T_tWch'].sumweights      },
    {Name:'TBar_tWch'   , DirName:'TBar_tWch'          , HistoDir:'TBar_tWch_L'  , XSection:sampleDict['TBar_tWch'].xsec   , SumWeights:sampleDict['TBar_tWch'].sumweights   },
    #{Name:'QCD'         , DirName:'QCD_Mu15'           , HistoDir:'', XSection:sampleDict['QCD'].xsec         , SumWeights:sampleDict['QCD'].sumweights         },
    {Name:'ZZTo2L2Q'    , DirName:'ZZTo2L2Q'           , HistoDir:'ZZTo2L2Q_L'   , XSection:sampleDict['ZZTo2L2Q'].xsec    , SumWeights:sampleDict['ZZTo2L2Q'].sumweights    },
    {Name:'WZTo3L'      , DirName:'WZTo3L'             , HistoDir:'WZTo3L_L'     , XSection:sampleDict['WZTo3L'].xsec      , SumWeights:sampleDict['WZTo3L'].sumweights      },
    {Name:'WZTo2L2Q'    , DirName:'WZTo2L2Q'           , HistoDir:'WZTo2L2Q_L'   , XSection:sampleDict['WZTo2L2Q'].xsec    , SumWeights:sampleDict['WZTo2L2Q'].sumweights    },
    {Name:'WZTo1L3Nu'   , DirName:'WZTo1L3Nu'          , HistoDir:'WZTo1L3Nu_L'  , XSection:sampleDict['WZTo1L3Nu'].xsec   , SumWeights:sampleDict['WZTo1L3Nu'].sumweights   },
    {Name:'WZTo1L1Nu2Q' , DirName:'WZTo1L1Nu2Q'        , HistoDir:'WZTo1L1Nu2Q_L', XSection:sampleDict['WZTo1L1Nu2Q'].xsec , SumWeights:sampleDict['WZTo1L1Nu2Q'].sumweights },
    {Name:'VVTo2L2Nu'   , DirName:'VVTo2L2Nu'          , HistoDir:'VVTo2L2Nu_L'  , XSection:sampleDict['VVTo2L2Nu'].xsec   , SumWeights:sampleDict['VVTo2L2Nu'].sumweights   },
    {Name:'WWTo1L1Nu2Q' , DirName:'WWTo1L1Nu2Q'        , HistoDir:'WWTo1L1Nu2Q_L', XSection:sampleDict['WWTo1L1Nu2Q'].xsec , SumWeights:sampleDict['WWTo1L1Nu2Q'].sumweights },
    #{Name:'ZZTo4L'      , DirName:'ZZTo4L'           , XSection:sampleDict['ZZTo4L'].xsec      , SumWeights:sampleDict['ZZTo4L'].sumweights      }   ,
]



## Variables to use
variables = [
    #VariableCfg(name='mvis', binning={'nbinsx':60, 'xmin':0, 'xmax':300}, unit='GeV', xtitle='m_{vis}'),
    VariableCfg(name='mvis_stdbins', binning=binning_svfitMass_finer, unit='GeV', xtitle='m_{vis}'),
    VariableCfg(name='mvis_mssmbins', binning=binning_svfitMass_mssm, unit='GeV', xtitle='m_{vis}'),
    VariableCfg(name='mt'  , binning={'nbinsx':40, 'xmin':0, 'xmax':200}, unit='GeV', xtitle='m_{T}'),
]

## Define fake factors and selections
global_selections = [
    "",
    "MT40_"
]

# Loop over fake factors
for fakeFactorsType in fakeFactorsTypes:
    fake_factors = fake_factors_minimal[fakeFactorsType]
    # Loop on variables
    for variable in variables:
        # Loop on global selections
        for global_selection in global_selections:
            # Loop on fake factors
            for fake_factor in fake_factors:
                ## Prepare histos configs
                samples_tmp = []
                fakes = []
                for sample in histo_samples:
                    config = BasicHistogramCfg(name=sample[Name],
                                             dir_name=sample[DirName],
                                             ana_dir=analysis_dir,
                                             histo_file_name=histo_file_template_name.format(SAMPLE=sample[HistoDir]),
                                             histo_name=histo_template_name.format(DIR='',SEL=global_selection+signal_selection(fake_factor),VAR=variable.name),
                                             is_data=sample.get(IsData, False),
                                             xsec=sample.get(XSection, 1),
                                             sumweights=sample.get(SumWeights,1)
                                             )
                    # Take fakes from the fake-factor directory, inverted isolation
                    if 'fakes' in config.name: 
                        config.histo_name = histo_template_name.format(DIR=fake_factor+'/',SEL=global_selection+inverted_selection(fake_factor),VAR=variable.name) 
                        fakes.append(copy.deepcopy(config))
                    else:
                        samples_tmp.append(copy.deepcopy(config))
                # Add fakes component
                samples_tmp.append( HistogramCfg(name='fakes_data', var=variable, cfgs=fakes, lumi=int_lumi) )
                config = HistogramCfg(name='config', var=variable, cfgs=samples_tmp, lumi=int_lumi)
                plot = createHistogram(config, verbose=True)
                plot.Group('VV', ['WWTo1L1Nu2Q', 'VVTo2L2Nu', 'WZTo1L1Nu2Q', 'WZTo1L3Nu', 'WZTo2L2Q', 'WZTo3L', 'ZZTo2L2Q', 'T_tWch', 'TBar_tWch'])
                HistDrawer.draw(plot, plot_dir=plot_dir.format(FAKETYPE=fakeFactorsType,VERSION=version)+'/'+global_selection+'/'+fake_factor, SetLogy=False)
