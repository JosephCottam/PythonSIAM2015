# Example of NumPy to VTK array
import vtk
from vtk.util.numpy_support import numpy_to_vtk
import numpy
numpyarray = numpy.zeros(5)
vtkarray = numpy_to_vtk(numpyarray)
