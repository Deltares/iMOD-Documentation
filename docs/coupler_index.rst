************
iMOD Coupler
************

=====================
Coupling to MODFLOW 6
=====================

Deltares have worked together with the USGS to create the `MODFLOW API
<https://www.sciencedirect.com/science/article/pii/S1364815221002991>`_ , based
on the `Basic Model Interface (BMI)
<https://bmi-spec.readthedocs.io/en/latest/>`_ with some extensions. The first
version of this functionality became available with the release of MODFLOW
6.2.0. BMI is a set of standard control and query functions that, when added to
a model code, make that model both easier to learn and easier to couple with
other software elements. Furthermore, the BMI makes it possible to control
MODFLOW 6 execution from scripting languages using bindings for the BMI.

We have also developed `xmipy <https://github.com/Deltares/xmipy>`_, a Python
package with bindings for the API, which allow you to run and update (at
runtime) a MODFLOW 6 model from Python. This allows coupling MODFLOW 6 to other
computational cores. One of its first applications is a coupling of MODFLOW 6 to
MetaSWAP, as part of the 
`iMOD Coupler <https://github.com/Deltares/imod_coupler>`_ 
package. Other applications can be found in `this paper.
<https://www.sciencedirect.com/science/article/pii/S1364815221002991>`_

===========
Source Code
===========
The developments on ``xmipy`` can be found on:
https://github.com/Deltares/xmipy 

The example of ``imod_coupler`` with the coupling between MODFLOW 6 and the
unsaturated zone model MetaSWAP can be found on:
https://github.com/Deltares/imod_coupler 

============
Known Issues
============
When using the imod_coupler an file error can occur on the dll of the kernel 
(for example MODFLOW 6 or MetaSWAP). The following error can occur: *'FileNotFoundError: Could not find 
module "\path\to\MetaSWAP.dll" (or one of its dependencies).
Try using the full path with constructor syntax.'* 

This is caused by not having the Intel redistrutable libraries on the system. 
They can be installed from https://software.intel.com/content/www/us/en/develop/articles/intel-compilers-redistributable-libraries-by-version.html. 
Make sure to choose the correct platform and the version for 'Parallel Studio XE 2020'. 
