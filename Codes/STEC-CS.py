# -*- coding: utf-8 -*-
"""
"""
import pandas as pd


#define the path of dataset
Elec_month_path = "Monthly.csv"
Processor_path = "Processor.csv"
Memory_path = "Memory.csv"
Storage_path = "Storage.csv"


#load dataset
Elec_month = pd.read_csv(Elec_month_path, header=0,index_col=0)
Processor = pd.read_csv(Processor_path, header=0,index_col=0)
Memory = pd.read_csv(Memory_path, header=0,index_col=0)
Storage = pd.read_csv(Storage_path, header=0,index_col=1)

time = input ("Please input the manufacturing time (supported input: 2019/1/1-2022/12/1): ")
location = input ("Please input the manufacturing location \n Support input: IE, IT, US, TW, KR:")  
haredware_type = input ("Please input the hardware type (supported input: Processor, Memory, Storage): ")
tech = input ("Please input the technology type from the following.\
\n*****************************************************************************************\
\nFor processor: 3nm, 5nm, 7nm, 7-EUV, 7-EUV-DP, 10nm, 14nm, 20nm, 28nm.\
\nFor memory: LPDDR4, 10nm DDR4, 20nm LPDDR3, 30nm LPDDR3.\nFor storage: Nytro 3530, Nytro 1551, Nytro 3331,\
Nytro 3332, BarraCuda 120 SSD, EXOS X20, EXOS X18, Exos 2X14, Exos 7E8, Exos 5E8, Exos 10E2400, EXOS 15E900, \
Exos X16, Exos X12, BarraCuda 3.5, BarraCuda, BarraCuda Pro, FireCuda, IronWolf, IronWolf Pro, Skyhawk 3 TB,\
Skyhawk Surveillance HDD, Skyhawk 6 TB, Video 3.5 HDD, Video 3.5 HDD (Pipeline HDD), ULTRA TOUCH, Rugged Mini.\
\n*****************************************************************************************\
\nPlease input: ")


try:
    CI= Elec_month.loc[time][location]   
    if haredware_type == "Processor":
        Em_processor = float(Processor.loc[tech]['EPS (kWh/cm2)']) * CI + float(Processor.loc[tech]['EPS (kWh/cm2)'])  +  float(Processor.loc[tech]['EPS (kWh/cm2)']) 
        print("The meobdied carbon of this processor is " + str(round(Em_processor,2)) + " g/cm2.")
        
    ### estimate memory
    elif haredware_type == "Memory":
        if tech == "LPDDR4":
            Em_memory = float(Memory.loc[tech]['Embodied Carbon (g/GB)']) - float(Memory.loc[tech]['Carbon Emissions from Electricity Consumption (g/GB)']) + float(Processor.loc['10nm']['EPS (kWh/cm2)']) / 100 / float(Memory.loc[tech]['Bit Density (G/mm2)']) * CI
    
    
        elif tech == "10nm DDR4":
            Em_memory = float(Memory.loc[tech]['Embodied Carbon (g/GB)']) - float(Memory.loc[tech]['Carbon Emissions from Electricity Consumption (g/GB)']) + float(Processor.loc['10nm']['EPS (kWh/cm2)']) / 100 / float(Memory.loc[tech]['Bit Density (G/mm2)'])* CI
            
        elif tech == "20nm LPDDR3":
            Em_memory = float(Memory.loc[tech]['Embodied Carbon (g/GB)']) - float(Memory.loc[tech]['Carbon Emissions from Electricity Consumption (g/GB)']) + float(Processor.loc['20nm']['EPS (kWh/cm2)']) / 100 / float(Memory.loc[tech]['Bit Density (G/mm2)']) * CI
            
    
        elif tech == "30nm LPDDR3":
            Em_memory = float(Memory.loc[tech]['Embodied Carbon (g/GB)']) - float(Memory.loc[tech]['Carbon Emissions from Electricity Consumption (g/GB)']) + float(Processor.loc['28nm']['EPS (kWh/cm2)']) / 100 / float(Memory.loc[tech]['Bit Density (G/mm2)']) * CI
    
        print("The meobdied carbon of this memory is " + str(round(Em_memory,2)) + " g/GB.")
        
    
    ### estimate storage
    elif haredware_type == "Storage":
        
        Em_storage = float(Storage.loc[tech]['Embodied Carbon (g/GB)']) / 448 * CI + float(Storage.loc[tech]['Other Carbon (g/GB)'])    # 448 is the average carbon in g/GB
        print("The meobdied carbon of this storage is " + str(round(Em_storage,2)) + " g/GB.")
    

except:
    print("Wrong input!!!")















