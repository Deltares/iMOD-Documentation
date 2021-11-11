###########
iMOD
###########

The iMOD suite provides tools to efficiently build and visualize
groundwater models. 

Deltares is working to integrate and improve our groundwater software. 
Therefore iMOD is extended with a new iMOD Suite to link to the latest 
developments on the MODFLOW and on the changing requirements in the field 
of groundwatermodelling, most pressing currently the support 
of unstructured grids. 

Therefore we created the new iMOD Suite to aid pre- and post-processing
unstructured groundwater models. 
Furthermore, a second goal of this suite was to better connect to
the latest developments in the data science ecosystem, by utilizing:

* Existing data format conventions (NetCDF, UGRID) instead of 
  developing new ones, allowing more user flexibility to find the right
  tools for the right job.
* Widely used and tested software (QGIS) to which we add our extension, 
  instead of creating complete programs ourselves.
* Modern programming languages (C++ and Python) that 
  allow connecting to a big and lively software ecoystem.

Important technological innovations will be developed 
in the new iMOD Suite, whereas iMOD 5 will be maintained the coming years, 
because of its proven technology
for groundwatermodelling simulations and visualisation, 
but will see no big new feature developments.

The iMOD Suite offers different modules which support modelling with 
MODFLOW 6 (including unstructured meshes), visualisation in QGIS, 
a brand-new 3D viewer, and a python package for a transparent and 
reproducible modelling workflow. 

.. figure:: screenshots/index/NHI-zz_cross-section.png

  Easy plotting of 4 dimensional [t, z, y, x] data in the iMOD QGIS plugin.
  The example shows the chlorine concentrations computed 
  by the `NHI fresh-salt model 
  <https://gitlab.com/deltares/imod/nhi-fresh-salt>`_.

.. figure:: screenshots/index/NHI-zz_3d_viewer.png

  The chlorine concentrations computed by the NHI-fresh-salt model.
  for the province of Zeeland, plotted in the new iMOD 3D viewer. 
  The top layer is made opaque, 
  creating the pretty mist effect in the creek ridges.

The proven technology and expertise of iMOD is consolidated within 
iMOD 5. iMOD 5 supports structured calculations with MODFLOW2005
and structured MODFLOW6 and can be coupled to the unsaturated zone 
model MetaSWAP. 
The model input and output can be visualised in the fast interactive viewer. 
`The documentation of iMOD 5 can be found here 
<https://oss.deltares.nl/nl/web/imod>`_
.

.. list-table:: Comparison between iMOD Suite & iMOD 5
  :header-rows: 1
  :stub-columns: 1

  * - 
    - iMOD Suite
    - iMOD 5
  * - computational kernels
    - Modflow 2005, Modflow 6, SEAWAT, MT3DMS
    - Modflow 2005, Modflow 6, SEAWAT, MT3DMS, MetaSWAP
  * - file types
    - NetCDF, UGRID, shp, tiff, idf, ipf, gen
    - idf, ipf, isg, gen
  * - grid types
    - structured & unstructured
    - structured & nested structured
  * - scripted pre-processing
    - iMOD python
    - iMOD Batch
  * - interactive pre-processing
    - (QGIS)
    - iMOD GUI
  * - scripted 2D plot
    - iMOD-python
    - 
  * - interactive 2D plot
    - iMOD QGIS plugin (& QGIS)
    - iMOD GUI
  * - scripted 3D plot
    - iMOD python
    -  
  * - interactive 3D plot
    - iMOD 3D viewer
    - iMOD GUI

The suite currently consists of three modules:

* :doc:`iMOD QGIS Plugin <qgis_index>`:
  QGIS plugin for visualisation of model input and output with tool for 
  cross-sections, timeseries and link to the 3D viewer. Supports NetCDF, UGRID 
  and ipf's.
* :doc:`iMOD 3D Viewer <viewer_index>`:
  A 3D Viewer for interactive 3D visualisation of unstructured input and output. Supports UGRID 
  file format.
* :doc:`iMOD python <python_index>`:
  An Python package to support MODFLOW groundwater modeling. It makes it easy 
  to go from your raw data to a fully defined MODFLOW model, with the aim 
  to make this process reproducable.
  Supports:

  * USGS MODFLOW 6, structured and unstructerd grids, 
    not all advanced stress packages yet (LAK, MAW, SFR), 
    and only the groundwater flow packages.
  * iMODFLOW (computational code provided with iMOD 5) 
  * iMOD-WQ (computational code provided with iMOD 5), 
    which integrates the SEAWAT (density-dependent groundwater flow) 
    and MT3DMS (multi-species reactive transport calculations)

*The following chapters further discuss the different components
of the iMOD Suite, as well as provide examples on how to use them.*

.. toctree::
   :titlesonly:

   qgis_index
   viewer_index
   python_index
   workflow_index
   further_links
