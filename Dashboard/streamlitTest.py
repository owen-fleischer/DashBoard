import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from streamlit_autorefresh import st_autorefresh


# Data This is where the logic for processing data will go, Might want a seperate file for actual data analysis such as finding standard Dev and avgs.
# That would allow for the data to not get processed multiple times everytime a change occurs on the page. Maybe everytime night at midnight.



dateTime = dt.datetime.now()
dateTime = str(dateTime.strftime("%Y-%m-%d %H:%M:%S"))

Devices = 5000
NonReporting = 400
OpenDeactReqs = 40
MultiMar = 0
PingsNotMar = 3000
OpenRestMode = 100
SoldDispEquip = 300
# Booleans used for status checks
TeleStatCheck = True
DevicesCheck = NonReportingCheck = OpenDeactReqsCheck = MultiMarCheck = PingsNotMarCheck = OpenRestModeCheck = SoldDispEquipCheck = True
if DevicesCheck == False or NonReportingCheck == False or OpenDeactReqsCheck == False or MultiMarCheck == False or PingsNotMarCheck == False or OpenRestModeCheck == False or SoldDispEquipCheck == False:
    TeleStatCheck = False

# These will need to be checked, for now they are always true
Lojack = True
TrackUnit = True
ZTR = True
TeleDataCheck = True

if Lojack == False or TrackUnit == False or ZTR == False:
    TeleDataCheck = False


# for now just setting this to time, will have to make it update whenever it was last down. This may be impossible with Streamlit
lastDown = str(dateTime)

# DAL data - these will prob be averages then I will need to compare current data to avg and depending on results change the display
IBMPing = .0070
Redis = .0008
IBMDB2 = .05
Easycom = .4


# RM to VCr data
RMtoVCRTime = 2
transNumsRMVCR = 10000
numContractsRMVCR = 5000

RMtoVCRCheck = True


# App Layout
st.set_page_config(layout="wide")
st_autorefresh(interval=.25 * 60 * 1000, key="dataframerefresh") # In order for this to work you must save the code, not sure about the datafiles

st.markdown("<h1 style='text-align: center; color: white;'>UR Dashboard</h1>",
            unsafe_allow_html=True)
st.caption("Last Updated: " + str(dateTime))

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    teleStats = st.container()
    with teleStats:
        if TeleStatCheck == True:
            tsExpander = st.expander(":black[Telematic Statistics]")
        else:
             tsExpander = st.expander(":red[Telematic Statistics]")
        with tsExpander:
                st.text("Devices: "+str(Devices))
                st.text("Non-Reporting Devices: " + str(NonReporting))
                st.text("Open Deactivation Requests: " + str(OpenDeactReqs))
                st.text("Multi-Marriages to single EQP#: "+str(MultiMar))
                st.text("Pinging/Not Married: " + str(PingsNotMar))
                st.text("Open Restricted Mode Chq Requ: "+str(OpenRestMode))
                st.text("Sold and Disposed Equipment: " + str(SoldDispEquip))

with col2:
    teleData = st.container()
    with teleData:
        if TeleDataCheck == True:

            TDExpander = st.expander(":black[Telematic Data]", expanded=False)
        elif TeleDataCheck == False:

            TDExpander = st.expander(":red[Telematic Data]")
        with TDExpander:
            if(Lojack == True):
                st.text("Lojack Feed: Normal-" +
                        str(dateTime))
            if(Lojack == False):  # Where logic will go if lojack is abnormal
                msg = str(dateTime.strftime("%Y-%m-%d %H:%M:%S"))
                st.markdown(
                    "<b style='text-align: center; color: red;'> Lojack Feed: Abnormal</b>", unsafe_allow_html=True)
                st.caption("Time reported: " + msg)

            if(TrackUnit == True):
                st.text("TrackUnit Feed: Normal-" +
                        str(dateTime))
            if(TrackUnit == False):  # Where logic will go if lojack is abnormal
                msg = str(dateTime)
                st.markdown(
                    "<b style='text-align: center; color: red;'> TrackUnit Feed: Abnormal</b>", unsafe_allow_html=True)
                st.caption("Time reported: " + msg)

            if(ZTR == True):
                st.text("ZTR OneiFeed: All Active: " +
                        str(dateTime))
            if(ZTR == False):  # Where logic will go if lojack is abnormal
                msg = str(dateTime)
                st.markdown(
                    "<b style='text-align: center; color: red;'> ZTR OneiFeed: Abnormal</b>", unsafe_allow_html=True)
                st.caption("Time reported: " + msg)
            st.text("Last Down: " + lastDown)
            # just copioed what was on current DBs
            st.text("Vendors Affected: ZTR")
            # same as prev.
            st.text("GPSSTGFL Feed: Started - " + str(dateTime))

with col3:
    dal = st.container()
    with dal:
        with st.expander(":black[DAL]", expanded=False):
           # st.markdown("<h2 style='text-align: left; color: black;'>DAL</h2>", unsafe_allow_html = True)
            st.text("IBM i Ping: " + str(IBMPing))
            st.text("IBT i Last Alert|Recovery: ")
            st.text("Redis Check: " + str(Redis))
            st.text("Redis Last Alert|Recovery: ")
            st.text("IBMi DB2 Last Alert|Recovery: " + str(IBMDB2))
            st.text("Easycom Check: ")
            st.text("Easycom Last Alert|Recovery: " + str(Easycom))


col4, col5, col6 = st.columns(3, gap="large")


with col4:
    RMtoVCR = st.container()
    with RMtoVCR:
        # can create a logic statement that changes the color here to red if their is an issue with one of the datapoints

        if RMtoVCRCheck ==True:
            RMtoVCRExpander = st.expander(":black[RM to VCR]")
        else:
            RMtoVCRExpander = st.expander(":red[RM to VCR]")
        with RMtoVCRExpander: 
            st.text("Average Time of RM to VCR: " + str(RMtoVCRTime))
            st.text("Transactions from RM to VCR: " + str(transNumsRMVCR))
            st.text("Contracts from RM to VCR: " + str(numContractsRMVCR))
