# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_Regs.m

    ## Run Regressions at Ecoregion Level
# Alisa White, March 4th 2018
    
    #Setup: Load key to create names
    load(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_AllVars']))
    clear('data')
    names.varsReg = copy(key.vars)
# EPA_Wildfire_Regs.m:8
    names.yrsReg = copy(key.years)
# EPA_Wildfire_Regs.m:9
    names.ecoReg = copy(key.ecoregions.T)
# EPA_Wildfire_Regs.m:10
    num.ecoReg = copy(length(names.ecoReg))
# EPA_Wildfire_Regs.m:11
    num.yrsReg = copy(length(names.yrsReg))
# EPA_Wildfire_Regs.m:12
    
    num.varsReg = copy(length(names.varsReg))
# EPA_Wildfire_Regs.m:13
    ## Regressions for Projections
# Reg 1: Pacific Northwest
# Regression 2: Nevada Mtns/semidesert 
# Regression 3: Eastern Rocky Mtns/Gr8 Plains
# Regression 4: California Coastal Shrub
# Regression 5: Desert Southwest 
# Regression 6: Rocky Mtn Forest
    
    #Loop over eco regions, gcms, rcps
#Output for area burned is in hectares
    
    regress=nan(num.ecoReg,num.yrsReg,num.gcms,num.rcps)
# EPA_Wildfire_Regs.m:27
    load(concat([home.outputs,'\MAT files\Derived Variables\Proj_Ecoregion_AllVars']))
    dataAll=copy(data)
# EPA_Wildfire_Regs.m:29
    for eco in arange(1,num.ecoReg).reshape(-1):
        for gcm in arange(1,num.gcms).reshape(-1):
            for rcp in arange(1,num.rcps).reshape(-1):
                data=squeeze(dataAll(arange(),arange(),gcm,rcp,arange()))
# EPA_Wildfire_Regs.m:34
                if 1 == eco:
                    first=dot(dot(3.4,10 ** 3.0),data(eco,arange(),9))
# EPA_Wildfire_Regs.m:38
                    second=dot(dot(2.9,10 ** 4.0),data(eco,arange(),2)) - dot(2.2,10 ** 6)
# EPA_Wildfire_Regs.m:39
                    regress[eco,arange(),gcm,rcp]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:40
                else:
                    if 2 == eco:
                        first=dot(dot(4.3,10 ** 4.0),data(eco,arange(),3))
# EPA_Wildfire_Regs.m:43
                        second=dot(dot(8.6,10 ** 4.0),data(eco,arange(),8))
# EPA_Wildfire_Regs.m:44
                        third=dot(dot(3.8,10 ** 5.0),data(eco,arange(),5)) - dot(4.2,10 ** 6)
# EPA_Wildfire_Regs.m:45
                        combine=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:46
                        regress[eco,arange(),gcm,rcp]=bsxfun(plus,combine,third)
# EPA_Wildfire_Regs.m:47
                    else:
                        if 3 == eco:
                            first=dot(dot(1.0,10 ** 3.0),data(eco,arange(),11))
# EPA_Wildfire_Regs.m:50
                            second=dot(dot(- 2.0,10 ** 4.0),data(eco,arange(),1)) + dot(1.0,10 ** 6)
# EPA_Wildfire_Regs.m:51
                            regress[eco,arange(),gcm,rcp]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:52
                        else:
                            if 4 == eco:
                                first=dot(dot(6.1,10 ** 3.0),data(eco,arange(),4))
# EPA_Wildfire_Regs.m:55
                                second=dot(dot(1.9,10 ** 2.0),data(eco,arange(),10)) - dot(6.5,10 ** 5)
# EPA_Wildfire_Regs.m:56
                                regress[eco,arange(),gcm,rcp]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:57
                            else:
                                if 5 == eco:
                                    first=dot(dot(4.1,10 ** 4.0),data(eco,arange(),6))
# EPA_Wildfire_Regs.m:60
                                    second=dot(dot(- 1.1,10 ** 4.0),data(eco,arange(),7)) - dot(7.7,10 ** 5)
# EPA_Wildfire_Regs.m:61
                                    regress[eco,arange(),gcm,rcp]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:62
                                else:
                                    #This is not from Yue et al. 2013, it is a linear
                    #regression we estimated from precipitation data
                                    first=multiply((multiply(- 9.36027,data(eco,arange(),12)) + 13.50438),(10 ** 5))
# EPA_Wildfire_Regs.m:67
                                    regress[eco,arange(),gcm,rcp]=first
# EPA_Wildfire_Regs.m:68
    
    regress[regress < 0]=0
# EPA_Wildfire_Regs.m:75
    
    data=copy(regress)
# EPA_Wildfire_Regs.m:76
    clear('key')
    key.dims = copy(cellarray(['ecoregion','year','gcms','rcps']))
# EPA_Wildfire_Regs.m:78
    key.ecoregions = copy(names.ecoReg)
# EPA_Wildfire_Regs.m:79
    key.years = copy(names.yrsReg)
# EPA_Wildfire_Regs.m:80
    key.gcms = copy(names.gcms)
# EPA_Wildfire_Regs.m:81
    key.rcps = copy(names.rcps)
# EPA_Wildfire_Regs.m:82
    key.units = copy('hectares')
# EPA_Wildfire_Regs.m:83
    save(concat([home.outputs,'\MAT files\Derived Variables\EcoregionRegs_DerivedProj']),'data','key')
    ## For Baseline
    
    load(concat([home.outputs,'\MAT files\Derived Variables\Base_Ecoregion_AllVars']))
    regress2=nan(num.ecoReg,num.baseEra)
# EPA_Wildfire_Regs.m:89
    #Export the baseline data as a table (for Meredith, 5/9/18)
    switches.print = copy(true)
# EPA_Wildfire_Regs.m:92
    if switches.print:
        names.ecoReg[2]='NevadaMtns'
# EPA_Wildfire_Regs.m:94
        names.ecoReg[3]='EasternRockiesGreatPlains'
# EPA_Wildfire_Regs.m:95
        for eco in arange(1,num.ecoReg).reshape(-1):
            input_=squeeze(data(eco,arange(),arange()))
# EPA_Wildfire_Regs.m:97
            xlsTable(concat([home.outputs,'\Data Files\RawBaselineVarsLOCA']),input_,names.ecoReg[eco],names.baseEra.T,names.newvars,cellarray(['Original Vars']),cellarray(['Vars']))
    
    #This is a test to substitute in Yue's humidity data for baseline
    switches.Yue = copy(false)
# EPA_Wildfire_Regs.m:104
    if switches.Yue:
        regress2=nan(num.ecoReg,num.baseEra - 1)
# EPA_Wildfire_Regs.m:106
        origvars=data(arange(),arange(1,19),arange())
# EPA_Wildfire_Regs.m:107
        #Yue's variables for relative humidity
        Yue=xlsread(concat([home.inputs,'\Data Files\Area Burned Calculations\Xus_Regression_Variables_ForProcessing.xlsx']),'Regression','B2:G151')
# EPA_Wildfire_Regs.m:109
        for eco in arange(1,num.ecoReg).reshape(-1):
            index=Yue(arange(),1) == eco
# EPA_Wildfire_Regs.m:111
            for var in arange(1,4).reshape(-1):
                values=Yue(index,var + 2)
# EPA_Wildfire_Regs.m:113
                values=values(arange(7,25),arange())
# EPA_Wildfire_Regs.m:114
                origvars[eco,arange(),var]=values
# EPA_Wildfire_Regs.m:115
                data=copy(origvars)
# EPA_Wildfire_Regs.m:116
    
    for eco in arange(1,num.ecoReg).reshape(-1):
        if 1 == eco:
            first=dot(dot(3.4,10 ** 3.0),data(eco,arange(),9))
# EPA_Wildfire_Regs.m:124
            second=dot(dot(2.9,10 ** 4.0),data(eco,arange(),2)) - dot(2.2,10 ** 6)
# EPA_Wildfire_Regs.m:125
            regress2[eco,arange()]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:126
        else:
            if 2 == eco:
                first=dot(dot(4.3,10 ** 4.0),data(eco,arange(),3))
# EPA_Wildfire_Regs.m:129
                second=dot(dot(8.6,10 ** 4.0),data(eco,arange(),8))
# EPA_Wildfire_Regs.m:130
                third=dot(dot(3.8,10 ** 5.0),data(eco,arange(),5)) - dot(4.2,10 ** 6)
# EPA_Wildfire_Regs.m:131
                combine=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:132
                regress2[eco,arange()]=bsxfun(plus,combine,third)
# EPA_Wildfire_Regs.m:133
            else:
                if 3 == eco:
                    first=dot(dot(1.0,10 ** 3.0),data(eco,arange(),11))
# EPA_Wildfire_Regs.m:136
                    second=dot(dot(- 2.0,10 ** 4.0),data(eco,arange(),1)) + dot(1.0,10 ** 6)
# EPA_Wildfire_Regs.m:137
                    regress2[eco,arange()]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:138
                else:
                    if 4 == eco:
                        first=dot(dot(6.1,10 ** 3.0),data(eco,arange(),4))
# EPA_Wildfire_Regs.m:141
                        second=dot(dot(1.9,10 ** 2.0),data(eco,arange(),10)) - dot(6.5,10 ** 5)
# EPA_Wildfire_Regs.m:142
                        regress2[eco,arange()]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:143
                    else:
                        if 5 == eco:
                            first=dot(dot(4.1,10 ** 4.0),data(eco,arange(),6))
# EPA_Wildfire_Regs.m:146
                            second=dot(dot(- 1.1,10 ** 4.0),data(eco,arange(),7)) - dot(7.7,10 ** 5)
# EPA_Wildfire_Regs.m:147
                            regress2[eco,arange()]=bsxfun(plus,first,second)
# EPA_Wildfire_Regs.m:148
                        else:
                            #This now includes Jackie's regression
                            first=multiply((multiply(- 9.36027,data(eco,arange(),12)) + 13.50438),(10 ** 5))
# EPA_Wildfire_Regs.m:152
                            regress2[eco,arange()]=first
# EPA_Wildfire_Regs.m:153
                            #ecoregion
           #regress2(regress2>1450000)=1450000;
    
    regress2[regress2 < 0]=0
# EPA_Wildfire_Regs.m:161
    
    data=copy(regress2)
# EPA_Wildfire_Regs.m:163
    clear('key')
    key.dims = copy(cellarray(['ecoregion','year']))
# EPA_Wildfire_Regs.m:165
    key.ecoregions = copy(names.ecoReg)
# EPA_Wildfire_Regs.m:166
    key.years = copy(names.baseEra)
# EPA_Wildfire_Regs.m:167
    key.units = copy('hectares')
# EPA_Wildfire_Regs.m:168
    switches.Yue = copy(true)
# EPA_Wildfire_Regs.m:170
    if switches.Yue:
        save(concat([home.outputs,'\MAT files\EcoregionRegs_BaselineYueHumidity']),'data','key')
    
    save(concat([home.outputs,'\MAT files\Derived Variables\EcoregionRegs_DerivedBase']),'data','key')
    ## Analyze Negative Regression Values
    
    switches.negreg = copy(false)
# EPA_Wildfire_Regs.m:179
    if switches.negreg:
        load(concat([home.outputs,'\MAT files\Derived Variables\EcoregionRegs_ProjUpdated']))
        names.yrstest = copy(arange(2008,2017))
# EPA_Wildfire_Regs.m:184
        eastrock=squeeze(data(3,arange(1,10),arange(),arange()))
# EPA_Wildfire_Regs.m:188
        rock=squeeze(data(6,arange(1,10),arange(),arange()))
# EPA_Wildfire_Regs.m:189
        for rcp in arange(1,num.rcps).reshape(-1):
            xlsTable(concat([home.outputs,'\Data Files\Wildfires\QCDMCmaxEco3']),eastrock(arange(),arange(),rcp),names.rcps[rcp],names.yrstest.T,names.gcms,cellarray(['Area Burned']),cellarray(['Hectares']))
        #For Rocky Mtns
        for rcp in arange(1,num.rcps).reshape(-1):
            xlsTable(concat([home.outputs,'\Data Files\Wildfires\QCDMCmaxEco6']),rock(arange(),arange(),rcp),names.rcps[rcp],names.yrstest.T,names.gcms,cellarray(['Area Burned']),cellarray(['Hectares']))
    
    ## Analyze Maximum Rocky Mountain Forest Values
    
    switches.rock = copy(false)
# EPA_Wildfire_Regs.m:207
    if switches.rock:
        data=load(concat([home.outputs,'\MAT files\Derived Variables\EcoregionRegs_DerivedProj']))
# EPA_Wildfire_Regs.m:210
        key.data = copy(data.key)
# EPA_Wildfire_Regs.m:211
        data=data.data
# EPA_Wildfire_Regs.m:212
        data85rock=squeeze(data(6,arange(),arange(),2))
# EPA_Wildfire_Regs.m:214
        yrs=key.data.years.T
# EPA_Wildfire_Regs.m:216
        xlsTable(concat([home.outputs,'\Data Files\QC\AreaBurnedRockMtn_UpdateLinear']),data85rock,names.rcps[2],names.yrsReg.T,names.gcms,cellarray(['Area Burned']),cellarray(['Hectares']))
    