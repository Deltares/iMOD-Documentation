###########
iMOD
###########

The iMOD suite provides tools to efficiently build and visualize
groundwater models. 

Deltares is working to integrate and improve our groundwater software. 
Therefore iMOD is extended with a new iMOD Suite to link to the latest 
developments on the MODFLOW and on the changing requirements in the field 
of groundwatermodelling. Important technological innovations will be developed 
in the new iMOD Suite. iMOD5 combines the proven technology and the experience 
of for groundwatermodelling simulations and visualisation. 

This Suite include different modules with supports modelling with 
MODFLOW 6, including unstructured meshes, visualisation in QGIS with 
a smart and fast plugin and 3D viewer, and a python package for transparent and 
reproducible modelling process. 

The proven technology and expertise of iMOD is consolidated in the 
iMOD5 suite. iMOD5 supports structured calculations with MODFLOW2005
and MODFLOW6 and can be coupled to the unsaturated zone model MetaSWAP. 
The model input and output can be visualised in the fast interactive viewer. 

.. image:: screenshots/index/overview.png

--------
iMOD Suite
--------
It currently consists of three modules:

* iMOD QGIS Plugin
  QGIS plugin for visualisation of model input and output with tool for 
  cross-sections, timeseries and link to the 3D viewer. Supports NetCDF, UGRID 
  and ipf's.
* iMOD 3D Viewer
  3D Viewer for interactive 3D visualisation of input and output. Supports UGRID 
  file format.
* iMOD python 
  An Python package to support MODFLOW groundwater modeling. It makes it easy 
  to go from your raw data to a fully defined MODFLOW model, with the aim 
  to make this process reproducable.
  Supports:
  * USGS MODFLOW 6, structured and unstructerd grids, no advanced stress packages yet (LAK, MAW, SFR, UZF)
  * iMODFLOW (iMOD5) 
  * iMOD-WQ (iMOD5), which integrates SEAWAT (density-dependent groundwater flow) and MT3DMS (multi-species reactive transport calculations)

--------
iMOD5 
--------

https://oss.deltares.nl/nl/web/imod 



--------
Sections
--------

.. toctree::
   :titlesonly:

   qgis_index
   viewer_index
   python_index