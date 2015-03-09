import vtk
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
reader = vtk.vtkMPASReader()
reader.SetFileName('MPASReader.nc')
# Have reader examine what information is available
reader.UpdateInformation()
# Print out available arrays
for i in range(reader.GetNumberOfCellArrays()):
    print reader.GetCellArrayName(i)
# Don't read in the ke cell data array
reader.SetCellArrayStatus('ke', 0)
reader.Update()

# Wrap the reader output to make simplify access
wrappedreader = dsa.WrapDataObject(reader.GetOutput())
print wrappedreader.PointData.keys()
print wrappedreader.CellData['vorticity']
vorticity = wrappedreader.CellData['vorticity']
# Perform some operations on the data
wrappedreader.CellData.append(vorticity + 1, 'vorticity plus one')
print algs.max(vorticity)
print algs.max(wrappedreader.CellData['vorticity plus one'])

