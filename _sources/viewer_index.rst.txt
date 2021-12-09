**************
iMOD Viewer
**************

The iMOD Viewer consist of a standalone 3D viewer and a QGIS plugin. 

* The iMOD 3D Viewer is a 3D viewer for grids and datasets. 
  It supports IDF files, UGRID files and Grb.disu files that contain an unstructured layered grid.  
  The 3D Viewer also supports viewing some non-grid objects like IPF files and Shapefiles.

* The iMOD QGIS plugin aids exploring 4D geospatial data in QGIS.  
  The primary components are Timeseries and cross-section visualization, connecting to the 3D Viewer and  and visualisation of IPF files.
  
  Primary components are:
     * Connecting to the iMOD 3D viewer
     * Timeseries visualization
     * Cross-section visualization
     * Reading .IPF files
     * Easy viewing of NHI data


.. image:: screenshots/viewer_index/example-dommel.png
   :width: 600px

.. toctree::
   :hidden:
   :numbered:

   viewer_install
   qgis_user_manual
   3dviewer_user_manual
   qgis_known_issues
