# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_pr.m

    #  Precipitation Variables
    
    #  prPSu*	Average total monthly precipitation (mm) during the summer (June through August) two years previously (t-2)
    
    ## Baseline
    load(concat([home.outputs,'\MAT files\Raw Variables\Base_Ecoregion_pr_Monthly']))
    Base_prPSu=nan(num.ecoregions,num.baseYrs - 2)
# EPA_Wildfire_pr.m:8
    Base_prFS=nan(num.ecoregions,num.baseYrs - 2)
# EPA_Wildfire_pr.m:9
    for yr in arange(1,num.baseYrs - 2).reshape(-1):
        index=find(names.baseYrs == names.baseYrs(yr) + 2)
# EPA_Wildfire_pr.m:11
        Base_prPSu[arange(),yr]=squeeze(mean(data(arange(),arange(6,8),index - 2),2))
# EPA_Wildfire_pr.m:12
        Base_prFS[arange(),yr]=squeeze(mean(data(arange(),arange(5,10),index),2))
# EPA_Wildfire_pr.m:13
    
    clear('data')
    key.dims = copy(cellarray(['ecoregion','year']))
# EPA_Wildfire_pr.m:17
    key.years = copy(arange(names.baseYrs(1) + 2,names.baseYrs(end())))
# EPA_Wildfire_pr.m:18
    key.units = copy('degrees C')
# EPA_Wildfire_pr.m:19
    data=copy(Base_prPSu)
# EPA_Wildfire_pr.m:21
    save(concat([home.outputs,'\MAT files\Derived Variables\Base_Ecoregion_prPSu']),'data','key')
    data=copy(Base_prFS)
# EPA_Wildfire_pr.m:23
    save(concat([home.outputs,'\MAT files\Derived Variables\Base_Ecoregion_prFS']),'data','key')
    ## Projections
    
    names.newyears = copy(arange(2008,2099))
# EPA_Wildfire_pr.m:28
    num.newyears = copy(length(names.newyears))
# EPA_Wildfire_pr.m:29
    load(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_pr_Monthly']))
    prPSu=nan(num.ecoregions,num.newyears,num.gcms,num.rcps,'single')
# EPA_Wildfire_pr.m:33
    prFS=nan(num.ecoregions,num.newyears,num.gcms,num.rcps,'single')
# EPA_Wildfire_pr.m:34
    for yr in arange(1,num.newyears).reshape(-1):
        index=find(names.projYrs == names.newyears(yr))
# EPA_Wildfire_pr.m:36
        prPSu[arange(),yr,arange(),arange()]=squeeze(mean(data(arange(),arange(6,8),index - 2,arange(),arange()),2))
# EPA_Wildfire_pr.m:37
        prFS[arange(),yr,arange(),arange()]=squeeze(mean(data(arange(),arange(5,10),index,arange(),arange()),2))
# EPA_Wildfire_pr.m:38
    
    clear('data')
    key.dims = copy(cellarray(['ecoregion','year','gcm','rcp']))
# EPA_Wildfire_pr.m:43
    key.units = copy('%')
# EPA_Wildfire_pr.m:44
    key.years = copy(names.newyears)
# EPA_Wildfire_pr.m:45
    key.gcms = copy(names.gcms)
# EPA_Wildfire_pr.m:46
    key.rcps = copy(names.rcps)
# EPA_Wildfire_pr.m:47
    data=copy(prPSu)
# EPA_Wildfire_pr.m:48
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_prPSu']),'data','key')
    data=copy(prFS)
# EPA_Wildfire_pr.m:50
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_prFS']),'data','key')