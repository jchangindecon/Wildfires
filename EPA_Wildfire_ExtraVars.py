# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_ExtraVars.m

    #  Extra Variables
    
    # 9 BUI**	Average daily BUI during the current year’s fire season (May through October)
# 10 DCmax**	Maximum daily DC during the current year’s fire season (May through October)
# 11 DMCmax**	Maximum daily DMC during the current year’s fire season (May through October)
# 
# ** Daily estimates of these variables should be calculated using the logic provided below this table. 
# For these variables the daily estimates should be used to determine maximum or average seasonal values.
    
    ## Setup
    clear('fullMask','locaMask')
    tic
    # create arrays that store month-specific values
    lmon=concat([[31],[28],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]])
# EPA_Wildfire_ExtraVars.m:15
    lmonLeap=concat([[31],[29],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]])
# EPA_Wildfire_ExtraVars.m:16
    el=concat([[6.5],[7.5],[9.0],[12.8],[13.9],[13.9],[12.4],[10.9],[9.4],[8.0],[7.0],[6.0]])
# EPA_Wildfire_ExtraVars.m:17
    fl=concat([[- 1.6],[- 1.6],[- 1.6],[0.9],[3.8],[5.8],[6.4],[5.0],[2.4],[0.4],[- 1.6],[- 1.6]])
# EPA_Wildfire_ExtraVars.m:18
    monthIndex=single([])
# EPA_Wildfire_ExtraVars.m:20
    monthIndexLeap=single([])
# EPA_Wildfire_ExtraVars.m:21
    for month in arange(1,12).reshape(-1):
        monthIndex=vertcat(monthIndex,repmat(month,lmon(month),1))
# EPA_Wildfire_ExtraVars.m:23
        monthIndexLeap=vertcat(monthIndexLeap,repmat(month,lmonLeap(month),1))
# EPA_Wildfire_ExtraVars.m:24
    
    names.newyrs = copy(arange(2008,2099))
# EPA_Wildfire_ExtraVars.m:27
    num.newyrs = copy(length(names.newyrs))
# EPA_Wildfire_ExtraVars.m:28
    ##  Yearly Loop
    finalData=nan(num.ecoregions,3,num.newyrs,num.gcms,num.rcps,'single')
# EPA_Wildfire_ExtraVars.m:31
    load(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_pr']))
    RAWpr_all=copy(data)
# EPA_Wildfire_ExtraVars.m:34
    load(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_tasmax']))
    RAWtasmax_all=copy(data)
# EPA_Wildfire_ExtraVars.m:36
    load(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_relh']))
    RAWrelh_all=copy(data)
# EPA_Wildfire_ExtraVars.m:38
    clear('data')
    for gcm in arange(1,num.gcms).reshape(-1):
        for rcp in arange(1,num.rcps).reshape(-1):
            disp(concat(['Processing ... ',names.gcms[gcm],'_',names.rcps[rcp],'  |  ',num2str(toc / 60),' min']))
            for yr in arange(1,length(names.newyrs)).reshape(-1):
                # set initial values
                dmc_init=single(repmat(6.0,num.ecoregions,1))
# EPA_Wildfire_ExtraVars.m:49
                dc_init=single(repmat(15.0,num.ecoregions,1))
# EPA_Wildfire_ExtraVars.m:50
                RAWpr=squeeze(RAWpr_all(arange(),arange(),yr,gcm,rcp))
# EPA_Wildfire_ExtraVars.m:53
                RAWtasmax=squeeze(RAWtasmax_all(arange(),arange(),yr,gcm,rcp))
# EPA_Wildfire_ExtraVars.m:54
                RAWrelh=squeeze(RAWrelh_all(arange(),arange(),yr,gcm,rcp))
# EPA_Wildfire_ExtraVars.m:55
                if isleap(names.newyrs(yr)):
                    temporary.yrDays = copy(366)
# EPA_Wildfire_ExtraVars.m:59
                    temporary.monthIndex = copy(monthIndexLeap)
# EPA_Wildfire_ExtraVars.m:60
                else:
                    temporary.yrDays = copy(365)
# EPA_Wildfire_ExtraVars.m:62
                    temporary.monthIndex = copy(monthIndex)
# EPA_Wildfire_ExtraVars.m:63
                    RAWpr[arange(),end()]=[]
# EPA_Wildfire_ExtraVars.m:64
                    RAWtasmax[arange(),end()]=[]
# EPA_Wildfire_ExtraVars.m:65
                    RAWrelh[arange(),end()]=[]
# EPA_Wildfire_ExtraVars.m:66
                #preallocate the year data
                yrData=nan(num.ecoregions,3,temporary.yrDays,'single')
# EPA_Wildfire_ExtraVars.m:70
                for day in arange(1,temporary.yrDays).reshape(-1):
                    #get month index
                    mon=temporary.monthIndex(day)
# EPA_Wildfire_ExtraVars.m:76
                    temp=RAWtasmax(arange(),day)
# EPA_Wildfire_ExtraVars.m:78
                    rain=RAWpr(arange(),day)
# EPA_Wildfire_ExtraVars.m:80
                    rh=RAWrelh(arange(),day)
# EPA_Wildfire_ExtraVars.m:82
                    EPA_Wildfire_ExtraVars_DMCPart
                    EPA_Wildfire_ExtraVars_DCPart
                    EPA_Wildfire_ExtraVars_BUIPart
                    #save variables to output file
                    yrData[arange(),1,day]=bui
# EPA_Wildfire_ExtraVars.m:90
                    yrData[arange(),2,day]=dc
# EPA_Wildfire_ExtraVars.m:91
                    yrData[arange(),3,day]=dmc
# EPA_Wildfire_ExtraVars.m:92
                    dmc_init=copy(dmc)
# EPA_Wildfire_ExtraVars.m:95
                    dc_init=copy(dc)
# EPA_Wildfire_ExtraVars.m:95
                mask1=temporary.monthIndex > 4
# EPA_Wildfire_ExtraVars.m:99
                mask2=temporary.monthIndex < 11
# EPA_Wildfire_ExtraVars.m:100
                fireSeasonMask=logical_and(mask1,mask2)
# EPA_Wildfire_ExtraVars.m:101
                finalData[arange(),1,yr,gcm,rcp]=squeeze(mean(yrData(arange(),1,fireSeasonMask),3))
# EPA_Wildfire_ExtraVars.m:103
                finalData[arange(),2,yr,gcm,rcp]=squeeze(max(yrData(arange(),2,fireSeasonMask),[],3))
# EPA_Wildfire_ExtraVars.m:104
                finalData[arange(),3,yr,gcm,rcp]=squeeze(max(yrData(arange(),3,fireSeasonMask),[],3))
# EPA_Wildfire_ExtraVars.m:105
    
    #save output file
    clear('data','key')
    key.dims = copy(cellarray(['ecoregion','year']))
# EPA_Wildfire_ExtraVars.m:112
    key.years = copy(names.newyrs)
# EPA_Wildfire_ExtraVars.m:113
    key.ecoregions = copy(names.ecoregions)
# EPA_Wildfire_ExtraVars.m:114
    data=squeeze(finalData(arange(),1,arange(),arange(),arange()))
# EPA_Wildfire_ExtraVars.m:116
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion','_BUI']),'data','key')
    clear('data')
    data=squeeze(finalData(arange(),2,arange(),arange(),arange()))
# EPA_Wildfire_ExtraVars.m:121
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion','_DCmax']),'data','key')
    clear('data')
    data=squeeze(finalData(arange(),3,arange(),arange(),arange()))
# EPA_Wildfire_ExtraVars.m:126
    save(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion','_DMCmax']),'data','key')
    clear('data')