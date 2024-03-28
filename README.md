# STEC: Spatial-Temporal Embodied Carbon Models for Embodied Carbon Accounting of Computer Systems
STEC is a new spatial-temporal embodied carbon model for embodied carbon accounting. 


## Getting Started
The code is built on Python 3.7.7 and no special packages are required.
### STEC-CD
`STEC-CD.py` can provide the daily embodied carbon accounting for hardware. To run `STEC-DE.py`, you need input: (a) The data of product manufacturing in the format: 01.01.2021-31.12.2021 (b) The location of product manufacturing in the format: IT, IE, US, TW, KR. (c) The haredware type: Processor, Storage, Memory. 
### STEC-CS
`STEC-CS.py` can provide the monthly embodied carbon accounting for hardware. To run `STEC-DE.py`, you need input: (a) The data of product manufacturing in the format: 2019/1/1-2022/12/1 (b) The location of product manufacturing in the format: CN, IT, IE, US, TW, KR. (c) The haredware type: Processor, Storage, Memory. 
### STEC-ZY
`STEC-ZY.py` can provide the monthly embodied carbon accounting for hardware. To run `STEC-DE.py`, you need input: (a) The data of product manufacturing in the format: 2019-2021 (b) The location of product manufacturing in the format: EU, ASEAN. (c) The haredware type: Processor, Storage, Memory. 
 
## Data description
In STEC, the data can be categorized into electricity data and hardware-related data.
### Hardware-related data
The hardware-related data contains Electricity consumed per die Size (EPS), Carbon emission from Gas used per die Size (GPS), Carbon emission from Material used per die Size (MPS), Bit density for memory (BD), and Electricity consumed per GB (EPG).  
| Hardware type   | Paremeters | Source |
|:----------------:|:-------------:|:-------------:|
|   Processor  | EPS, GPS, MPS       | [Research paper, ](https://doi.org/10.1109/IEDM13553.2020.9372004) [Industrial research reports](https://link.springer.com/book/10.1007/978-1-4419-9988-7)     | 
| Storage |  EPG          | [LCA reports](https://www.seagate.com/gb/en/esg/planet/product-sustainability/)       | 
|   Memory  | EPS, BD    |  [Industrial research reports](https://www.flashmemorysummit.com/English/Collaterals/Proceedings/2017/20170808_FR12_Choe.pdf)       | 

### Electricity data
Along the temporal dimension, the carbon intensity of electricity has granularity on day-level, season-level, and year-level. 
| Data granularity  | Source |
|:----------------:| :-------------:|
|   Daily | [ElectricityMaps](https://app.electricitymaps.com/map), [ENTSOE](https://transparency.entsoe.eu/dashboard/show?loggedUserIsPrivileged=false)  |
| Monthly     |  [EMBIR](https://ember-climate.org/countries-and-regions/) |
|   Yearly   |   [Our Word in Data](https://ourworldindata.org/grapher/carbon-intensity-electricity?tab=chart)  |
