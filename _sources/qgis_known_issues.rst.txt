
*************
Known Issues
*************

.. _plot_axis_off:

--------------
Plot axis off
--------------

In both the Time series widget as the Cross-section widget
a weird offset in the plot axis can occur when you use a multiple monitor setup.

.. figure:: screenshots/qgis_issues/plot_axis_offset.png

    Notice the y-axis being moved too high and 
    the x-axis being scaled weirdly.

So far we haven't been able to fix it in the code, 
so you can fix this as a user by either:

- Moving your QGIS application to the **main window** of your monitor setup
- In Windows, navigate to *Settings > Display* then under 
  *Rearrange your displays* select the monitor you want to view QGIS on, 
  and finally tick the box *Make this my main display*