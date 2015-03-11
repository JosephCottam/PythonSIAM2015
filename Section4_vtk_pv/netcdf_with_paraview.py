from paraview.simple import *
reader = NetCDFMPASreader(FileName='MPASReader.nc')
# Get information about what's in the file
reader.UpdatePipelineInformation()
print reader.PointArrayStatus
print reader.TimestepValues
# Reader in only some of the arrays
reader.PointArrayStatus = ['latCell', 'lonCell', 'xCell', 'nEdgesOnCell', 'areaCell']
# Read in the requested data
reader.UpdatePipeline()
# Change time steps
animation = GetAnimationScene()
animation.GoToLast()
animation.GoToPrevious()
