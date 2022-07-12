# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_Fuelbed_testing.m

    ## Wildfires Analyze Fuelbed Load 
# Alisa White, 5/7/2018
    
    addpath(genpath('L:\01 Data\src'))
    #homes
    home.inputs = copy('L:\02 Projects\EPA Wildfire\Inputs')
# EPA_Wildfire_Fuelbed_testing.m:7
    home.proj = copy('\\clusterfs\CLM-Data\CURRENT LOCA\Clipped LOCA2')
# EPA_Wildfire_Fuelbed_testing.m:8
    home.base = copy('\\clusterfs\CLM-Data\CURRENT LOCA\Clipped LOCA2\Observed Baseline')
# EPA_Wildfire_Fuelbed_testing.m:9
    home.graphics = copy('L:\02 Projects\EPA Wildfire\Outputs\Graphics')
# EPA_Wildfire_Fuelbed_testing.m:10
    home.outputs = copy('L:\02 Projects\EPA Wildfire\Outputs')
# EPA_Wildfire_Fuelbed_testing.m:11
    home.cluster = copy('\\clusterfs\CLM-Data\CURRENT LOCA')
# EPA_Wildfire_Fuelbed_testing.m:12
    ##  Step 1: Processing Fuelbed Map
    
    # A note on reshape: reshape works column wise, so in order to make it read
# in a vertical (1 column list) of IDs into a 2D matrix, you need to
# reshape as follows (including the transpose '):
# B=reshape(A,[# columns , # rows])';
    
    #First, use flipud to flip the lookup matrix, which reads from bottom left
#originally
    
    #1A: Pull in Fuelbed values and reshape into list
    lookup=flipud(xlsread(concat([home.inputs,'\Data Files\Fuelbeds\Fuelbed Map.xlsx']),'Fuelbed Values','B2:FVB2932'))
# EPA_Wildfire_Fuelbed_testing.m:25
    names.rowsF = copy(arange(1,length(lookup(arange(),1))))
# EPA_Wildfire_Fuelbed_testing.m:26
    names.colsF = copy(arange(1,length(lookup(1,arange()))))
# EPA_Wildfire_Fuelbed_testing.m:27
    num.rowsF = copy(length(names.rowsF))
# EPA_Wildfire_Fuelbed_testing.m:28
    num.colsF = copy(length(names.colsF))
# EPA_Wildfire_Fuelbed_testing.m:29
    fuelbedIDs=(arange(1,dot(num.rowsF,num.colsF))).T
# EPA_Wildfire_Fuelbed_testing.m:30
    #1B: The reshape & concatenate with IDs
    lookuplist=reshape(lookup.T,[],1)
# EPA_Wildfire_Fuelbed_testing.m:33
    lookupfuel=cat(2,fuelbedIDs,lookuplist)
# EPA_Wildfire_Fuelbed_testing.m:34
    clear('lookuplist','fuelbedIDs','lookup')
    #1C: Pull in Organic Matter/Fuel types lookup chart in
    fueltype=xlsread(concat([home.inputs,'\Data Files\Fuelbeds\Fuelbed Map.xlsx']),'Fuelbed MATLAB','A2:H504')
# EPA_Wildfire_Fuelbed_testing.m:39
    __,txt=xlsread(concat([home.inputs,'\Data Files\Fuelbeds\Fuelbed Map.xlsx']),'Fuelbed MATLAB','A1:H1',nargout=2)
# EPA_Wildfire_Fuelbed_testing.m:40
    #lookupIDs=xlsread([home.inputs '\Fuelbeds\Fuelbed Map.xlsx'],'Fuelbed Lookup 2','A3:H505');
    names.fuels = copy(txt(arange(),arange(2,8)))
# EPA_Wildfire_Fuelbed_testing.m:42
    clear('txt')
    num.fuels = copy(length(names.fuels))
# EPA_Wildfire_Fuelbed_testing.m:44
    #1D: Add to the lookupfuel matrix with each fuel type
    fuelfinal=nan(dot(num.rowsF,num.colsF),num.fuels)
# EPA_Wildfire_Fuelbed_testing.m:47
    for ID in arange(1,dot(num.rowsF,num.colsF)).reshape(-1):
        index=lookupfuel(ID,2) == fueltype(arange(),1)
# EPA_Wildfire_Fuelbed_testing.m:49
        fuels=fueltype(index,arange(2,8))
# EPA_Wildfire_Fuelbed_testing.m:50
        fuelfinal[ID,arange()]=fuels
# EPA_Wildfire_Fuelbed_testing.m:51
    
    ## Step 2: Weighting Fuel to CRU Grid Level
    
    #2A:Pull in Grid Codes for 1/2 Degree Grid in Area of Interest
    grid=xlsread(concat([home.inputs,'\Data Files\Grid Definitions\LookupTables\HalfDegree_NoNA_Table.xlsx']),'HalfDegree_NoNA_Table','A2:A1587')
# EPA_Wildfire_Fuelbed_testing.m:57
    #2B:Pull in Fractional Fuel Consumption as a Function of Fire Severity
    fracfuel=xlsread(concat([home.inputs,'\Data Files\Fuelbeds\Fractional Fuel Consumption.xlsx']),'Sheet1','B2:D8')
# EPA_Wildfire_Fuelbed_testing.m:61
    #2C:Pull in Weights File for each ecosystem
    names.ecosystems = copy(cellarray(['242','m242','m261','341','m341','342','331','315','262','m262','261','322','321','m313','313','m331','m332','m333']))
# EPA_Wildfire_Fuelbed_testing.m:65
    num.ecosystems = copy(length(names.ecosystems))
# EPA_Wildfire_Fuelbed_testing.m:67
    #To check if any CRUs with 0 load later
    weightcheck=nan(num.ecosystems,2)
# EPA_Wildfire_Fuelbed_testing.m:70
    tic
    for ecos in arange(1,num.ecosystems).reshape(-1):
        disp(concat(['Running ',names.ecosystems[ecos],'  |  ',num2str(toc / 60),' min']))
        #ecosystem 7 is too large to run through extract var cru in one piece
        if ecos == 7:
            #Part 1
            weights=xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'_1.xlsx']),'weights')
# EPA_Wildfire_Fuelbed_testing.m:80
            names.fuelecos = copy(xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'_1.xlsx']),'Fuelbed_IDs','A:A'))
# EPA_Wildfire_Fuelbed_testing.m:82
            names.CRU = copy(xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'_1.xlsx']),'CRU_IDs','A:A'))
# EPA_Wildfire_Fuelbed_testing.m:84
            weights2=xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'_2.xlsx']),'weights')
# EPA_Wildfire_Fuelbed_testing.m:88
            names.fuelecos2 = copy(xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'_2.xlsx']),'Fuelbed_IDs','A:A'))
# EPA_Wildfire_Fuelbed_testing.m:90
            names.CRU2 = copy(xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'_2.xlsx']),'CRU_IDs','A:A'))
# EPA_Wildfire_Fuelbed_testing.m:92
            namesfuelecos2=names.fuelecos2 + 1
# EPA_Wildfire_Fuelbed_testing.m:96
            namesfuelecos=names.fuelecos + 1
# EPA_Wildfire_Fuelbed_testing.m:97
            reduce2,order2=ismember(lookupfuel(arange(),1),namesfuelecos2,nargout=2)
# EPA_Wildfire_Fuelbed_testing.m:99
            dataReduce2=fuelfinal(reduce2,arange())
# EPA_Wildfire_Fuelbed_testing.m:102
            orderReduce2=order2(reduce2)
# EPA_Wildfire_Fuelbed_testing.m:103
            dataReduceOrder2=dataReduce2(orderReduce2,arange())
# EPA_Wildfire_Fuelbed_testing.m:106
            #the fuelbeds that fall in that ecosystem
            originalList2=lookupfuel(arange(),1)
# EPA_Wildfire_Fuelbed_testing.m:110
            originalListReduce2=originalList2(reduce2)
# EPA_Wildfire_Fuelbed_testing.m:111
            originalListReduceOrder2=originalListReduce2(orderReduce2)
# EPA_Wildfire_Fuelbed_testing.m:112
            sums(originalListReduceOrder2 != namesfuelecos2)
            clear('dataReduce2','orderReduce2','originalList2','originalListReduce2','originalListReduceOrder2')
            clear('reduce2','order2')
            #Spatial Weighting from Fuelbed to 1/2 Degree
        #Dimensions should be a number of CRUs x 7 fuel types
            dataByCRU2=extract_var_CRU(dataReduceOrder2,weights2)
# EPA_Wildfire_Fuelbed_testing.m:119
        else:
            #Important Inputs
            weights=xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'.xlsx']),'weights')
# EPA_Wildfire_Fuelbed_testing.m:124
            names.fuelecos = copy(xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'.xlsx']),'Fuelbed_IDs','A:A'))
# EPA_Wildfire_Fuelbed_testing.m:126
            names.CRU = copy(xlsread(concat([home.inputs,'\Data Files\Grid Definitions\Weights\Ecosyst_',names.ecosystems[ecos],'.xlsx']),'CRU_IDs','A:A'))
# EPA_Wildfire_Fuelbed_testing.m:128
            namesfuelecos=names.fuelecos + 1
# EPA_Wildfire_Fuelbed_testing.m:132
        reduce,order=ismember(lookupfuel(arange(),1),namesfuelecos,nargout=2)
# EPA_Wildfire_Fuelbed_testing.m:136
        dataReduce=fuelfinal(reduce,arange())
# EPA_Wildfire_Fuelbed_testing.m:139
        orderReduce=order(reduce)
# EPA_Wildfire_Fuelbed_testing.m:140
        dataReduceOrder=dataReduce(orderReduce,arange())
# EPA_Wildfire_Fuelbed_testing.m:143
        originalList=lookupfuel(arange(),1)
# EPA_Wildfire_Fuelbed_testing.m:146
        originalListReduce=originalList(reduce)
# EPA_Wildfire_Fuelbed_testing.m:147
        originalListReduceOrder=originalListReduce(orderReduce)
# EPA_Wildfire_Fuelbed_testing.m:148
        sums(originalListReduceOrder != namesfuelecos)
        clear('dataReduce','orderReduce','originalList','originalListReduce','originalListReduceOrder')
        clear('reduce','order')
        #Spatial Weighting from Fuelbed to 1/2 Degree
    #Dimensions should be a number of CRUs x 7 fuel types
        dataByCRU=extract_var_CRU(dataReduceOrder,weights)
# EPA_Wildfire_Fuelbed_testing.m:155
        #Create box plots to check on fuel ranges for each fuel type over all
    #CRUS in ecosystem
        if ecos == 7:
            boxPlot(dataByCRU2,0)
            title(concat([names.ecosystems[ecos],' Ecosystem- Fuelbed Heterogeneity at CRU level (tons/km^2)']))
            set(gca,'xtick',concat([arange(1,7,1)]),'xticklabel',cellarray(['Light','Medium','Heavy','Duff','Grass','Shrub','Canopy']))
            print_('-djpeg','-r300',concat([home.graphics,'\Fuelbed QC\FuelTypesByCRUpart2_',names.ecosystems[ecos]]))
            close_
            boxPlot(dataByCRU,0)
            title(concat([names.ecosystems[ecos],' Ecosystem- Fuelbed Heterogeneity at CRU level (tons/km^2)']))
            set(gca,'xtick',concat([arange(1,7,1)]),'xticklabel',cellarray(['Light','Medium','Heavy','Duff','Grass','Shrub','Canopy']))
            print_('-djpeg','-r300',concat([home.graphics,'\Fuelbed QC\FuelTypesByCRUpart1_',names.ecosystems[ecos]]))
            close_
        else:
            boxPlot(dataByCRU,0)
            title(concat([names.ecosystems[ecos],' Ecosystem- Fuelbed Heterogeneity at CRU level (tons/km^2)']))
            set(gca,'xtick',concat([arange(1,7,1)]),'xticklabel',cellarray(['Light','Medium','Heavy','Duff','Grass','Shrub','Canopy']))
            print_('-djpeg','-r300',concat([home.graphics,'\Fuelbed QC\FuelTypesByCRU_',names.ecosystems[ecos]]))
            close_
        if ecos == 7:
            dataByCRU=cat(1,dataByCRU,dataByCRU2)
# EPA_Wildfire_Fuelbed_testing.m:181
            names.CRU = copy(cat(1,names.CRU,names.CRU2))
# EPA_Wildfire_Fuelbed_testing.m:182
        #1. Multiply 7 fuels by 7x3 matrix by 25# for each fire intensity (low, med, high)
    #2. Then multiply by dataByCRU for 7 fuel types
    #3. Multiply by 907.185 to convert from tons to kgs
    #4. Then sum across all fuel types to get total fuel load and 
    # See Questions for Xu Yue Questions for more explanation - OC & BC are
    # mulitplied in during Step 3 but set up is here in total load 2 (make
    # 2 copies of total load)
        #Output tons/km2 for each fuel type for ecosystem
        datacat=horzcat(names.CRU,dot(dataByCRU,0.5))
# EPA_Wildfire_Fuelbed_testing.m:194
        xlswrite(concat([home.outputs,'\Emission Factor Revision\Fuel1_',names.ecosystems[ecos]]),datacat,'Fuel Tons per km2')
        totalload=dot(multiply(multiply(dot(dot(dataByCRU,fracfuel),0.25),907.185),0.01),0.5)
# EPA_Wildfire_Fuelbed_testing.m:197
        totalload=nansum(totalload,2)
# EPA_Wildfire_Fuelbed_testing.m:198
        totalload2=cat(2,totalload,totalload)
# EPA_Wildfire_Fuelbed_testing.m:199
        #xlsTable([home.outputs '\Data Files\QC\Fuelbed\FuelFinal_' names.ecosystems{ecos}],totalload2(:,1),'Fuel', ...
        #names.CRU,{'kg per ha'},{'kg/ha'},{'Fuelbed'});
        finaldatacat=horzcat(names.CRU,totalload2(arange(),1))
# EPA_Wildfire_Fuelbed_testing.m:204
        xlswrite(concat([home.outputs,'\Emission Factor Revision\FuelFinal1_',names.ecosystems[ecos]]),finaldatacat,'Fuel kg per ha')
        pause
        #calculate for
        if ecos == 2:
            totalloadtest=dataByCRU(10,arange())
# EPA_Wildfire_Fuelbed_testing.m:212
            totalloadmult=dot(totalloadtest,fracfuel)
# EPA_Wildfire_Fuelbed_testing.m:213
            totalloadmult2=multiply(multiply(multiply(totalloadmult,0.25),907.185),0.01)
# EPA_Wildfire_Fuelbed_testing.m:214
        #Check number of CRUs with no load
        weightcheck[ecos,1]=bsxfun(minus,numel(totalload2(arange(),1)),nnz(totalload2(arange(),1)))
# EPA_Wildfire_Fuelbed_testing.m:218
        weightcheck[ecos,2]=bsxfun(minus,numel(totalload2(arange(),2)),nnz(totalload2(arange(),2)))
# EPA_Wildfire_Fuelbed_testing.m:219
        data=copy(totalload2)
# EPA_Wildfire_Fuelbed_testing.m:221
        clear('key')
        key.dims = copy(cellarray(['IDs','type']))
# EPA_Wildfire_Fuelbed_testing.m:223
        key.IDs = copy(names.CRU)
# EPA_Wildfire_Fuelbed_testing.m:224
        key.type = copy(cellarray(['OC','BC']))
# EPA_Wildfire_Fuelbed_testing.m:225
        key.units = copy(cellarray(['kg matter']))
# EPA_Wildfire_Fuelbed_testing.m:226
        clear('data')
    
    clear('totalload','data','dataReduce','dataReduceOrder')
    ## Step 3: Multiply by Area Burned 
# Ecoregion 1: Pacific Northwest
# Ecoregion 2: Nevada Mtns/semidesert
# Ecoregion 3: Eastern Rocky Mtns/Gr8 Plains
# Ecoregion 4: California Coastal Shrub
# Ecoregion 5: Desert Southwest
# Ecoregion 6: Rocky Mtn Forest
    
    #Step 3A: Projection from 2008 to 2099
    
    #1.  Eliminate eco system loop
#2. For each eco region, concatenate grid30 and grd70 & concat burned30 and
#burned70
#3. sort based on the grid ids - both ids and data!!
#4. pull in all ecosystem files & concat grids and fuel data similar to above
#5. also sort based on grid ids - like above
#6. write loop over cru list and multiply area burned by fuel
    
    #This is to check the annual mean biomass consumption from 2051-2065
    Check2050Bio=nan(num.ecoReg,num.gcms,num.rcps)
# EPA_Wildfire_Fuelbed_testing.m:253
    Check2090Bio=nan(num.ecoReg,num.gcms,num.rcps)
# EPA_Wildfire_Fuelbed_testing.m:254
    #This is to QC that sort order matches for the fuelbed and area burned
    QCmatrix=nan(num.ecoReg,num.yrsReg,num.firemo,num.rcps)
# EPA_Wildfire_Fuelbed_testing.m:257
    tic
    for eco in arange(1,num.ecoReg).reshape(-1):
        disp(concat(['Running ',names.ecoReg[eco],'  |  ',num2str(toc / 60),' min']))
        #Load the Area Burned and IDs
        grids_30=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedIDs30Percent_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:265
        burned_30=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedAreaBurned30_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:266
        grids_70=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedIDs70Percent_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:267
        burned_70=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedAreaBurned70_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:268
        grids_30=cell2mat(struct2cell(grids_30))
# EPA_Wildfire_Fuelbed_testing.m:271
        grids_70=cell2mat(struct2cell(grids_70))
# EPA_Wildfire_Fuelbed_testing.m:272
        burned_30=cell2mat(struct2cell(burned_30))
# EPA_Wildfire_Fuelbed_testing.m:273
        burned_70=cell2mat(struct2cell(burned_70))
# EPA_Wildfire_Fuelbed_testing.m:274
        if 1 == eco:
            names.ecosystClip = copy(cellarray(['242','m242','m261']))
# EPA_Wildfire_Fuelbed_testing.m:278
            num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:279
        else:
            if 2 == eco:
                names.ecosystClip = copy(cellarray(['341','342','m341']))
# EPA_Wildfire_Fuelbed_testing.m:281
                num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:282
            else:
                if 3 == eco:
                    names.ecosystClip = copy(cellarray(['315','331']))
# EPA_Wildfire_Fuelbed_testing.m:284
                    num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:285
                else:
                    if 4 == eco:
                        names.ecosystClip = copy(cellarray(['261','262','m262']))
# EPA_Wildfire_Fuelbed_testing.m:287
                        num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:288
                    else:
                        if 5 == eco:
                            names.ecosystClip = copy(cellarray(['313','321','322','m313']))
# EPA_Wildfire_Fuelbed_testing.m:290
                            num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:291
                        else:
                            if 6 == eco:
                                names.ecosystClip = copy(cellarray(['m331','m332','m333']))
# EPA_Wildfire_Fuelbed_testing.m:293
                                num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:294
        #Import CRU level fuel load and vertically concatenate together
        fuelload1=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[1]]))
# EPA_Wildfire_Fuelbed_testing.m:299
        fuelCRUs1=fuelload1.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:300
        fuelload1=fuelload1.data
# EPA_Wildfire_Fuelbed_testing.m:301
        num.fuelCRUs1 = copy(length(fuelCRUs1))
# EPA_Wildfire_Fuelbed_testing.m:302
        fuelload2=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[2]]))
# EPA_Wildfire_Fuelbed_testing.m:304
        fuelCRUs2=fuelload2.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:305
        fuelload2=fuelload2.data
# EPA_Wildfire_Fuelbed_testing.m:306
        num.fuelCRUs2 = copy(length(fuelCRUs2))
# EPA_Wildfire_Fuelbed_testing.m:307
        fuelload1=horzcat(fuelCRUs1,fuelload1)
# EPA_Wildfire_Fuelbed_testing.m:310
        fuelload2=horzcat(fuelCRUs2,fuelload2)
# EPA_Wildfire_Fuelbed_testing.m:311
        #the eco region & sort based on the CRU/GRIDCODE
        if num.ecosystClip == 2:
            fuelcat=vertcat(fuelload1,fuelload2)
# EPA_Wildfire_Fuelbed_testing.m:317
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:318
        if num.ecosystClip == 3:
            fuelload3=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[3]]))
# EPA_Wildfire_Fuelbed_testing.m:322
            fuelCRUs3=fuelload3.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:323
            fuelload3=fuelload3.data
# EPA_Wildfire_Fuelbed_testing.m:324
            num.fuelCRUs3 = copy(length(fuelCRUs3))
# EPA_Wildfire_Fuelbed_testing.m:325
            fuelload3=horzcat(fuelCRUs3,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:327
            fuelcat=vertcat(fuelload1,fuelload2,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:328
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:329
        if num.ecosystClip == 4:
            fuelload3=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[3]]))
# EPA_Wildfire_Fuelbed_testing.m:333
            fuelCRUs3=fuelload3.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:334
            fuelload3=fuelload3.data
# EPA_Wildfire_Fuelbed_testing.m:335
            num.fuelCRUs3 = copy(length(fuelCRUs3))
# EPA_Wildfire_Fuelbed_testing.m:336
            fuelload3=horzcat(fuelCRUs3,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:338
            fuelcat=vertcat(fuelload1,fuelload2,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:339
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:340
            fuelload4=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[4]]))
# EPA_Wildfire_Fuelbed_testing.m:341
            fuelCRUs4=fuelload4.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:342
            fuelload4=fuelload4.data
# EPA_Wildfire_Fuelbed_testing.m:343
            num.fuelCRUs4 = copy(length(fuelCRUs4))
# EPA_Wildfire_Fuelbed_testing.m:344
            fuelload4=horzcat(fuelCRUs4,fuelload4)
# EPA_Wildfire_Fuelbed_testing.m:345
            fuelcat=vertcat(fuelload1,fuelload2,fuelload3,fuelload4)
# EPA_Wildfire_Fuelbed_testing.m:346
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:347
        #Preallocate matrix to save
    #The 2 is for 2 types of matter (OC versus BC)
        fuelburn=nan(size(fuelcatsort,1),num.yrsReg,num.firemo,num.gcms,num.rcps,2)
# EPA_Wildfire_Fuelbed_testing.m:352
        for mo in arange(1,num.firemo).reshape(-1):
            for year in arange(1,num.yrsReg).reshape(-1):
                #Concatenate 30# and 70# area burned CRUS and associated
            #area burned
                concatgrids=vertcat(grids_30(arange(),year,mo),grids_70(arange(),year,mo))
# EPA_Wildfire_Fuelbed_testing.m:359
                burned_30clip=squeeze(burned_30(arange(),year,mo,arange(),arange()))
# EPA_Wildfire_Fuelbed_testing.m:360
                burned_70clip=squeeze(burned_70(arange(),year,mo,arange(),arange()))
# EPA_Wildfire_Fuelbed_testing.m:361
                for rcp in arange(1,num.rcps).reshape(-1):
                    concatburn=vertcat(burned_30clip(arange(),arange(),rcp),burned_70clip(arange(),arange(),rcp))
# EPA_Wildfire_Fuelbed_testing.m:364
                    concatburn=horzcat(concatgrids,concatburn)
# EPA_Wildfire_Fuelbed_testing.m:365
                    concatburn=sortrows(concatburn)
# EPA_Wildfire_Fuelbed_testing.m:366
                    #burned and fuelbed (QC matrix should be all 0s)
                    QCmatrix[eco,year,mo,rcp]=sum(bsxfun(minus,concatburn(arange(),1),fuelcatsort(arange(),1)),1)
# EPA_Wildfire_Fuelbed_testing.m:371
                    for gcm in arange(1,num.gcms).reshape(-1):
                        #+1 is because the first column is the IDs
                    #4.0 for OC, .59 for BC
                    #Need to take concat and divide by area of grid because
                    #the amount of the total fuel used in the grid cell is
                    #(area burned/total area)*fuel in the total area
                        concatgcm=concatburn(arange(),gcm + 1)
# EPA_Wildfire_Fuelbed_testing.m:379
                        fuelburn[arange(),year,mo,gcm,rcp,1]=multiply(multiply(concatgcm,fuelcatsort(arange(),1 + 1)),4.0)
# EPA_Wildfire_Fuelbed_testing.m:380
                        fuelburn[arange(),year,mo,gcm,rcp,2]=multiply(multiply(concatgcm,fuelcatsort(arange(),2 + 1)),0.59)
# EPA_Wildfire_Fuelbed_testing.m:381
        start=find(names.yrsReg == 2041)
# EPA_Wildfire_Fuelbed_testing.m:387
        stop=find(names.yrsReg == 2050)
# EPA_Wildfire_Fuelbed_testing.m:388
        start2=find(names.yrsReg == 2089)
# EPA_Wildfire_Fuelbed_testing.m:390
        stop2=find(names.yrsReg == 2098)
# EPA_Wildfire_Fuelbed_testing.m:391
        Check2050Bio[eco,arange(),arange()]=squeeze(nanmean(nansum(nansum((fuelburn(arange(),arange(start,stop),arange(),arange(),arange(),1) / 4.0),3),1),2)) / (10 ** 9)
# EPA_Wildfire_Fuelbed_testing.m:394
        Check2090Bio[eco,arange(),arange()]=squeeze(nanmean(nansum(nansum((fuelburn(arange(),arange(start2,stop2),arange(),arange(),arange(),1) / 4.0),3),1),2)) / (10 ** 9)
# EPA_Wildfire_Fuelbed_testing.m:395
        data=copy(fuelburn)
# EPA_Wildfire_Fuelbed_testing.m:397
        clear('key')
        key.dims = copy(cellarray(['CRUs','year','months','gcms','rcps','type']))
# EPA_Wildfire_Fuelbed_testing.m:399
        key.CRUs = copy(concatburn(arange(),1))
# EPA_Wildfire_Fuelbed_testing.m:400
        key.year = copy(names.yrsReg)
# EPA_Wildfire_Fuelbed_testing.m:401
        key.months = copy(names.firemo)
# EPA_Wildfire_Fuelbed_testing.m:402
        key.gcms = copy(names.gcms)
# EPA_Wildfire_Fuelbed_testing.m:403
        key.rcps = copy(names.rcps)
# EPA_Wildfire_Fuelbed_testing.m:404
        key.type = copy(cellarray(['OC','BC']))
# EPA_Wildfire_Fuelbed_testing.m:405
        key.units = copy(cellarray(['kilograms']))
# EPA_Wildfire_Fuelbed_testing.m:406
        clear('data')
    
    #Tables for 2050 and 2090
    for eco in arange(1,num.ecoReg).reshape(-1):
        print2050=squeeze(Check2050Bio(eco,arange(),arange()))
# EPA_Wildfire_Fuelbed_testing.m:414
        print2090=squeeze(Check2090Bio(eco,arange(),arange()))
# EPA_Wildfire_Fuelbed_testing.m:415
        xlsTable(concat([home.outputs,'\Data Files\QC\Biomass_2041to2050_sheet1.xlsx']),print2050,names.ecoReg[eco],names.gcms.T,names.rcps,cellarray(['Tg']),cellarray(['2041-2050']))
        xlsTable(concat([home.outputs,'\Data Files\QC\Biomasssheet7_2089to2098.xlsx']),print2090,names.ecoReg[eco],names.gcms.T,names.rcps,cellarray(['Tg']),cellarray(['2089-2098']))
    
    #Step 3B: For LOCA Baseline of 1986 to 2005
    CheckAnnualBioBase=nan(num.ecoReg,1)
# EPA_Wildfire_Fuelbed_testing.m:425
    CheckAnnualBioBaseClip=nan(num.ecoReg,1)
# EPA_Wildfire_Fuelbed_testing.m:426
    #This is to QC thatsort order matches for the fuelbed and area burned
    QCmatrixbase=nan(num.ecoReg,num.firemo,num.baseEra)
# EPA_Wildfire_Fuelbed_testing.m:429
    tic
    for eco in arange(1,num.ecoReg).reshape(-1):
        disp(concat(['Running ',names.ecoReg[eco],'  |  ',num2str(toc / 60),' min']))
        #Load the Area Burned and IDs
        grids_30=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedIDs30PercentBase_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:437
        burned_30=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedAreaBurned30Base_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:438
        grids_70=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedIDs70PercentBase_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:439
        burned_70=load(concat([home.outputs,'\MAT files\Spatial_Disaggregation\DerivedAreaBurned70Base_',names.ecoReg[eco]]),'data')
# EPA_Wildfire_Fuelbed_testing.m:440
        grids_30=cell2mat(struct2cell(grids_30))
# EPA_Wildfire_Fuelbed_testing.m:443
        grids_70=cell2mat(struct2cell(grids_70))
# EPA_Wildfire_Fuelbed_testing.m:444
        burned_30=cell2mat(struct2cell(burned_30))
# EPA_Wildfire_Fuelbed_testing.m:445
        burned_70=cell2mat(struct2cell(burned_70))
# EPA_Wildfire_Fuelbed_testing.m:446
        if 1 == eco:
            names.ecosystClip = copy(cellarray(['242','m242','m261']))
# EPA_Wildfire_Fuelbed_testing.m:450
            num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:451
        else:
            if 2 == eco:
                names.ecosystClip = copy(cellarray(['341','342','m341']))
# EPA_Wildfire_Fuelbed_testing.m:453
                num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:454
            else:
                if 3 == eco:
                    names.ecosystClip = copy(cellarray(['315','331']))
# EPA_Wildfire_Fuelbed_testing.m:456
                    num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:457
                else:
                    if 4 == eco:
                        names.ecosystClip = copy(cellarray(['261','262','m262']))
# EPA_Wildfire_Fuelbed_testing.m:459
                        num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:460
                    else:
                        if 5 == eco:
                            names.ecosystClip = copy(cellarray(['313','321','322','m313']))
# EPA_Wildfire_Fuelbed_testing.m:462
                            num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:463
                        else:
                            if 6 == eco:
                                names.ecosystClip = copy(cellarray(['m331','m332','m333']))
# EPA_Wildfire_Fuelbed_testing.m:465
                                num.ecosystClip = copy(length(names.ecosystClip))
# EPA_Wildfire_Fuelbed_testing.m:466
        #Import CRU level fuel load and vertically concatenate together
        fuelload1=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[1]]))
# EPA_Wildfire_Fuelbed_testing.m:471
        fuelCRUs1=fuelload1.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:472
        fuelload1=fuelload1.data
# EPA_Wildfire_Fuelbed_testing.m:473
        num.fuelCRUs1 = copy(length(fuelCRUs1))
# EPA_Wildfire_Fuelbed_testing.m:474
        fuelload2=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[2]]))
# EPA_Wildfire_Fuelbed_testing.m:476
        fuelCRUs2=fuelload2.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:477
        fuelload2=fuelload2.data
# EPA_Wildfire_Fuelbed_testing.m:478
        num.fuelCRUs2 = copy(length(fuelCRUs2))
# EPA_Wildfire_Fuelbed_testing.m:479
        fuelload1=horzcat(fuelCRUs1,fuelload1)
# EPA_Wildfire_Fuelbed_testing.m:482
        fuelload2=horzcat(fuelCRUs2,fuelload2)
# EPA_Wildfire_Fuelbed_testing.m:483
        #the eco region & sort based on the CRU/GRIDCODE
        if num.ecosystClip == 2:
            fuelcat=vertcat(fuelload1,fuelload2)
# EPA_Wildfire_Fuelbed_testing.m:489
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:490
        if num.ecosystClip == 3:
            fuelload3=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[3]]))
# EPA_Wildfire_Fuelbed_testing.m:494
            fuelCRUs3=fuelload3.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:495
            fuelload3=fuelload3.data
# EPA_Wildfire_Fuelbed_testing.m:496
            num.fuelCRUs3 = copy(length(fuelCRUs3))
# EPA_Wildfire_Fuelbed_testing.m:497
            fuelload3=horzcat(fuelCRUs3,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:499
            fuelcat=vertcat(fuelload1,fuelload2,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:500
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:501
        if num.ecosystClip == 4:
            fuelload3=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[3]]))
# EPA_Wildfire_Fuelbed_testing.m:505
            fuelCRUs3=fuelload3.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:506
            fuelload3=fuelload3.data
# EPA_Wildfire_Fuelbed_testing.m:507
            num.fuelCRUs3 = copy(length(fuelCRUs3))
# EPA_Wildfire_Fuelbed_testing.m:508
            fuelload3=horzcat(fuelCRUs3,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:510
            fuelcat=vertcat(fuelload1,fuelload2,fuelload3)
# EPA_Wildfire_Fuelbed_testing.m:511
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:512
            fuelload4=load(concat([home.outputs,'\MAT Files\Fuelbed\CRUlevel_',names.ecosystClip[4]]))
# EPA_Wildfire_Fuelbed_testing.m:513
            fuelCRUs4=fuelload4.key.IDs
# EPA_Wildfire_Fuelbed_testing.m:514
            fuelload4=fuelload4.data
# EPA_Wildfire_Fuelbed_testing.m:515
            num.fuelCRUs4 = copy(length(fuelCRUs4))
# EPA_Wildfire_Fuelbed_testing.m:516
            fuelload4=horzcat(fuelCRUs4,fuelload4)
# EPA_Wildfire_Fuelbed_testing.m:517
            fuelcat=vertcat(fuelload1,fuelload2,fuelload3,fuelload4)
# EPA_Wildfire_Fuelbed_testing.m:518
            fuelcatsort=sortrows(fuelcat)
# EPA_Wildfire_Fuelbed_testing.m:519
        #Preallocate matrix to save
    #The 2 is for 2 types of matter (OC versus BC)
        fuelburn=nan(size(fuelcatsort,1),num.baseEra,num.firemo,2)
# EPA_Wildfire_Fuelbed_testing.m:525
        for mo in arange(1,num.firemo).reshape(-1):
            for year in arange(1,num.baseEra).reshape(-1):
                #Concatenate 30# and 70# area burned CRUS and associated
            #area burned
                concatgrids=vertcat(grids_30(arange(),year,mo),grids_70(arange(),year,mo))
# EPA_Wildfire_Fuelbed_testing.m:532
                burned_30clip=squeeze(burned_30(arange(),year,mo))
# EPA_Wildfire_Fuelbed_testing.m:533
                burned_70clip=squeeze(burned_70(arange(),year,mo))
# EPA_Wildfire_Fuelbed_testing.m:534
                concatburn=vertcat(burned_30clip,burned_70clip)
# EPA_Wildfire_Fuelbed_testing.m:536
                concatburn=horzcat(concatgrids,concatburn)
# EPA_Wildfire_Fuelbed_testing.m:537
                concatburn=sortrows(concatburn)
# EPA_Wildfire_Fuelbed_testing.m:538
                #burned and fuelbed (QC matrix should be all 0s)
                QCmatrixbase[eco,mo,year]=sum(bsxfun(minus,concatburn(arange(),1),fuelcatsort(arange(),1)),1)
# EPA_Wildfire_Fuelbed_testing.m:542
                fuelburn[arange(),year,mo,1]=multiply(multiply(concatburn(arange(),2),fuelcatsort(arange(),1 + 1)),4.0)
# EPA_Wildfire_Fuelbed_testing.m:545
                fuelburn[arange(),year,mo,2]=multiply(multiply(concatburn(arange(),2),fuelcatsort(arange(),2 + 1)),0.59)
# EPA_Wildfire_Fuelbed_testing.m:546
        start=find(names.baseEra == 1986)
# EPA_Wildfire_Fuelbed_testing.m:551
        stop=find(names.baseEra == 2004)
# EPA_Wildfire_Fuelbed_testing.m:552
        stop1=find(names.baseEra == 2000)
# EPA_Wildfire_Fuelbed_testing.m:553
        CheckAnnualBioBase[eco,1]=squeeze(nanmean(nansum(nansum((fuelburn(arange(),arange(start,stop),arange(),1) / 4.0),3),1),2)) / (10 ** 9)
# EPA_Wildfire_Fuelbed_testing.m:555
        CheckAnnualBioBaseClip[eco,1]=squeeze(nanmean(nansum(nansum((fuelburn(arange(),arange(start,stop1),arange(),1) / 4.0),3),1),2)) / (10 ** 9)
# EPA_Wildfire_Fuelbed_testing.m:556
        data=copy(fuelburn)
# EPA_Wildfire_Fuelbed_testing.m:558
        clear('key')
        key.dims = copy(cellarray(['CRUs','year','months','type']))
# EPA_Wildfire_Fuelbed_testing.m:560
        key.CRUs = copy(concatburn(arange(),1))
# EPA_Wildfire_Fuelbed_testing.m:561
        key.year = copy(names.baseEra)
# EPA_Wildfire_Fuelbed_testing.m:562
        key.months = copy(names.firemo)
# EPA_Wildfire_Fuelbed_testing.m:563
        key.type = copy(cellarray(['OC','BC']))
# EPA_Wildfire_Fuelbed_testing.m:564
        key.units = copy(cellarray(['kilograms']))
# EPA_Wildfire_Fuelbed_testing.m:565
        clear('data')
    