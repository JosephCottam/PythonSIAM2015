import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
# Create a dataset
w = vtk.vtkRTAnalyticSource()
t = vtk.vtkDataSetTriangleFilter()
t.SetInputConnection(w.GetOutputPort())
t.Update()
# Compute gradient of RTData array
ugrid = dsa.WrapDataObject(t.GetOutput())
print algs.gradient(ugrid.PointData['RTData'])
