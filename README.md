# pyAQIplot
plot AQI data (.csv files downloaded from [https://waqi.info/](https://waqi.info/))

## Usage
### load package
```
from AQIFrame import Frame
file = 'xxx_div\\yyy_filename.csv'
fm = Frame(file)
```
### one plot
```
fm.ind(title=r'PM$_{2.5}$', select=0, color_bar=True)
```
example:

<img src="https://github.com/Augus1999/pyAQIplot/blob/main/examples/Figure_1.png" width="400" alt="example 1"/>

### plot all
```
fm.gro(title='your title')
```
example:

<img src="https://github.com/Augus1999/pyAQIplot/blob/main/examples/Figure_2.png" width="400" alt="example 2"/>

### statistics
```
fm.data.statistics()
```
output is like:
```
Unit: day(s)
************************************************************
             PM2.5     PM10     O3     NO2     SO2     CO
[  0, 25 ]   27        127      377    1852    2258    1980
( 25, 50 ]   202       636      790    435     36      8
( 50, 75 ]   397       884      341    13      0       10
( 75, 100]   466       436      164    0       0       9
(100, 125]   373       142      74     0       0       2
(125, 150]   355       40       16     0       0       4
(150, 175]   344       16       2      0       0       4
(175, 200]   91        3        1      0       0       8
(200, 300]   43        9        0      0       0       32
(300, 400]   2         2        0      0       0       54
(400, +oo)   0         1        0      0       0       189
************************************************************
```
### settings
```
fm.settings()
```
