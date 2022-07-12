# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_Validate.m

    ## Validate Process Aganst Example Data
    
    ## Setup
    clear('fullMask','locaMask')
    # create arrays that store month-specific values 
#validation data starts on January 3rd so January has 29 days
    lmonLeap=concat([[29],[29],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]])
# EPA_Wildfire_Validate.m:8
    el=concat([[6.5],[7.5],[9.0],[12.8],[13.9],[13.9],[12.4],[10.9],[9.4],[8.0],[7.0],[6.0]])
# EPA_Wildfire_Validate.m:9
    fl=concat([[- 1.6],[- 1.6],[- 1.6],[0.9],[3.8],[5.8],[6.4],[5.0],[2.4],[0.4],[- 1.6],[- 1.6]])
# EPA_Wildfire_Validate.m:10
    monthIndexLeap=single([])
# EPA_Wildfire_Validate.m:12
    for month in arange(1,12).reshape(-1):
        monthIndexLeap=vertcat(monthIndexLeap,repmat(month,lmonLeap(month),1))
# EPA_Wildfire_Validate.m:14
    
    ## Get Data 
#load tasmax and pr and set some temporary values
    input_=dlmread(concat([home.inputs,'\Data Files\wildfire\inputs\fwi_ca_1984.txt']))
# EPA_Wildfire_Validate.m:19
    temporary.yrDays = copy(size(input_,1))
# EPA_Wildfire_Validate.m:20
    temporary.monthIndex = copy(monthIndexLeap)
# EPA_Wildfire_Validate.m:21
    RAWpr=input_(arange(),6)
# EPA_Wildfire_Validate.m:22
    RAWtasmax=input_(arange(),3)
# EPA_Wildfire_Validate.m:23
    RAWrh=input_(arange(),4)
# EPA_Wildfire_Validate.m:24
    #preallocate the year data
    yrData=nan(temporary.yrDays,3,'single')
# EPA_Wildfire_Validate.m:27
    ## Run Matrix Scripts
# set initial values
    dmc_init=6.0
# EPA_Wildfire_Validate.m:30
    dc_init=15.0
# EPA_Wildfire_Validate.m:31
    tic
    for day in arange(1,temporary.yrDays).reshape(-1):
        disp(concat(['Processing ... Matrix Day ',num2str(day),'  |  ',num2str(toc / 60),' min']))
        mon=temporary.monthIndex(day)
# EPA_Wildfire_Validate.m:38
        temp=RAWtasmax(day)
# EPA_Wildfire_Validate.m:40
        rain=RAWpr(day)
# EPA_Wildfire_Validate.m:42
        rh=RAWrh(day)
# EPA_Wildfire_Validate.m:44
        CIRA3_Wildfire_ExtraVars_DMCPart
        CIRA3_Wildfire_ExtraVars_DCPart
        CIRA3_Wildfire_ExtraVars_BUIPart
        #save variables to output file
        yrData[day,1]=bui
# EPA_Wildfire_Validate.m:52
        yrData[day,2]=dc
# EPA_Wildfire_Validate.m:53
        yrData[day,3]=dmc
# EPA_Wildfire_Validate.m:54
        dmc_init=copy(dmc)
# EPA_Wildfire_Validate.m:57
        dc_init=copy(dc)
# EPA_Wildfire_Validate.m:57
    
    ## Compare to output
    output=dlmread(concat([home.inputs,'\Data Files\wildfire\outputs\fwi_ca_1984_mod.txt']))
# EPA_Wildfire_Validate.m:62
    output=output(arange(),concat([10,9,8]))
# EPA_Wildfire_Validate.m:63
    compare=dot(((yrData - output) / output),100)
# EPA_Wildfire_Validate.m:65
    ## Histogram and Line Plots
    subplot(2,1,1)
    plot(compare(arange(),1))
    title('Percent Difference between IEc Results and Test Set')
    xlim(concat([0,303]))
    subplot(2,1,2)
    hist(compare(arange(),1),50)
    print_('-djpeg','-r300',concat([home.graphics,'\ValidationPercentDif_BUI']))
    close_
    subplot(2,1,1)
    plot(compare(arange(),2))
    title('Percent Difference between IEc Results and Test Set')
    xlim(concat([0,303]))
    subplot(2,1,2)
    hist(compare(arange(),2),50)
    print_('-djpeg','-r300',concat([home.graphics,'\ValidationPercentDif_DC']))
    close_
    subplot(2,1,1)
    plot(compare(arange(),3))
    title('Percent Difference between IEc Results and Test Set')
    xlim(concat([0,303]))
    subplot(2,1,2)
    hist(compare(arange(),3),50)
    print_('-djpeg','-r300',concat([home.graphics,'\ValidationPercentDif_DMC']))
    close_
    ## Double Y Axi
    x1=concat([arange(1,303)])
# EPA_Wildfire_Validate.m:89
    y1=horzcat(output(arange(),3),yrData(arange(),3))
# EPA_Wildfire_Validate.m:90
    x2=copy(x1)
# EPA_Wildfire_Validate.m:91
    y2=compare(arange(),3)
# EPA_Wildfire_Validate.m:92
    figure
    hAx,hLine1,hLine2=plotyy(x1,y1,x2,y2,nargout=3)
# EPA_Wildfire_Validate.m:94
    set(hLine1,'LineWidth',1.5)
    set(hLine2,'LineWidth',1.5)
    title('Compare DMC Results')
    xlabel('Day (Jan-October)')
    ylabel(hAx(1),'DMC')
    ylabel(hAx(2),'Percent Difference')
    hold('on')
    x3=cumsum(lmonLeap(arange(1,10))) - 2
# EPA_Wildfire_Validate.m:107
    for i in arange(1,length(x3)).reshape(-1):
        line(concat([x3(i),x3(i)]),concat([0,500]))
    
    hold('off')