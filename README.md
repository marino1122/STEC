# STEC: Spatial-Temporal Embodied Carbon Models for Embodied Carbon Accounting of Computer Systems
STEC is a new spatial-temporal embodied carbon model for embodied carbon accounting. 
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

## STEC Models Set
To serve different applications, STEC models are classified by different spatical and temporal granularity, e.g., country-level and day-level (CD), country-level and season-level (CS), and treaty-zone-level and year-level (ZY).
|   Model  | Input | 
|:----------------:|:-------------:|
| STEC-CD |      Hardware-related data +  Daily electricity data  | 
|  STEC-CS  |    Hardware-related data +  Monthly electricity data   | 
|  STEC-ZY  |    Hardware-related data +  Yearly electricity data   | 

## Getting Started 
...
