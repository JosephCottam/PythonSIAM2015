Python @ SIAM 2015 
=================

Links to the static notebooks:
- [Section 0](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section0_intro.ipynb) Introduction
- [Section 1-1](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section1-1_ipython.ipynb) ipython
- [Section 1-2](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section1-2_matplotlib.ipynb) matplotlib
- [Section 2](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section2_numpy_scipy_pandas.ipynb) numpy, scipy, pandas
- [Section 3](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section3_bokeh.ipynb) bokeh
- [Section 4](http://nbviewer.ipython.org/github/JosephCottam/PythonSIAM2015/blob/master/Section4_vtk.ipynb) VTK

All notebooks have been created in 2.7 Python.

Using Python for Visualization and Analysis 
------------------------------------------------------

Our setup involves using a virtual machine to ease the install process
because eveything will be prepackaged right from the start,
and launched after you start the VM.

We have provided VirtualBox to be able to run the virtual machine,
but other virtualization systems (VMWare, libvirt/qemu, etc.) should
be able to run the images. The virtual machine is packaged in a OVA
(Open Virtualization Format) for easy installation on your machine.

At the tutorial, we will provide instructions to view the static
web versions that we will be presenting, if you do not wish to install
the virtual machine and software.

*All materials (except for the VM) will be available afterwards on github at:
 http://github.com/JosephCottam/PythonSIAM2015*


Step One: Install VirtualBox
----------------------------

Several installers are provided for Win-64, Win-32, OSX-64, Ubuntu-64,
and Ubuntu-32. For other flavors of Linux, typically you can acquire
VirtualBox through the system's package manager, otherwise it can
be found at http://virtualbox.org

Open the installer and go through the default installation to install 
VirtualBox on your computer.


Step Two: Open the Virtual Machine
-----------------------------------------

Start VirtualBox, and in the main menu, go to "File->Import Appliance"

Open the "pyvis.ova" that is provided on this USB drive. Continue
through the default options for the virtual machine.

This will unpack and install the virtual machine on your computer.


Step Three: Launch the Virtual Machine
--------------------------------------

In VirtualBox, in the virtual machine lists, open the new "pyvis" virtual 
machine.  This will start Arch Linux in a virtual machine on your computer.

It will automatically launch into an graphical session with two open
terminals and a ipython notebook session.

In case you happen to need it, the default user is "pyvis" with a 
password of "pyvis". It has sudo access, and the root password is "pyvis".


Step Four: Copy the tutorial materials
--------------------------------------

Assuming you are connected to the internet, run "get-internet"
from the terminal, which should be open in one of the windows.

```
$ get-internet
```

In the case you are not connected to the internet or unable to download
the materials, we will have several USB sticks with the tutorial 
materials on hand.

In that case, after inserting the USB stick and mounting it in
the virtual machine, run "get-usb" from the terminal.

```
$ get-usb
```

If you happen to be running VirtualBox on a host Linux machine,
you may need to add yourself to the "vboxusers" group to allow the VM
to have USB access.

In both cases, they will copy the materials needed to continue with
the tutorial.


Step Five: You're Ready!
------------------------

If all went well, a window should have launched in the browser on the VM,
showing the ipython notebook interface.


Notes
-----

Contact Jon Woodring (woodring-at-lanl-dot-gov) if you would like a copy of the VM.
