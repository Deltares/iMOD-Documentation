
*************
Known Issues
*************

.. _plot_axis_off:

--------------
Plot axis off
--------------

In the QGIS plugin, 
a weird offset in the plot axis can occur when you use a multiple monitor setup.
Both the Time series widget as well as the Cross-section widget can suffer from this.

.. figure:: screenshots/qgis_issues/plot_axis_offset.png

    Notice the y-axis being moved too high and 
    the x-axis being scaled weirdly.

So far we haven't been able to fix it in the code, 
so you can fix this as a user by either:

- Moving your QGIS application to the **main window** of your monitor setup
- In Windows, navigate to *Settings > Display* then under 
  *Rearrange your displays* select the monitor you want to view QGIS on, 
  and finally tick the box *Make this my main display*

..
  Technical comment:
  This is due to a bug in PyQtgraph, which is difficult to fix.
  The proposed fix of PyQtgraph requires us to run specific python code before 
  the application starts, which is impossible to do for a plugin.
  https://pyqtgraph.readthedocs.io/en/latest/how_to_use.html#hidpi-displays
  Qt6 has better support for multiple model setups, so when QGIS migrates
  to Qt6, this shouldn't be an issue anymore.