# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_tasmax.m

    #  Maximum Temperature Variables
    
    # TmaxAnn*	Annual average monthly maximum temperature (°C) for  the current year
# TmaxPW*	Average monthly maximum temperature (°C) during the previous year’s winter (December through February)
# TmaxSu*	Average monthly maximum temperature (°C) during the current year’s summer (June through August)
    
    ## Baseline
    load(concat([home.outputs,'\MAT files\Raw Variables\Base_Ecoregion_tasmax_monthly']))
    Base_tasmaxAnn=nan(num.ecoregions,num.baseYrs - 2)
# EPA_Wildfire_tasmax.m:10
    Base_tasmaxPW=nan(num.ecoregions,num.baseYrs - 2)
# EPA_Wildfire_tasmax.m:11
    Base_tasmaxSu=nan(num.ecoregions,num.baseYrs - 2)
# EPA_Wildfire_tasmax.m:12
    for yr in arange(1,num.baseYrs - 2).reshape(-1):
        index=find(names.baseYrs == names.baseYrs(yr) + 2)
# EPA_Wildfire_tasmax.m:15
        Base_tasmaxAnn[arange(),yr]=squeeze(mean(data(arange(),arange(),index),2))
# EPA_Wildfire_tasmax.m:16
        Base_tasmaxPW[arange(),yr]=squeeze((data(arange(),12,index - 1) + sum(data(arange(),arange(1,2),index),2)) / 3)
# EPA_Wildfire_tasmax.m:17
        Base_tasmaxSu[arange(),yr]=squeeze(mean(data(arange(),arange(6,8),index),2))
# EPA_Wildfire_tasmax.m:18
    
    clear('data')
    key.dims = copy(cellarray(['ecoregion','year']))
# EPA_Wildfire_tasmax.m:23
    key.years = copy(arange(names.baseYrs(1) + 2,names.baseYrs(end())))
# EPA_Wildfire_tasmax.m:24
    key.units = copy('degrees C')
# EPA_Wildfire_tasmax.m:25
    data=copy(Base_tasmaxAnn)
# EPA_Wildfire_tasmax.m:27
    save(concat([home.outputs,'\MAT files\Derived Variables\Base_Ecoregion_tasmaxAnn']),'data','key')
    clear('data')
    data=copy(Base_tasmaxPW)
# EPA_Wildfire_tasmax.m:30
    save(concat([home.outputs,'\MAT files\Derived Variables\Base_Ecoregion_tasmaxPW']),'data','key')
    clear('data')
    data=copy(Base_tasmaxSu)
# EPA_Wildfire_tasmax.m:33
    save(concat([home.outputs,'\MAT files\Derived Variables\Base_Ecoregion_tasmaxSu']),'data','key')
    ## Projections
    
    names.newyears = copy(arange(2008,2099))
# EPA_Wildfire_tasmax.m:37
    num.newyears = copy(length(names.newyears))
# EPA_Wildfire_tasmax.m:38
    tasmaxAnn=nan(num.ecoregions,num.newyears,num.gcms,num.rcps)
# EPA_Wildfire_tasmax.m:40
    tasmaxPW=nan(num.ecoregions,num.newyears,num.gcms,num.rcps)
# EPA_Wildfire_tasmax.m:41
    tasmaxSu=nan(num.ecoregions,num.newyears,num.gcms,num.rcps)
# EPA_Wildfire_tasmax.m:42
    load(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_tasmax_monthly']))
    for yr in arange(1,num.newyears).reshape(-1):
        index=find(names.projYrs == names.newyears(yr))
# EPA_Wildfire_tasmax.m:47
        tasmaxAnn[arange(),yr,arange(),arange()]=squeeze(mean(data(arange(),arange(),index,arange(),arange()),2))
# EPA_Wildfire_tasmax.m:48
        tasmaxPW[arange(),yr,arange(),arange()]=squeeze((data(arange(),12,index - 2,arange(),arange()) + sum(data(arange(),arange(1,2),index - 1,arange(),arange()),2)) / 3)
# EPA_Wildfire_tasmax.m:49
        tasmaxSu[arange(),yr,arange(),arange()]=squeeze(mean(data(arange(),arange(6,8),index,arange(),arange()),2))
# EPA_Wildfire_tasmax.m:51
    
    clear('data')
    key.dims = copy(cellarray(['ecoregion','year']))
# EPA_Wildfire_tasmax.m:57
    key.units = copy('%')
# EPA_Wildfire_tasmax.m:58
    key.years = copy(names.newyears)
# EPA_Wildfire_tasmax.m:59
    data=copy(tasmaxAnn)
# EPA_Wildfire_tasmax.m:61
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_tasmaxAnn']),'data','key')
    clear('data')
    data=copy(tasmaxPW)
# EPA_Wildfire_tasmax.m:64
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_tasmaxPW']),'data','key')
    clear('data')
    data=copy(tasmaxSu)
# EPA_Wildfire_tasmax.m:67
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_tasmaxSu']),'data','key')