# Example of VTK array to NumPy
import vtk
vtkarray = vtk.vtkDoubleArray()
vtkarray.InsertNextValue(1)
vtkarray.InsertNextValue(2)
from vtk.util.numpy_support import vtk_to_numpy
numpyarray = vtk_to_numpy(vtkarray)
