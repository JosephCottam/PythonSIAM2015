Python @ SIAM 2015
=================

Links to the static materials:
- [Section 0](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section0_intro.ipynb) Introduction
- [Section 1-1](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section1-1_ipython.ipynb) ipython
- [Section 1-2](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section1-2_matplotlib.ipynb) matplotlib
- [Section 2](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section2_numpy_scipy_pandas.ipynb) numpy, scipy, pandas
- [Section 3-1](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section3-1_blaze.ipynb) blaze
- [Section 3-2](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section3-2_bokeh.ipynb) bokeh
- [Section 4](https://github.com/JosephCottam/PythonSIAM2015/blob/master/VTK_PV.pdf?raw=true) VTK, ParaView

All notebooks have been created in 2.7 Python. The virtual machine has
latest Anaconda Python and latest ParaView/VTK, as of March 12, 2015.

Interactively following along in the tutorial
---------------------------------------------

The above links allow you to follow along in a web browser, but it will
be unable to run any of the code. To have a live system that has
interaction, follow the steps below.

Our setup involves using a virtual machine (VM) to ease the process
because everything will be prepackaged right from the start,
and launched after you start the VM. We will have copies of the VM
on USB drives, or you can download the VM directly from the web.

*The virtual machine is available at:
 https://drive.google.com/file/d/0BzyiUoirucJpTTB6WnNDV00wY0k/view?usp=sharing*

*Virtualbox software download link is at:
 https://www.virtualbox.org/wiki/Downloads*

We will provide VirtualBox to be able to run the virtual machine,
on-site at SIAM, (or you can download it directly from Oracle)
but other virtualization systems (VMWare, libvirt/qemu, etc.) should
be able to run the images. The virtual machine is packaged in a OVA
(Open Virtualization Format) for easy installation on your machine.

Step One: Install VirtualBox
----------------------------

Install VirtualBox on your computer. We will have copies of installers
available on-site, or download it directly from the link below.

*Virtualbox software download link is at:
 https://www.virtualbox.org/wiki/Downloads*

*We are running a 64-bit Linux on the VM, which should work even if
 you are running a 32-bit OS, as long as you have a modern 64-bit
 processor.*

Open the installer and go through the default installation to install
VirtualBox on your computer.

If you have trouble installing, at this point, please use the above
links and follow along in a web browser.


Step Two: Open the Virtual Machine
-----------------------------------------

Copy pyvis_siam_2015.ova from USB drives available on-site at SIAM or download
it from the link below.

*The virtual machine is available at:
 https://drive.google.com/file/d/0BzyiUoirucJpTTB6WnNDV00wY0k/view?usp=sharing*

Start VirtualBox, and in the main menu, go to "File->Import Appliance"

Open the "pyvis_siam_2015.ova" that is provided. Continue through the
default options for the virtual machine.

This will unpack and install the virtual machine on your computer.

If you have trouble installing, at this point, please use the above
links and follow along in a web browser.


Step Three: Launch the Virtual Machine
--------------------------------------

In VirtualBox, in the virtual machine lists, open the new virtual
machine.  This will start Arch Linux in a virtual machine on your computer.

It will automatically launch into an graphical session with two open
terminals and a ipython notebook session.

In case you happen to need it, the default user is "pyvis" with a
password of "pyvis". It has sudo access, and the root password is "pyvis".

If you have trouble installing, at this point, please use the above
links and follow along in a web browser.


Step Four: You're Ready!
------------------------

If all went well, a window should have launched in the browser on the VM,
showing the ipython notebook interface.

If you have trouble installing, at this point, please use the above
links and follow along in a web browser.


Alternatively, install on your computer without VM
--------------------------------------------------

Alternatively, if you can't get the VM to work, you can download
Anaconda, ParaView, VTK & the materials:

[Tutorial Materials](https://github.com/JosephCottam/PythonSIAM2015/archive/master.zip) https://github.com/JosephCottam/PythonSIAM2015/archive/master.zip
[Anaconda Python](http://continuum.io/downloads) http://continuum.io/downloads
[ParaView](http://www.paraview.org/download/) http://www.paraview.org/download/
[VTK](http://www.vtk.org/VTK/resources/software.html) http://www.vtk.org/VTK/resources/software.html

