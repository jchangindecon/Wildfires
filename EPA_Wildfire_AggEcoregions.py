# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_AggEcoregions.m

    ## Pr and Tasmax
    tic
    crosswalk=copy(LOCA_USHCNcrosswalk)
# EPA_Wildfire_AggEcoregions.m:3
    switches.base = copy(true)
# EPA_Wildfire_AggEcoregions.m:4
    switches.proj = copy(true)
# EPA_Wildfire_AggEcoregions.m:5
    for var in arange(1,2).reshape(-1):
        ## Step 1. Baseline
        if switches.base:
            #Preallocate
            annual=nan(num.ecoregions,num.days + 1,num.baseYrs,'single')
# EPA_Wildfire_AggEcoregions.m:13
            monthly=nan(num.ecoregions,num.mo,num.baseYrs,'single')
# EPA_Wildfire_AggEcoregions.m:14
            #consolidate to ecoregions here
            for yr in arange(1,num.baseYrs).reshape(-1):
                disp(concat(['Processing ',names.vars[var],'  |  Baseline  ',num2str(names.baseYrs(yr)),'  |  ',num2str(toc / 60),' min']))
                if isleap(names.baseYrs(yr)):
                    load(concat([home.base,'\',names.vars[var],'\LOCA_ObsBaselineClip_',names.vars[var],'_',num2str(names.baseYrs(yr)),'_leap']))
                else:
                    load(concat([home.base,'\',names.vars[var],'\LOCA_ObsBaselineClip_',names.vars[var],'_',num2str(names.baseYrs(yr))]))
                data2=reshape(permute(data,concat([2,1,3])),[],size(data,3))
# EPA_Wildfire_AggEcoregions.m:30
                for ecoregion in arange(1,num.ecoregions).reshape(-1):
                    match=crosswalk(arange(),2) == ecoregion
# EPA_Wildfire_AggEcoregions.m:32
                    rows=crosswalk(match,1)
# EPA_Wildfire_AggEcoregions.m:33
                    annual[ecoregion,arange(1,size(data2,2)),yr]=nanmean(data2(rows,arange()),1)
# EPA_Wildfire_AggEcoregions.m:34
            #save
            clear('key')
            key.dims = copy(cellarray(['ecoregion','day','year']))
# EPA_Wildfire_AggEcoregions.m:40
            key.years = copy(names.baseYrs)
# EPA_Wildfire_AggEcoregions.m:41
            key.ecoregions = copy(names.ecoregions)
# EPA_Wildfire_AggEcoregions.m:42
            key.network = copy('USHCN')
# EPA_Wildfire_AggEcoregions.m:43
            data=single(annual)
# EPA_Wildfire_AggEcoregions.m:44
            save(concat([home.outputs,'\MAT files\Raw Variables\Base_Ecoregion_',names.vars[var]]),'data','key')
            for yr in arange(1,num.baseYrs).reshape(-1):
                dayTrack=1
# EPA_Wildfire_AggEcoregions.m:50
                for mo in arange(1,num.mo).reshape(-1):
                    if isleap(names.baseYrs(yr)):
                        dayJump=num.modaysLeap(mo)
# EPA_Wildfire_AggEcoregions.m:53
                    else:
                        dayJump=num.modays(mo)
# EPA_Wildfire_AggEcoregions.m:55
                    monthly[arange(),mo,yr]=mean(annual(arange(),arange(dayTrack,dayTrack + dayJump - 1),yr),2)
# EPA_Wildfire_AggEcoregions.m:58
                    dayTrack=dayTrack + dayJump
# EPA_Wildfire_AggEcoregions.m:59
            #save
            clear('key')
            key.dims = copy(cellarray(['ecoregion','month','year']))
# EPA_Wildfire_AggEcoregions.m:66
            key.years = copy(names.baseYrs)
# EPA_Wildfire_AggEcoregions.m:67
            key.ecoregions = copy(names.ecoregions)
# EPA_Wildfire_AggEcoregions.m:68
            key.network = copy('USHCN')
# EPA_Wildfire_AggEcoregions.m:69
            data=single(monthly)
# EPA_Wildfire_AggEcoregions.m:70
            save(concat([home.outputs,'\MAT files\Raw Variables\Base_Ecoregion_',names.vars[var],'_Monthly']),'data','key')
        ##  Step 2. projections
        if switches.proj:
            annual=nan(num.ecoregions,num.days + 1,num.projYrs,num.gcms,num.rcps,'single')
# EPA_Wildfire_AggEcoregions.m:77
            monthly=nan(num.ecoregions,num.mo,num.projYrs,num.gcms,num.rcps,'single')
# EPA_Wildfire_AggEcoregions.m:78
            for gcm in arange(1,num.gcms).reshape(-1):
                for rcp in arange(1,num.rcps).reshape(-1):
                    ## Annual
                    for yr in arange(1,num.projYrs).reshape(-1):
                        disp(concat(['Processing ',names.vars[var],'  |  ',num2str(names.projYrs(yr)),' ',names.gcms[gcm],' ',names.rcps[rcp],'  |  ',num2str(toc / 60),' min']))
                        if isleap(names.projYrs(yr)):
                            load(concat([home.proj,'\',names.gcms[gcm],'\',names.rcps[rcp],'\',names.vars[var],'\LOCA_projClip_',names.gcms[gcm],'_',names.rcps[rcp],'_',num2str(names.projYrs(yr)),'_',names.vars[var],'_leap']))
                        else:
                            load(concat([home.proj,'\',names.gcms[gcm],'\',names.rcps[rcp],'\',names.vars[var],'\LOCA_projClip_',names.gcms[gcm],'_',names.rcps[rcp],'_',num2str(names.projYrs(yr)),'_',names.vars[var]]))
                        #consolidate to ecoregions here
                        data2=reshape(permute(data,concat([2,1,3])),[],size(data,3))
# EPA_Wildfire_AggEcoregions.m:100
                        for ecoregion in arange(1,num.ecoregions).reshape(-1):
                            match=crosswalk(arange(),2) == ecoregion
# EPA_Wildfire_AggEcoregions.m:102
                            rows=crosswalk(match,1)
# EPA_Wildfire_AggEcoregions.m:103
                            annual[ecoregion,arange(1,size(data2,2)),yr,gcm,rcp]=nanmean(data2(rows,arange()),1)
# EPA_Wildfire_AggEcoregions.m:104
                    ## Monthly
                    for yr in arange(1,num.projYrs).reshape(-1):
                        dayTrack=1
# EPA_Wildfire_AggEcoregions.m:112
                        for mo in arange(1,num.mo).reshape(-1):
                            if isleap(names.projYrs(yr)):
                                dayJump=num.modaysLeap(mo)
# EPA_Wildfire_AggEcoregions.m:115
                            else:
                                dayJump=num.modays(mo)
# EPA_Wildfire_AggEcoregions.m:117
                            monthly[arange(),mo,yr,gcm,rcp]=mean(annual(arange(),arange(dayTrack,dayTrack + dayJump - 1),yr,gcm,rcp),2)
# EPA_Wildfire_AggEcoregions.m:120
                            dayTrack=dayTrack + dayJump
# EPA_Wildfire_AggEcoregions.m:121
            #save
            clear('key')
            key.dims = copy(cellarray(['ecoregion','month','year']))
# EPA_Wildfire_AggEcoregions.m:129
            key.years = copy(names.projYrs)
# EPA_Wildfire_AggEcoregions.m:130
            key.crus = copy(names.ecoregions)
# EPA_Wildfire_AggEcoregions.m:131
            key.network = copy('USHCN')
# EPA_Wildfire_AggEcoregions.m:132
            data=single(annual)
# EPA_Wildfire_AggEcoregions.m:134
            save(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_',names.vars[var]]),'data','key')
            clear('key')
            key.dims = copy(cellarray(['ecoregion','month','year']))
# EPA_Wildfire_AggEcoregions.m:140
            key.years = copy(names.projYrs)
# EPA_Wildfire_AggEcoregions.m:141
            key.crus = copy(names.ecoregions)
# EPA_Wildfire_AggEcoregions.m:142
            key.network = copy('USHCN')
# EPA_Wildfire_AggEcoregions.m:143
            data=single(monthly)
# EPA_Wildfire_AggEcoregions.m:145
            save(concat([home.outputs,'\MAT files\Raw Variables\Proj_Ecoregion_',names.vars[var],'_Monthly']),'data','key')
    