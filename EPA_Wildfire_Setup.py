# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_Setup.m

    ## Setup
    clear
    clc
    addpath(genpath('L:\01 Data\src'))
    #homes
    home.inputs = copy('L:\02 Projects\EPA Wildfire\Inputs')
# EPA_Wildfire_Setup.m:8
    home.proj = copy('\\clusterfs\CLM-Data\CURRENT LOCA\Clipped LOCA2')
# EPA_Wildfire_Setup.m:9
    home.base = copy('\\clusterfs\CLM-Data\CURRENT LOCA\Clipped LOCA2\Observed Baseline')
# EPA_Wildfire_Setup.m:10
    home.outputs = copy('L:\02 Projects\EPA Wildfire\Outputs\6_GCMs')
# EPA_Wildfire_Setup.m:11
    home.graphics = copy(concat([home.outputs,'\Graphics']))
# EPA_Wildfire_Setup.m:12
    home.cluster = copy('\\clusterfs\CLM-Data\CURRENT LOCA')
# EPA_Wildfire_Setup.m:14
    #names
    names.gcms = copy(cellarray(['CanESM2','CCSM4','GISS-E2-R','HadGEM2-ES','MIROC5','GFDL-CM3']))
# EPA_Wildfire_Setup.m:17
    names.rcps = copy(cellarray(['rcp45','rcp85']))
# EPA_Wildfire_Setup.m:19
    names.vars = copy(cellarray(['pr','tasmax','tasmin']))
# EPA_Wildfire_Setup.m:20
    names.projYrs = copy(arange(2006,2099))
# EPA_Wildfire_Setup.m:21
    names.baseYrs = copy(arange(1950,2013))
# EPA_Wildfire_Setup.m:22
    names.mo = copy(cellarray(['01','02','03','04','05','06','07','08','09','10','11','12']))
# EPA_Wildfire_Setup.m:23
    names.firemo = copy(cellarray(['May','June','July','August','September','October']))
# EPA_Wildfire_Setup.m:24
    names.varsH = copy(cellarray(['pr','tasmax','tasmin','wspd','relh','radiation']))
# EPA_Wildfire_Setup.m:25
    names.newvars = copy(cellarray(['rhAnn','rhPAnn','rhPFS','rhPW','prPSu','tasmaxAnn','tasmaxPW','tasmaxSu','BUI','DCmax','DMCmax','PrFS']))
# EPA_Wildfire_Setup.m:26
    names.networks = copy(cellarray(['GSOD','GSOD','GSOD','GSOD','USHCN','USHCN','USHCN','USHCN','GSOD','GSOD','GSOD','USHCN']))
# EPA_Wildfire_Setup.m:28
    names.type = copy(cellarray(['OC','BC']))
# EPA_Wildfire_Setup.m:30
    names.fuels = copy(cellarray(['Light','Medium','Heavy','Duff','Grass','Shrub','Canopy']))
# EPA_Wildfire_Setup.m:31
    #temporal names (era specific)
    names.eras = copy(cellarray(['2030','2050','2070','2090']))
# EPA_Wildfire_Setup.m:34
    names.baseEra = copy(arange(1986,2005))
# EPA_Wildfire_Setup.m:35
    names.projEras = copy(concat([[arange(2020,2039)],[arange(2040,2059)],[arange(2060,2079)],[arange(2080,2099)]]))
# EPA_Wildfire_Setup.m:36
    #numbers
    num.gcms = copy(length(names.gcms))
# EPA_Wildfire_Setup.m:39
    num.rcps = copy(length(names.rcps))
# EPA_Wildfire_Setup.m:40
    num.vars = copy(length(names.vars))
# EPA_Wildfire_Setup.m:41
    num.projYrs = copy(length(names.projYrs))
# EPA_Wildfire_Setup.m:42
    num.baseYrs = copy(length(names.baseYrs))
# EPA_Wildfire_Setup.m:43
    num.eras = copy(length(names.eras))
# EPA_Wildfire_Setup.m:44
    num.baseEra = copy(length(names.baseEra))
# EPA_Wildfire_Setup.m:45
    num.mo = copy(length(names.mo))
# EPA_Wildfire_Setup.m:46
    num.firemo = copy(length(names.firemo))
# EPA_Wildfire_Setup.m:47
    num.modays = copy(concat([31,28,31,30,31,30,31,31,30,31,30,31]))
# EPA_Wildfire_Setup.m:48
    num.modaysLeap = copy(concat([31,29,31,30,31,30,31,31,30,31,30,31]))
# EPA_Wildfire_Setup.m:49
    num.days = copy(365)
# EPA_Wildfire_Setup.m:50
    num.varsH = copy(length(names.varsH))
# EPA_Wildfire_Setup.m:51
    num.lats = copy(458)
# EPA_Wildfire_Setup.m:52
    num.lons = copy(928)
# EPA_Wildfire_Setup.m:53
    num.newvars = copy(length(names.newvars))
# EPA_Wildfire_Setup.m:54
    num.type = copy(length(names.type))
# EPA_Wildfire_Setup.m:55
    num.fuels = copy(length(names.fuels))
# EPA_Wildfire_Setup.m:56
    ## CRUS
    load('L:\01 Data\Meteorological Data\CRU_Historical_Data\cru_ids','CRU_Coord')
    load('\\clusterfs\CLM-Data\CURRENT LOCA\HAWQS Project 10.2017\Outputs\NewVars_cru\Final Files\USproj_LOCA_Base_relh.mat')
    names.crus = copy(key.crus)
# EPA_Wildfire_Setup.m:61
    num.crus = copy(length(names.crus))
# EPA_Wildfire_Setup.m:62
    names.cruLat = copy(CRU_Coord(names.crus,2))
# EPA_Wildfire_Setup.m:63
    names.cruLon = copy(CRU_Coord(names.crus,1))
# EPA_Wildfire_Setup.m:64
    clear('CRU_Coord')
    ## For Graphics
    
    #make mask
    key=xlsread('\\iec-fs03\matlab\02 Projects\EPA CIRA 3\Inputs\Maps and keys\spatial keys and weights\LOCA_state','key')
# EPA_Wildfire_Setup.m:69
    mask=key(arange(),2)
# EPA_Wildfire_Setup.m:71
    clear('key')
    mask[mask != - 999]=1
# EPA_Wildfire_Setup.m:72
    mask[mask != 1]=nan
# EPA_Wildfire_Setup.m:73
    mask2=permute(reshape(mask,concat([num.lons,num.lats])),concat([2,1]))
# EPA_Wildfire_Setup.m:75
    clear('mask')
    #locaMASK (from ManuscriptMaps Setup)
    load('\\clusterfs\CLM-Data\CURRENT LOCA\Clipped LOCA2\Observed Baseline\pr\LOCA_ObsBaselineClip_pr_1959')
    locaMask=ones(size(data(arange(),arange(),1)))
# EPA_Wildfire_Setup.m:79
    locaMask[isnan(data(arange(),arange(),1))]=nan
# EPA_Wildfire_Setup.m:80
    LOCAlats=key.lats
# EPA_Wildfire_Setup.m:82
    LOCAlons=key.lons
# EPA_Wildfire_Setup.m:83
    #make boundary box
    top=dot((90 - (LOCAlats(1) + (1 / 32))),16)
# EPA_Wildfire_Setup.m:86
    top=top + 1
# EPA_Wildfire_Setup.m:87
    
    bottom=dot((90 - (LOCAlats(end()) - (1 / 32))),16)
# EPA_Wildfire_Setup.m:88
    left=dot(((LOCAlons(1) - (1 / 32)) + 180),16)
# EPA_Wildfire_Setup.m:89
    left=left + 1
# EPA_Wildfire_Setup.m:90
    
    right=dot(((LOCAlons(end()) + (1 / 32)) + 180),16)
# EPA_Wildfire_Setup.m:91
    #fullMASK (from ManuscriptMaps Setup)
    fullMask=multiply(locaMask,mask2)
# EPA_Wildfire_Setup.m:94
    clear('mask','mask2','data')
    ## Ecoregion Stuff
#ecoregion key
    __,names.ecoregions=xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\LOCA_EcoregionNetwork','key','A:A',nargout=2)
# EPA_Wildfire_Setup.m:99
    num.ecoregions = copy(length(names.ecoregions))
# EPA_Wildfire_Setup.m:101
    LOCA_GSODcrosswalk=horzcat(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\LOCA_EcoregionNetwork','GSOD','A:A'),(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\LOCA_EcoregionNetwork','GSOD','C:C')))
# EPA_Wildfire_Setup.m:102
    LOCA_USHCNcrosswalk=horzcat(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\LOCA_EcoregionNetwork','USHCN','A:A'),(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\LOCA_EcoregionNetwork','USHCN','C:C')))
# EPA_Wildfire_Setup.m:105
    #CRU key
    CRU_GSODcrosswalk=horzcat(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\CRU_EcoregionNetwork','GSOD','A:A'),(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\CRU_EcoregionNetwork','GSOD','C:C')))
# EPA_Wildfire_Setup.m:110
    CRU_USHCNcrosswalk=horzcat(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\CRU_EcoregionNetwork','USHCN','A:A'),(xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\CRU_EcoregionNetwork','USHCN','C:C')))
# EPA_Wildfire_Setup.m:113