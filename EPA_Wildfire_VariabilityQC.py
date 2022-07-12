# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_VariabilityQC.m

    ## QC of Interannual Variability
    
    ## Step 0. Setup
    
    redtoblue=makeColorMap(concat([0.9,0.4,0.4]),concat([1,1,1]),concat([0.3,0.3,0.7]),100)
# EPA_Wildfire_VariabilityQC.m:5
    lims[1]=concat([0,2])
# EPA_Wildfire_VariabilityQC.m:6
    lims[2]=lims[1]
# EPA_Wildfire_VariabilityQC.m:6
    lims[3]=lims[1]
# EPA_Wildfire_VariabilityQC.m:6
    lims[4]=lims[1]
# EPA_Wildfire_VariabilityQC.m:6
    lims[5]=concat([0,60])
# EPA_Wildfire_VariabilityQC.m:7
    lims[6]=concat([0,3])
# EPA_Wildfire_VariabilityQC.m:8
    lims[7]=lims[6]
# EPA_Wildfire_VariabilityQC.m:8
    lims[8]=lims[6]
# EPA_Wildfire_VariabilityQC.m:8
    lims[9]=concat([0,80])
# EPA_Wildfire_VariabilityQC.m:9
    lims[10]=concat([0,300])
# EPA_Wildfire_VariabilityQC.m:10
    lims[11]=concat([0,250])
# EPA_Wildfire_VariabilityQC.m:11
    #ecoregion key
    __,names.ecoregions=xlsread('L:\02 Projects\EPA CIRA 3\Inputs\Maps and Keys\spatial keys and weights\LOCA_ecoregion.xlsx','key','B:B',nargout=2)
# EPA_Wildfire_VariabilityQC.m:14
    num.ecoregions = copy(length(names.ecoregions))
# EPA_Wildfire_VariabilityQC.m:16
    ## Step 1a.  Grid Cell Level IQR
    for var in arange(1,num.newvars).reshape(-1):
        load(concat([home.cluster,'\EPA Wildfire\Base_',names.newvars[var]]))
        if var < 5:
            quantiles=quantile(data,concat([0.25,0.75]),2)
# EPA_Wildfire_VariabilityQC.m:22
            iqr=abs(quantiles(arange(),2) - quantiles(arange(),1))
# EPA_Wildfire_VariabilityQC.m:23
            a=nan(67420,1)
# EPA_Wildfire_VariabilityQC.m:25
            a[names.crus]=iqr
# EPA_Wildfire_VariabilityQC.m:26
            toMap=cru2mat(a)
# EPA_Wildfire_VariabilityQC.m:27
        else:
            quantiles=nan(num.lats,num.lons,2)
# EPA_Wildfire_VariabilityQC.m:30
            for lat in arange(1,num.lats).reshape(-1):
                quantiles[lat,arange(),arange()]=abs(quantile(squeeze(data(lat,arange(),arange())),concat([0.25,0.75]),2))
# EPA_Wildfire_VariabilityQC.m:32
            iqr=abs(quantiles(arange(),arange(),2) - quantiles(arange(),arange(),1))
# EPA_Wildfire_VariabilityQC.m:34
            toMap=nan(dot(180,16),dot(360,16),'single')
# EPA_Wildfire_VariabilityQC.m:35
            data=copy(iqr)
# EPA_Wildfire_VariabilityQC.m:36
            data=multiply(data,fullMask)
# EPA_Wildfire_VariabilityQC.m:37
            toMap[arange(top,bottom),arange(left,right)]=data
# EPA_Wildfire_VariabilityQC.m:38
        subplot(2,1,1)
        mapGrid(double(toMap),'latRange',concat([24,54]),'lonRange',concat([- 125.5,- 66.5]),'colors',redtoblue,'colorlimits',lims[var],'boundaryline','state','linecolor',concat([0.3,0.3,0.3]),'projection','albers','linewidth',0.2,'frame','off')
        h=copy(colorbar)
# EPA_Wildfire_VariabilityQC.m:45
        set(h,'position',concat([0.8,0.6,0.02,0.3]))
        title(concat(['IQR for Annual ',names.newvars[var],' 1986-2005']))
        subplot(2,1,2)
        hist(reshape(toMap,[],1),50)
        title('Distribution of IQR Values Across Cells')
        print_('-djpeg','-r300',concat([home.graphics,'\Variability\griddedIQR_Base_',names.newvars[var]]))
        close_
    
    ## Step 1b.  Grid Cell Level Full Range
    for var in arange(1,num.newvars).reshape(-1):
        load(concat([home.cluster,'\CIRA 3 Wildfire\Base_',names.newvars[var]]))
        if var < 5:
            quantiles=quantile(data,concat([0,1]),2)
# EPA_Wildfire_VariabilityQC.m:62
            iqr=abs(quantiles(arange(),2) - quantiles(arange(),1))
# EPA_Wildfire_VariabilityQC.m:63
            a=nan(67420,1)
# EPA_Wildfire_VariabilityQC.m:65
            a[names.crus]=iqr
# EPA_Wildfire_VariabilityQC.m:66
            toMap=cru2mat(a)
# EPA_Wildfire_VariabilityQC.m:67
        else:
            quantiles=nan(num.lats,num.lons,2)
# EPA_Wildfire_VariabilityQC.m:70
            for lat in arange(1,num.lats).reshape(-1):
                quantiles[lat,arange(),arange()]=abs(quantile(squeeze(data(lat,arange(),arange())),concat([0,1]),2))
# EPA_Wildfire_VariabilityQC.m:72
            iqr=abs(quantiles(arange(),arange(),2) - quantiles(arange(),arange(),1))
# EPA_Wildfire_VariabilityQC.m:74
            toMap=nan(dot(180,16),dot(360,16),'single')
# EPA_Wildfire_VariabilityQC.m:75
            data=copy(iqr)
# EPA_Wildfire_VariabilityQC.m:76
            data=multiply(data,fullMask)
# EPA_Wildfire_VariabilityQC.m:77
            toMap[arange(top,bottom),arange(left,right)]=data
# EPA_Wildfire_VariabilityQC.m:78
        subplot(2,1,1)
        mapGrid(double(toMap),'latRange',concat([24,54]),'lonRange',concat([- 125.5,- 66.5]),'colors',redtoblue,'colorlimits',lims[var],'boundaryline','state','linecolor',concat([0.3,0.3,0.3]),'projection','albers','linewidth',0.2,'frame','off')
        h=copy(colorbar)
# EPA_Wildfire_VariabilityQC.m:85
        set(h,'position',concat([0.8,0.6,0.02,0.3]))
        title(concat(['Full Range for Annual ',names.newvars[var],' 1986-2005']))
        subplot(2,1,2)
        hist(reshape(toMap,[],1),50)
        title('Distribution of Full Range Values Across Cells')
        print_('-djpeg','-r300',concat([home.graphics,'\Variability\griddedFullRange_Base_',names.newvars[var]]))
        close_
    
    
    ## Step 2.  Ecoregion Level
    load(concat([home.outputs,'\MAT files\Wildfire\Baseline']))
    quantiles=quantile(data,concat([0.25,0.75]),2)
# EPA_Wildfire_VariabilityQC.m:100
    iqr=abs(squeeze((quantiles(arange(),2,arange()) - quantiles(arange(),1,arange()))))
# EPA_Wildfire_VariabilityQC.m:101
    for var in arange(1,num.newvars).reshape(-1):
        subplot(2,1,1)
        boxPlot(data(arange(),arange(),var).T,0)
        title(concat([names.newvars[var],'- Baseline Values for 20 Years (1986-2005)']))
        set(gca,'xtick',concat([arange(1,6,1)]),'xticklabel',cellarray(['1 PNW','2 NM/SD','3 ERM/GP','4 CCS','5 DSW','6 RMF']))
        subplot(2,1,2)
        bar(data(arange(),arange(),var),'b')
        set(gca,'xtick',concat([arange(1,6,1)]),'xticklabel',cellarray(['1 PNW','2 NM/SD','3 ERM/GP','4 CCS','5 DSW','6 RMF']))
        print_('-djpeg','-r300',concat([home.graphics,'\Variability\Base_',names.newvars[var],'_Ecoregion']))
        close_
    
    ## Step 3.  Check the Variability
    names.binnedVars = copy(cellarray(['wspd','relh','radiation']))
# EPA_Wildfire_VariabilityQC.m:121
    num.binnedVars = copy(length(names.binnedVars))
# EPA_Wildfire_VariabilityQC.m:122
    home.oldloca = copy('L:\02 Projects\EPA CIRA II\Outputs\MC2\grid2mat files')
# EPA_Wildfire_VariabilityQC.m:123
    start=find(names.baseYrs == 1986)
# EPA_Wildfire_VariabilityQC.m:124
    load(concat([home.cluster,'\HAWQS Project 10.2017\Outputs\NewVars_cru\Final Files\','USproj_LOCA_Base_relh']))
    nans=isnan(data(arange(),1,1))
# EPA_Wildfire_VariabilityQC.m:128
    clear('data')
    #first get the princeton data
    load(concat([home.cluster,'\HAWQS Project 10.2017\Outputs\princeHAWQS']))
    princeHAWQS[nans,arange(),arange(),arange()]=nan
# EPA_Wildfire_VariabilityQC.m:132
    princeHAWQS=squeeze(nanmean(nanmean(princeHAWQS,1),2))
# EPA_Wildfire_VariabilityQC.m:133
    for var in arange(1,num.binnedVars).reshape(-1):
        #princeton
        princeBox=princeHAWQS(arange(),var + 3)
# EPA_Wildfire_VariabilityQC.m:138
        load(concat([home.cluster,'\HAWQS Project 10.2017\Outputs\NewVars_cru\Final Files\','USproj_LOCA_Base_',names.binnedVars[var]]))
        locaBox=squeeze(nanmean(nanmean(data(arange(),arange(),arange(start,start + 19)),1),2))
# EPA_Wildfire_VariabilityQC.m:143
        clear('data')
        crus=key.crus
# EPA_Wildfire_VariabilityQC.m:144
        load(concat([home.oldloca,'\USproj_LOCA_NewBase_',names.binnedVars[var]]))
        beta=squeeze(nanmean(data(arange(),arange(),arange(),arange(start,start + 19)),3))
# EPA_Wildfire_VariabilityQC.m:148
        clear('data')
        top=dot((90 - (key.centroidLatLon(1,1) + (1 / 4))),2)
# EPA_Wildfire_VariabilityQC.m:150
        top=top + 1
# EPA_Wildfire_VariabilityQC.m:151
        bottom=dot((90 - (key.centroidLatLon(end(),1) - (1 / 4))),2)
# EPA_Wildfire_VariabilityQC.m:152
        left=dot(((key.centroidLatLon(1,2) - (1 / 4)) + 180),2)
# EPA_Wildfire_VariabilityQC.m:153
        left=left + 1
# EPA_Wildfire_VariabilityQC.m:154
        right=dot(((key.centroidLatLon(end(),2) + (1 / 4)) + 180),2)
# EPA_Wildfire_VariabilityQC.m:155
        a=nan(360,720,20,'single')
# EPA_Wildfire_VariabilityQC.m:157
        a[arange(top,bottom),arange(left,right),arange()]=beta
# EPA_Wildfire_VariabilityQC.m:158
        beta=mat2cru(a)
# EPA_Wildfire_VariabilityQC.m:160
        beta=beta(crus,arange())
# EPA_Wildfire_VariabilityQC.m:161
        beta[nans,arange()]=nan
# EPA_Wildfire_VariabilityQC.m:162
        betaBox=squeeze(nanmean(beta,1)).T
# EPA_Wildfire_VariabilityQC.m:164
        boxes=concat([princeBox,betaBox,locaBox])
# EPA_Wildfire_VariabilityQC.m:167
        boxplot(boxes,'Labels',cellarray(['Princeton','Beta LOCA','LOCA']))
        title(concat(['Distribution of average annual ',names.binnedVars[var],' (1986-2005)']))
        print_('-djpeg','-r300',concat([home.graphics,'Variability\Baseline_Comparison_Box_',names.binnedVars[var]]))
        close_
        #bar!
        bars=concat([princeBox,betaBox,locaBox])
# EPA_Wildfire_VariabilityQC.m:176
        bar(bars)
        xlim(concat([0,21]))
        if var == 1:
            ylim(concat([3,3.5]))
        else:
            if var == 2:
                ylim(concat([55,70]))
            else:
                ylim(concat([14,16]))
        legend('Princeton','betaLOCA','LOCA')
        title(concat(['Distribution of average annual ',names.binnedVars[var],' (1986-2005)']))
        print_('-djpeg','-r300',concat([home.graphics,'Variability\Baseline_Comparison_Bar_',names.binnedVars[var]]))
        close_
    
    for var in arange(1,num.binnedVars).reshape(-1):
        #LOCA
        load(concat([home.cluster,'\HAWQS Project 10.2017\Outputs\NewVars_cru\Final Files\','USproj_LOCA_Base_',names.binnedVars[var]]))
        start=find(names.baseYrs == 1986)
# EPA_Wildfire_VariabilityQC.m:200
        loca=squeeze(nanmean(nanmean(data(arange(),arange(),arange(start,start + 19)),2),3))
# EPA_Wildfire_VariabilityQC.m:201
        clear('data')
        crus=key.crus
# EPA_Wildfire_VariabilityQC.m:202
        load(concat([home.oldloca,'\USproj_LOCA_NewBase_',names.binnedVars[var]]))
        top=dot((90 - (key.centroidLatLon(1,1) + (1 / 4))),2)
# EPA_Wildfire_VariabilityQC.m:208
        top=top + 1
# EPA_Wildfire_VariabilityQC.m:209
        bottom=dot((90 - (key.centroidLatLon(end(),1) - (1 / 4))),2)
# EPA_Wildfire_VariabilityQC.m:210
        left=dot(((key.centroidLatLon(1,2) - (1 / 4)) + 180),2)
# EPA_Wildfire_VariabilityQC.m:211
        left=left + 1
# EPA_Wildfire_VariabilityQC.m:212
        right=dot(((key.centroidLatLon(end(),2) + (1 / 4)) + 180),2)
# EPA_Wildfire_VariabilityQC.m:213
        a=nan(360,720)
# EPA_Wildfire_VariabilityQC.m:214
        a[arange(top,bottom),arange(left,right)]=squeeze(nanmean(nanmean(data(arange(),arange(),arange(),arange(start,start + 19)),3),4))
# EPA_Wildfire_VariabilityQC.m:215
        beta=mat2cru(a)
# EPA_Wildfire_VariabilityQC.m:216
        beta=beta(crus,arange())
# EPA_Wildfire_VariabilityQC.m:217
        dev=dot(((loca - beta) / beta),100)
# EPA_Wildfire_VariabilityQC.m:219
        subplot(2,1,1)
        hist(dev,50)
        title(concat([names.binnedVars[var],' : %deviation between runs of 1986-2005 baseline ']))
        subplot(2,1,2)
        a=nan(67420,1)
# EPA_Wildfire_VariabilityQC.m:226
        a[crus]=dev
# EPA_Wildfire_VariabilityQC.m:227
        b=cru2mat(a)
# EPA_Wildfire_VariabilityQC.m:228
        mapGrid(double(b),'latRange',concat([24,54]),'lonRange',concat([- 125.5,- 66.5]),'colors',makeColorMap(concat([1,0.3,0.3]),concat([1,1,1]),concat([0.3,0.3,1]),50),'colorlimits',concat([- 2,2]),'boundaryline','state','linecolor',concat([0.3,0.3,0.3]),'projection','albers','linewidth',0.2,'frame','on')
        colorbar
        print_('-djpeg','-r300',concat([home.graphics,'Variability\Baseline_Comparison_Map_',names.binnedVars[var]]))
        close_
    