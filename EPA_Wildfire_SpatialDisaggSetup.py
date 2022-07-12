# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_SpatialDisaggSetup.m

    ## Spatial Disaggregation Setup
    
    #Setup: Load key to create names
#Setup: Load key to create names
    load(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_AllVars']))
    clear('data')
    names.varsReg = copy(key.vars)
# EPA_Wildfire_SpatialDisaggSetup.m:8
    names.yrsReg = copy(key.years)
# EPA_Wildfire_SpatialDisaggSetup.m:9
    names.ecoReg = copy(key.ecoregions.T)
# EPA_Wildfire_SpatialDisaggSetup.m:10
    num.ecoReg = copy(length(names.ecoReg))
# EPA_Wildfire_SpatialDisaggSetup.m:11
    num.yrsReg = copy(length(names.yrsReg))
# EPA_Wildfire_SpatialDisaggSetup.m:12
    
    num.varsReg = copy(length(names.varsReg))
# EPA_Wildfire_SpatialDisaggSetup.m:13
    names.ecoReg[2]='NevadaMtns'
# EPA_Wildfire_SpatialDisaggSetup.m:15
    names.ecoReg[3]='EasternRockiesGreatPlains'
# EPA_Wildfire_SpatialDisaggSetup.m:16
    #Load Projection Data
    load(concat([home.outputs,'\MAT files\Derived Variables\EcoregionRegs_DerivedProj']))
    proj=copy(data)
# EPA_Wildfire_SpatialDisaggSetup.m:20
    clear('data')
    #Load Baseline Data
    load(concat([home.outputs,'\MAT files\Derived Variables\EcoregionRegs_DerivedBase']))
    base=copy(data)
# EPA_Wildfire_SpatialDisaggSetup.m:25
    clear('data')
    #Generate names
    names.firemo = copy(cellarray(['May','June','July','August','September','October']))
# EPA_Wildfire_SpatialDisaggSetup.m:29
    num.firemo = copy(length(names.firemo))
# EPA_Wildfire_SpatialDisaggSetup.m:30
    num.ecosyst = copy(arange(1,4))
# EPA_Wildfire_SpatialDisaggSetup.m:31
    #Important Arrays for Spatial Disaggregation
    
    areafrac=xlsread(concat([home.inputs,'\Data Files\HalfDegree_Ecoregion.xlsx']),'Tables','C5:F10')
# EPA_Wildfire_SpatialDisaggSetup.m:35
    burnfrac=xlsread(concat([home.inputs,'\Data Files\HalfDegree_Ecoregion.xlsx']),'Tables','C17:F22')
# EPA_Wildfire_SpatialDisaggSetup.m:36
    ecotable=xlsread(concat([home.inputs,'\Data Files\HalfDegree_Ecoregion.xlsx']),'KeyEco','A2:D19')
# EPA_Wildfire_SpatialDisaggSetup.m:37
    gridded=xlsread(concat([home.inputs,'\Data Files\HalfDegree_Ecoregion.xlsx']),'HalfDegree_Ecoregion','K2:Q1588')
# EPA_Wildfire_SpatialDisaggSetup.m:38
    num.grid = copy(length(gridded(arange(),1)))
# EPA_Wildfire_SpatialDisaggSetup.m:39