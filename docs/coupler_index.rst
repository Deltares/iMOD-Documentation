*********************
Coupling to MODFLOW 6
*********************

In collabortion between the USGS and Deltares BMI is supported in MODFLOW 6
from the release of MODFLOW 6.2.0. BMI is a set of standard control and
query functions that, when added to a model code, make that model 
both easier to learn and easier to couple with other software elements. 
Furthermore, the BMI makes it possible to control MODFLOW 6 execution 
from scripting languages using bindings for the BMI.

xmipy is a python package with a generic bindings witch can be used to couple different
computational cores. xmipy is an extention to the existing bmipy. The extended interface is required to couple certain
hydrological kernels, particularly MODFLOW 6. Currently it is a joint 
development of the USGS and Deltares. The imod_coupler <https://github.com/Deltares/imod_coupler> uses it, for example, 
to couple Modflow 6 and MetaSWAP.

===========
Source Code
===========
The developments on xmipy can be found on:
https://github.com/Deltares/xmipy 