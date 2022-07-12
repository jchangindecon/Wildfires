# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_TestNETCDF.m

    ## Code to test NETCDF files sent to us from GCAM
# Run master and Spatial Disagg setup first!
    ncdisp('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\Cristoph Files\Wildfires\base_edit.nc4')
    var=ncread('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\Cristoph Files\Wildfires\base_edit.nc4','Base_OC')
# EPA_Wildfire_TestNETCDF.m:5
    lat=ncread('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\Cristoph Files\Wildfires\base_edit.nc4','lat')
# EPA_Wildfire_TestNETCDF.m:6
    lon=ncread('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\Cristoph Files\Wildfires\base_edit.nc4','lon')
# EPA_Wildfire_TestNETCDF.m:7
    num=dot(length(lat),length(lon))
# EPA_Wildfire_TestNETCDF.m:9
    #Reshape data into long list of lat and lons
#Note that it is sorted by lon then lat
    datalist=reshape(var,num,60)
# EPA_Wildfire_TestNETCDF.m:13
    sumcheck=sum(datalist,2)
# EPA_Wildfire_TestNETCDF.m:14
    reduce=sumcheck != 0
# EPA_Wildfire_TestNETCDF.m:15
    dataall=datalist(reduce,arange())
# EPA_Wildfire_TestNETCDF.m:16
    #Load in my data from netcdf
    datanet=ncread('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\ALL Final Files\NetCDFlinear\base.nc','Base_OC')
# EPA_Wildfire_TestNETCDF.m:19
    latnet=ncread('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\ALL Final Files\NetCDFlinear\base.nc','lat')
# EPA_Wildfire_TestNETCDF.m:20
    lonnet=ncread('L:\02 Projects\EPA Wildfire\Outputs\MAT Files\ALL Final Files\NetCDFlinear\base.nc','lon')
# EPA_Wildfire_TestNETCDF.m:21
    #Divide datanet by 30 days per month, 24 hours in a day, 60 min and 60 sec
    datasec=datanet / (dot(dot(dot(30,24),60),60))
# EPA_Wildfire_TestNETCDF.m:24
    #Test maxima
    max1=max(dataall)
# EPA_Wildfire_TestNETCDF.m:27
    max2=max(datasec)
# EPA_Wildfire_TestNETCDF.m:28
    dif=(max1 - max2) / max2
# EPA_Wildfire_TestNETCDF.m:29
    
    #Test minima
    ref1=dataall > 0
# EPA_Wildfire_TestNETCDF.m:32
    ref2=datasec > 0
# EPA_Wildfire_TestNETCDF.m:33
    min1=min(dataall(ref1))
# EPA_Wildfire_TestNETCDF.m:34
    min2=min(datasec(ref2))
# EPA_Wildfire_TestNETCDF.m:35
    #minima also very similar