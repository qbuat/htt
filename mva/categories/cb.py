import math
from rootpy.tree import Cut
from .common import (
    Category_Preselection,
    CUTS_2J, CUTS_VBF, CUTS_BOOSTED)

# Documentation:
# https://cds.cern.ch/record/1629891/files/ATL-COM-PHYS-2013-1558.pdf

DETA_JETS = Cut('dEta_jets > 2.6')
MASS_JETS = Cut('mass_jet1_jet2 > 250000')

TAU1_CENTR = Cut('tau1_centrality > %f' % (1. / math.e))
TAU2_CENTR = Cut('tau2_centrality > %f' % (1. / math.e))
TAUS_CENTR = TAU1_CENTR & TAU2_CENTR

CUTS_VBF_CUTBASED = (
    CUTS_VBF
    & DETA_JETS
    & MASS_JETS
    & TAUS_CENTR
    )

CUTS_BOOSTED_CUTBASED = (
    CUTS_BOOSTED
    )

INF = 1E100

# Cut-based categories

class Category_Cuts_VBF_Preselection(Category_Preselection):
    name = 'cuts_vbf_preselection'
    label = '#tau_{had}#tau_{had} CB VBF Preselection'
    cuts = CUTS_VBF_CUTBASED
    norm_category = Category_Preselection


class Category_Cuts_Boosted_Preselection(Category_Preselection):
    name = 'cuts_boosted_preselection'
    label = '#tau_{had}#tau_{had} CB Boosted Preselection'
    cuts = CUTS_BOOSTED_CUTBASED
    norm_category = Category_Preselection


# -----------> Main Categories used in the CB Signal Region
class Category_Cuts_VBF_LowDR(Category_Preselection):
    name = 'cuts_vbf_lowdr'
    label = '#tau_{had}#tau_{had} CB VBF High-p_{T}^{H}'
    latex = '\\textbf{VBF High-$p_T^{H}$}'
    color = 'red'
    jk_number = 11
    linestyle = 'dotted'
    cuts = (
        CUTS_VBF_CUTBASED
        & Cut('dR_tau1_tau2 < 1.5')
        & Cut('resonance_pt > 140000'))
    limitbins = {}
    limitbins[2011] = [0, 64, 80, 92, 104, 116, 132, INF]
    limitbins[2012] = [0, 64, 80, 92, 104, 116, 132, 176, INF]
    norm_category = Category_Preselection


class Category_Cuts_VBF_HighDR_Tight(Category_Preselection):
    name = 'cuts_vbf_highdr_tight'
    label = '#tau_{had}#tau_{had} CB VBF Low-p_{T}^{H} Tight'
    latex = '\\textbf{VBF Low-$p_T^{H}$ Tight}'
    jk_number = 13
    color = 'red'
    linestyle = 'verylongdash'
    cuts = (
        CUTS_VBF_CUTBASED
        & (Cut('dR_tau1_tau2 > 1.5') | Cut('resonance_pt < 140000'))
        & Cut('mass_jet1_jet2 > (-250000 * dEta_jets + 1550000)'))
    # limitbins = [0, 80, 92, 104, 116, 132, 152, INF] - old binning
    limitbins = [0, 80, 104, 132, INF]
    norm_category = Category_Preselection


class Category_Cuts_VBF_HighDR_Loose(Category_Preselection):
    name = 'cuts_vbf_highdr_loose'
    label = '#tau_{had}#tau_{had} CB VBF Low-p_{T}^{H} Loose'
    latex = '\\textbf{VBF Low-$p_T^{H}$ Loose}'
    color = 'red'
    linestyle = 'dashed'
    jk_number = 12
    cuts = (
        CUTS_VBF_CUTBASED
        & (Cut('dR_tau1_tau2 > 1.5') | Cut('resonance_pt < 140000'))
        & Cut('mass_jet1_jet2 < (-250000 * dEta_jets + 1550000)'))
    # limitbins = [0, 64, 80, 92, 104, 116, 132, 152, 176, INF] - old binning
    limitbins = [0, 64, 80, 92, 104, 116, 152, INF]
    norm_category = Category_Preselection


class Category_Cuts_VBF_HighDR(Category_Preselection):
    name = 'cuts_vbf_highdr'
    label = '#tau_{had}#tau_{had} CB VBF Low-p_{T}^{H}'
    latex = '\\textbf{VBF Low-$p_T^{H}$}'
    color = 'red'
    linestyle = 'longdash'
    cuts = Category_Cuts_VBF_HighDR_Loose.cuts | Category_Cuts_VBF_HighDR_Tight.cuts
    # limitbins = [0, 64, 80, 92, 104, 116, 132, 152, INF] - old binning
    limitbins = [0, 80, 92, 104, 116, 132, 152, INF]
    norm_category = Category_Preselection


class Category_Cuts_Boosted_Tight(Category_Preselection):
    name = 'cuts_boosted_tight'
    label = '#tau_{had}#tau_{had} CB Boosted High-p_{T}^{H}'
    latex = '\\textbf{Boosted High-$p_T^{H}$}'
    color = 'blue'
    linestyle = 'verylongdashdot'
    jk_number = 10
    cuts = ((- CUTS_VBF_CUTBASED) & CUTS_BOOSTED_CUTBASED
            & (Cut('dR_tau1_tau2 < 1.5') & Cut('resonance_pt>140000')))
    limitbins = {}
    limitbins[2011] = [0,64,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,140,INF]
    # limitbins[2012] = [0,64,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,140,156,176,INF] - old binning
    limitbins[2012] = [0, 64, 72, 80, 88, 96, 104, 112, 120, 128, 140, 156, 176, INF]
    norm_category = Category_Preselection


class Category_Cuts_Boosted_Loose(Category_Preselection):
    name = 'cuts_boosted_loose'
    label = '#tau_{had}#tau_{had} CB Boosted Low-p_{T}^{H}'
    latex = '\\textbf{Boosted Low-$p_T^{H}$}'
    color = 'blue'
    linestyle = 'dotted'
    jk_number = 9
    cuts = ((- CUTS_VBF_CUTBASED) & CUTS_BOOSTED_CUTBASED
            & (Cut('dR_tau1_tau2 > 1.5') | Cut('resonance_pt<140000')))
    limitbins = {}
    # limitbins[2011] = [0,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,156,200,INF] - old binning
    limitbins[2011] = [0, 80, 88 ,96 ,104 ,112 ,120 ,128, 140, 156, INF]
    # limitbins[2012] = [0,64,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,148,156,176,INF] - old binning
    # limitbins[2012] = [0, 64, 80, 88, 96, 104, 112, 120, 128, 136, 148, 176, INF] # - new binning
    limitbins[2012] = [0, 64, 96, 104, 112, 120, 128, 136, 148, 176, INF] # - alternative new binning
    norm_category = Category_Preselection


# ------------> Categories designed for analysis control plots
class Category_Cuts_VBF_CR(Category_Preselection):
    name = 'cuts_vbf_cr'
    label = '#tau_{had}#tau_{had} CB VBF Control Region'
    latex = '\\textbf{VBF Control Region}'
    cuts  = CUTS_2J


class Category_Cuts_Boosted(Category_Preselection):
    name = 'cuts_boosted_cr'
    label = '#tau_{had}#tau_{had} CB Boosted Control Region'
    cuts = Category_Cuts_Boosted_Tight.cuts | Category_Cuts_Boosted_Loose.cuts
    norm_category = Category_Preselection


class Category_Cuts_Boosted_Tight_NoDRCut(Category_Preselection):
    name = 'cuts_boosted_tight_nodrcut'
    label = '#tau_{had}#tau_{had} CB Boosted Tight No dR Cut'
    cuts = ((- CUTS_VBF_CUTBASED) & CUTS_BOOSTED_CUTBASED
            & Cut('resonance_pt>140000') )
    norm_category = Category_Preselection


# --------> Added by Quentin Buat quentin(dot)buat(at)cern(dot)ch
class Category_Cuts_VBF(Category_Preselection):
    name = 'cuts_vbf'
    label = '#tau_{had}#tau_{had} CB VBF'
    cuts  = Category_Cuts_VBF_HighDR_Loose.cuts | Category_Cuts_VBF_HighDR_Tight.cuts | Category_Cuts_VBF_LowDR.cuts
    limitbins = [0,64,80,92,104,116,132,152,176,INF]
    norm_category = Category_Preselection
