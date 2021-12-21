*********************
Coupling to MODFLOW 6
*********************

Deltares have worked together with the USGS to create the MODFLOW API, based on the
Basic Model Interface (BMI) with some extensions.
The first version of this functionality became available with the release of MODFLOW 6.2.0. 
BMI is a set of standard control and query functions that, when added to a model code, make that model
both easier to learn and easier to couple with other software elements.
Furthermore, the BMI makes it possible to control MODFLOW 6 execution
from scripting languages using bindings for the BMI.

We have also developed xmipy, a Python package with bindings for the API, which can be 
used to couple MODFLOW 6 to other computational cores. One of its first applications
is a coupling of MODFLOW 6 to MetaSWAP, as part of the imod_coupler package.

===========
Source Code
===========
The developments on xmipy can be found on:
https://github.com/Deltares/xmipy 

The example of imod_coupler with the coupling between MODFLOW 6 and the unsaturated
zone model MetaSWAP can be found on:
https://github.com/Deltares/imod_coupler 