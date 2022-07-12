# Generated with SMOP  0.41
from libsmop import *
# EPA_Wildfire_Master.m

    
    ## Master Script for CIRA 3 Wildfire Data Processing
# Instructions: L:\02 Projects\EPA CIRA 3\02 Documents\Wildfire\Wildfires
# LOCA Data Prep.docx
# Lisa Rennels, RA at Industrial Economics Inc.
# Alisa White, RA at Industrial Economics Inc.
# 1/30/2018, last updated 08/2018
# 
# 1 rhAnn*	Annual average monthly relative humidity (#) for  the current year
# 2 rhPAnn*	Annual average monthly relative humidity (#) for the previous year
# 3 rhPFS*	Average monthly relative humidity (#) during the previous year’s fire season (May through October)
# 4 rhPW*	Average monthly relative humidity (#) during the previous year’s winter (December through February)
# 5 prPSu*	Average total daily precipitation (mm) during the summer (June through August) two years previously (t-2) 
# 6 TmaxAnn*	Annual average monthly maximum temperature (°C) for  the current year
# 7 TmaxPW*	Average monthly maximum temperature (°C) during the previous year’s winter (December through February)
# 8 TmaxSu*	Average monthly maximum temperature (°C) during the current year’s summer (June through August)
# 9 BUI**	Average daily BUI during the current year’s fire season (May through October)
# 10 DCmax**	Maximum daily DC during the current year’s fire season (May through October)
# 11 DMCmax**	Maximum daily DMC during the current year’s fire season (May through October)
# 12 PrFS*  Average total daily precipitation (mm) during  year's fire season (May througH October)
# * Variables should be calculated by first calculating monthly means and then averaging these results to obtain seasonal or annual means.
# ** Daily estimates of these variables should be calculated using the logic provided below this table. For these variables the daily estimates should be used to determine maximum or average seasonal values.
# NOTE that prPSu was instructed to be monthly precip, but later reserch
# found it should be daily, and this was changed
    clear
    clc
    cd('L:\02 Projects\EPA Wildfire\src')
    ##  Step 0. Setup
    EPA_Wildfire_Setup
    ## SECTION 1.  Create Variables -----------------------------------------##
##-----------------------------------------------------------------------##
    switches.section1 = copy(false)
# EPA_Wildfire_Master.m:33
    if switches.section1:
        ## Step 1a.  Aggregate to Ecoregions 
    #for each of tasmax and pr, select the cells pertaining to the correct CRU
    #cells, and then aggregate to ecoregion
        EPA_Wildfire_AggEcoregions_relh
        EPA_Wildfire_AggEcoregions
        EPA_Wildfire_QCecoregions
        ## Step 1b.  Create Month-Based Variables for pr and tasmax
        EPA_Wildfire_pr
        EPA_Wildfire_tasmax
        ##  Step 1c.  Create  Day-Based Variables
        EPA_Wildfire_ExtraVarsBase
        EPA_Wildfire_ExtraVars
        ## Step 1d.  Create Month-Based Variables for relh
        EPA_Wildfire_relh
        ## Step 1e.  Consolidate into one Proj & one Base file
        EPA_Wildfire_Consolidate
        ## Step 1f.  QC
        EPA_Wildfire_QCecoregions_Part2
        #the scripts below are unedited from the deprecated version of this code,
    #they can be adapted if these categories of extra QC are requested
    # EPA_Wildfire_TestParts
    # EPA_Wildfire_Validate
    # EPA_Wildfire_VariabilityQC
        cropFigDir(home.graphics,home.graphics,'jpg')
    
    ## SECTION 2.  Wildfires Analysis ---------------------------------------##
##-----------------------------------------------------------------------##
    switches.section2 = copy(true)
# EPA_Wildfire_Master.m:69
    if switches.section2:
        ## Step 2a. Run Regressions at Ecoregions level
        EPA_Wildfire_Regs
        #     EPA_Wildfire_QCHist # Code to output tables to make histograms with (LFR - broken because missing file)
        ## Step 2b. Spatially/Temporally Disaggregate
        # This is an important Setup from this step, it can be run once 
    # Sections 1-2a have been run to create their output files
        EPA_Wildfire_SpatialDisaggSetup
        # Spatially and temporally disaggregate area burned from Step 4
    # Note: this step has a randomization component ONLY RUN ONCE
        switches.step2b = copy(false)
# EPA_Wildfire_Master.m:83
        if switches.step2b:
            EPA_Wildfire_SpatialDisagg_v2
        ## Step 2c. Converting Area Burned to Biomass Consumed (as well as saving
    # intermediate files of area burned)
        EPA_Wildfire_Fuelbed
        EPA_Wildfire_AreaBurnedAggregation
    
    ## SECTION 3.  Maps and Export Data -------------------------------------##
##-----------------------------------------------------------------------##
    switches.section3 = copy(true)
# EPA_Wildfire_Master.m:97
    if switches.section3:
        # Step 3a. Make Maps of Fuel Beds
        EPA_Wildfire_Fuelbed_Maps
        # Step 3b. Make Original NetCDF Files for Validation
        EPA_Wildfire_Mat2NetCDFformatted
    
    ## SECTION 4.  Maps and Export Data Part II -----------------------------##
##-----------------------------------------------------------------------##
    switches.section4 = copy(false)
# EPA_Wildfire_Master.m:108
    if switches.section4:
        cd('Manuscript Maps')
        #Step 4a. Make Maps for Manuscript: check this Master script for the correct switches on or off
        Manuscript_Maps_Master
        #Step 4b. Make Original NetCDF Files for Validation
        EPA_Wildfire_AllNetCDF
        cd('..')
    
    ## SECTION 5.  Optional Analyses --------------------------------------##
##-----------------------------------------------------------------------## 
#Note that you will need to have run setups from earlier sections to ensure
#These optional analyses will work
    
    switches.section5 = copy(false)
# EPA_Wildfire_Master.m:126
    if switches.section5:
        # Step 5a. Generate fuelbed histograms at one degree level
        EPA_Wildfire_Fuelbed_OneDeg
        # Step 5b. Test NETCDF files sent to us by Christof
        EPA_Wildfire_TestNETCDF
    