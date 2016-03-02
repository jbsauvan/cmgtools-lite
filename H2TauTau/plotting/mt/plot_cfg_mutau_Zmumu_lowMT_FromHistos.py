import copy

from CMGTools.H2TauTau.proto.plotter.PlotConfigs import HistogramCfg, VariableCfg, BasicHistogramCfg
from CMGTools.H2TauTau.proto.plotter.categories_TauMu import cat_Inc
from CMGTools.H2TauTau.proto.plotter.HistCreator import createHistogram, setSumWeights
from CMGTools.H2TauTau.proto.plotter.HistDrawer import HistDrawer
from CMGTools.H2TauTau.proto.plotter.Variables import all_vars, getVars
from CMGTools.H2TauTau.proto.plotter.cut import Cut

#from CMGTools.H2TauTau.proto.plotter.Samples import samples
from CMGTools.H2TauTau.proto.plotter.Samples import createSampleLists
from CMGTools.H2TauTau.proto.plotter.SamplesFromHisto import createSampleListsFromHisto
#from samples import samples

int_lumi = 2260 

## Output
version = 'v160301'
plot_dir = "controlregions/ZJet/{VERSION}/".format(VERSION=version)
publish_plots = False
publication_dir = "/afs/cern.ch/user/j/jsauvan/www/H2Taus/FakeRate/ControlRegions/ZJet/{VERSION}/".format(VERSION=version)

## templates for histogram and file names
histo_version = 'v_1_2016-03-01'
histo_base_dir = '/afs/cern.ch/work/j/jsauvan/Projects/Htautau_Run2/Histos/StudyFakeRate/MuMu_MTStudy/76X/'
histo_file_template_name = histo_base_dir+'/{SAMPLE}/'+histo_version+'/fakerates_ZMuMu_MTStudy_{SAMPLE}.root'
histo_template_name = '{DIR}hFakeRate_{SEL}_{VAR}' 



# -> Command line
analysis_dir = '/afs/cern.ch/user/j/jsauvan/workspace/public/HTauTau/Trees/mm/v20160220/'
tree_prod_name = 'H2TauTauTreeProducerMuMu'
data_dir = analysis_dir
samples_mc, samples_data, samples, all_samples, sampleDict = createSampleListsFromHisto(analysis_dir=analysis_dir, channel='mm')


selections = []
selections.append('NoIso')
selections.append('Iso_Medium')
selections.append('InvertIso_Medium')


for sample in all_samples:
    ### SumWeights seems to be not correctly filled
    ### Filled them from SkimAnalyzerCount pickle file
    setSumWeights(sample)

# Taken from Variables.py, can get subset with e.g. getVars(['mt', 'mvis'])
variables = [
    VariableCfg(name='mt', binning={'nbinsx':40, 'xmin':0., 'xmax':200.}, unit='GeV', xtitle='m_{T}'),
]

sampleHistoNames = {
    'DYJetsToLL_M50_LO':'Z',
    'WJetsToLNu':'W',
    'TT_pow_ext':'TT',
    'T_tWch':'T_tWch',
    'TBar_tWch':'TBar_tWch',
    'SingleMuon_Run2015D_16Dec':'Data_Run15D',
    'ZZTo4L':'ZZTo4L',
    'WZTo1L3Nu':'WZTo1L3Nu',
    'WWTo1L1Nu2Q':'WWTo1L1Nu2Q',
}



for selection in selections:
    for variable in variables:
        samples_copy = copy.deepcopy(all_samples)
        for sample in samples_copy:
            sampleName = sampleHistoNames[sample.dir_name]
            sample.histo_file_name = histo_file_template_name.format(SAMPLE=sampleName) 
            #sample.histo_name = histo_template_name.format(DIR='NoPUReweight/',SEL=selection,VAR=variable.name)
            sample.histo_name = histo_template_name.format(DIR='',SEL=selection,VAR=variable.name)
        cfg = HistogramCfg(name='{SEL}_{VAR}'.format(SEL=selection,VAR=variable), var=variable, cfgs=samples_copy, lumi=int_lumi)
        plot = createHistogram(cfg, verbose=True)
        plot.Group('VV', ['WWTo1L1Nu2Q','WZTo1L3Nu','ZZTo4L', 'T_tWch', 'TBar_tWch'])
        #HistDrawer.draw(plot, plot_dir=plot_dir, plot_name='{VAR}_{SEL}_Log'.format(VAR=variable.name,SEL=selection), SetLogy=True)
        HistDrawer.draw(plot, plot_dir=plot_dir, plot_name='{VAR}_{SEL}'.format(VAR=variable.name,SEL=selection), SetLogy=False)










