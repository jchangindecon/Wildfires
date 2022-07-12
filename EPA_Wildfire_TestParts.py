# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_TestParts.m

    ## Testing the Parts for the Last Three Variables:
    
    ## Setup
    clear('fullMask','locaMask')
    # create arrays that store month-specific values
    lmon=concat([[31],[28],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]])
# EPA_Wildfire_TestParts.m:7
    lmonLeap=concat([[31],[29],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]])
# EPA_Wildfire_TestParts.m:8
    el=concat([[6.5],[7.5],[9.0],[12.8],[13.9],[13.9],[12.4],[10.9],[9.4],[8.0],[7.0],[6.0]])
# EPA_Wildfire_TestParts.m:9
    fl=concat([[- 1.6],[- 1.6],[- 1.6],[0.9],[3.8],[5.8],[6.4],[5.0],[2.4],[0.4],[- 1.6],[- 1.6]])
# EPA_Wildfire_TestParts.m:10
    monthIndex=single([])
# EPA_Wildfire_TestParts.m:12
    monthIndexLeap=single([])
# EPA_Wildfire_TestParts.m:13
    for month in arange(1,12).reshape(-1):
        monthIndex=vertcat(monthIndex,repmat(month,lmon(month),1))
# EPA_Wildfire_TestParts.m:15
        monthIndexLeap=vertcat(monthIndexLeap,repmat(month,lmonLeap(month),1))
# EPA_Wildfire_TestParts.m:16
    
    ## Get Data
    yr=1
# EPA_Wildfire_TestParts.m:20
    #load tasmax and pr and set some temporary values
    if isleap(names.baseEra(yr)):
        temporary.yrDays = copy(366)
# EPA_Wildfire_TestParts.m:23
        temporary.monthIndex = copy(monthIndexLeap)
# EPA_Wildfire_TestParts.m:24
        load(concat([home.base,'\pr\LOCA_ObsBaselineClip_pr_',num2str(names.baseYrs(yr)),'_leap']))
        RAWpr=copy(data)
# EPA_Wildfire_TestParts.m:26
        load(concat([home.base,'\tasmax\LOCA_ObsBaselineClip_tasmax_',num2str(names.baseYrs(yr)),'_leap']))
        RAWtasmax=copy(data)
# EPA_Wildfire_TestParts.m:28
        clear('data')
    else:
        temporary.yrDays = copy(365)
# EPA_Wildfire_TestParts.m:31
        temporary.monthIndex = copy(monthIndex)
# EPA_Wildfire_TestParts.m:32
        load(concat([home.base,'\pr\LOCA_ObsBaselineClip_pr_',num2str(names.baseYrs(yr))]))
        RAWpr=copy(data)
# EPA_Wildfire_TestParts.m:34
        load(concat([home.base,'\tasmax\LOCA_ObsBaselineClip_tasmax_',num2str(names.baseYrs(yr))]))
        RAWtasmax=copy(data)
# EPA_Wildfire_TestParts.m:36
        clear('data')
    
    #pull relative humidity and turn into a mat
    load(concat(['\\clusterfs\CLM-Data\HAWQS Project 10.2017\Outputs\NewVars_cru\Final ','Files\USproj_LOCA_Base_relh']))
    relhYr=nan(67420,366)
# EPA_Wildfire_TestParts.m:43
    relhYr[names.crus,arange()]=data(arange(),arange(),find(names.baseYrs == names.baseEra(yr)))
# EPA_Wildfire_TestParts.m:44
    relhYr=cru2mat(relhYr)
# EPA_Wildfire_TestParts.m:45
    if logical_not(isleap(names.baseEra(yr))):
        relhYr[arange(),arange(),60]=[]
# EPA_Wildfire_TestParts.m:47
    
    clear('data')
    #preallocate the year data
    yrData_Scalar=nan(num.lats,num.lons,3,temporary.yrDays,'single')
# EPA_Wildfire_TestParts.m:52
    yrData_Matrix=nan(num.lats,num.lons,3,temporary.yrDays,'single')
# EPA_Wildfire_TestParts.m:53
    ## Run Matrix Scripts
# set initial values
    dmc_old=single(repmat(6.0,num.lats,num.lons))
# EPA_Wildfire_TestParts.m:58
    dc_old=single(repmat(15.0,num.lats,num.lons))
# EPA_Wildfire_TestParts.m:59
    tic
    for day in arange(1,temporary.yrDays).reshape(-1):
        disp(concat(['Processing ... Matrix Day ',num2str(day),'  |  ',num2str(toc / 60),' min']))
        mon=temporary.monthIndex(day)
# EPA_Wildfire_TestParts.m:66
        temp=RAWtasmax(arange(),arange(),day)
# EPA_Wildfire_TestParts.m:68
        rain=RAWpr(arange(),arange(),day)
# EPA_Wildfire_TestParts.m:70
        rh=pixelate(relhYr(arange(),arange(),day),8,8)
# EPA_Wildfire_TestParts.m:72
        rh=rh(arange(top,bottom),arange(left,right))
# EPA_Wildfire_TestParts.m:73
        CIRA3_Wildfire_ExtraVars_DMCPart
        CIRA3_Wildfire_ExtraVars_DCPart
        CIRA3_Wildfire_ExtraVars_BUIPart
        #save variables to output file
        yrData_Matrix[arange(),arange(),1,day]=bui
# EPA_Wildfire_TestParts.m:81
        yrData_Matrix[arange(),arange(),2,day]=dc
# EPA_Wildfire_TestParts.m:82
        yrData_Matrix[arange(),arange(),3,day]=dmc
# EPA_Wildfire_TestParts.m:83
        dmc_old=copy(dmc)
# EPA_Wildfire_TestParts.m:86
        dc_old=copy(dc)
# EPA_Wildfire_TestParts.m:86
    
    ## Run Scalar Scripts
# set initial values
    dmc_old=6.0
# EPA_Wildfire_TestParts.m:92
    dc_old=15.0
# EPA_Wildfire_TestParts.m:93
    tic
    for day in arange(1,temporary.yrDays).reshape(-1):
        disp(concat(['Processing ... Scalar Day ',num2str(day),'  |  ',num2str(toc / 60),' min']))
        mon=temporary.monthIndex(day)
# EPA_Wildfire_TestParts.m:101
        temp=RAWtasmax(arange(),arange(),day)
# EPA_Wildfire_TestParts.m:103
        rain=RAWpr(arange(),arange(),day)
# EPA_Wildfire_TestParts.m:105
        rh=pixelate(relhYr(arange(),arange(),day),8,8)
# EPA_Wildfire_TestParts.m:107
        rh=rh(arange(top,bottom),arange(left,right))
# EPA_Wildfire_TestParts.m:108
        for lat in arange(1,size(LOCAlats)).reshape(-1):
            for lon in arange(1,size(LOCAlons)).reshape(-1):
                if isnan(temp(lat,lon)):
                    continue
                ## DMC Part
                t=max(- 1.1,temp(lat,lon))
# EPA_Wildfire_TestParts.m:118
                rk=dot(dot(multiply(dot(1.894,(t + 1.1)),(100.0 - rh(lat,lon))),el(mon)),0.0001)
# EPA_Wildfire_TestParts.m:119
                if rain(lat,lon) <= 1.5:
                    pr=copy(dmc_old)
# EPA_Wildfire_TestParts.m:122
                else:
                    ra=rain(lat,lon)
# EPA_Wildfire_TestParts.m:124
                    rw=dot(0.92,ra) - 1.27
# EPA_Wildfire_TestParts.m:125
                    wmi=20.0 + 280.0 / exp(dot(0.023,dmc_old))
# EPA_Wildfire_TestParts.m:126
                    if dmc_old <= 33:
                        b=100.0 / (0.5 + dot(0.3,dmc_old))
# EPA_Wildfire_TestParts.m:129
                    else:
                        if dmc_old <= 65:
                            b=14.0 - dot(1.3,log(dmc_old))
# EPA_Wildfire_TestParts.m:131
                        else:
                            b=dot(6.2,log(dmc_old)) - 17.2
# EPA_Wildfire_TestParts.m:133
                    wmr=wmi + dot(1000.0,rw) / (48.77 + dot(b,rw))
# EPA_Wildfire_TestParts.m:136
                    pr=dot(43.43,(5.6348 - log(wmr - 20)))
# EPA_Wildfire_TestParts.m:137
                if pr < 0:
                    pr=0
# EPA_Wildfire_TestParts.m:140
                dmc=pr + rk
# EPA_Wildfire_TestParts.m:142
                if dmc < 0:
                    dmc=0
# EPA_Wildfire_TestParts.m:144
                ## DC Part
                if temp(lat,lon) < - 2.8:
                    t=- 2.8
# EPA_Wildfire_TestParts.m:150
                pe=(dot(0.36,(t + 2.8)) + fl(mon)) / 2.0
# EPA_Wildfire_TestParts.m:152
                if pe < 0.0:
                    pe=0.0
# EPA_Wildfire_TestParts.m:154
                if rain(lat,lon) <= 2.8:
                    dr=copy(dc_old)
# EPA_Wildfire_TestParts.m:157
                else:
                    ra=rain(lat,lon)
# EPA_Wildfire_TestParts.m:159
                    rw=dot(0.83,ra) - 1.27
# EPA_Wildfire_TestParts.m:160
                    smi=dot(800,exp(- dc_old / 400))
# EPA_Wildfire_TestParts.m:161
                    dr=dc_old - dot(400.0,log(1.0 + dot(3.937,rw) / smi))
# EPA_Wildfire_TestParts.m:162
                    if (dr < 0):
                        dr=0
# EPA_Wildfire_TestParts.m:164
                dc=dr + pe
# EPA_Wildfire_TestParts.m:167
                if (dc < 0):
                    dc=0
# EPA_Wildfire_TestParts.m:169
                ## BUI Part
                if (abs(dmc) + abs(dc)) == 0:
                    bui=0
# EPA_Wildfire_TestParts.m:175
                else:
                    bui=dot(dot(0.8,dc),dmc) / (dmc + dot(0.4,dc))
# EPA_Wildfire_TestParts.m:177
                if bui < dmc:
                    p=(dmc - bui) / dmc
# EPA_Wildfire_TestParts.m:181
                    cc=0.92 + ((dot(0.0114,dmc)) ** 1.7)
# EPA_Wildfire_TestParts.m:182
                    bui=dmc - dot(cc,p)
# EPA_Wildfire_TestParts.m:183
                    if (bui < 0):
                        bui=0
# EPA_Wildfire_TestParts.m:185
                ## Fill In
                yrData_Scalar[lat,lon,1,day]=bui
# EPA_Wildfire_TestParts.m:190
                yrData_Scalar[lat,lon,2,day]=dc
# EPA_Wildfire_TestParts.m:191
                yrData_Scalar[lat,lon,3,day]=dmc
# EPA_Wildfire_TestParts.m:192
    
    ## Do they match?
    