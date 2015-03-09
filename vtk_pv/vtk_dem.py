# Step 1 - Creating the Display
# First thing first
import vtk
# Make a window on our display
renwin = vtk.vtkRenderWindow()
# Define the size of the initial window
renwin.SetSize(500,500)
# Create a renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground2(1,1,1)
renderer.SetGradientBackground(1)
# Create an interactor
iren = vtk.vtkRenderWindowInteractor()
# Add the renderer to the render window
renwin.AddRenderer(renderer)
# Set the interactor to the render window
renwin.SetInteractor(iren)
# Show the (empty) window
renwin.Render()

# Step 1b - Enabling interactions
# Initialize the interactor
iren.Initialize()
# Update the rendering pipeline
renwin.Render()
# Start the UI event loop
iren.Start()

# Step 2 - Read the DEM file
# Creating a reader
reader = vtk.vtkDataSetReader()
filename = "SaintHelens.vtk"
reader.SetFileName(filename)
# Updating the pipeline
reader.Update()
# Printing information about the output of the reader
id = reader.GetOutput()
print(id.GetClassName())
print(id.GetBounds())
print id.GetPointData().GetArray(0).GetRange()

# Step 3 - Creating the mapper
# Create the mapper
mapper = vtk.vtkDataSetMapper()
# Set the visisbility on the scalar
mapper.ScalarVisibilityOn()
# Set the scalar range to have a nice blue-red range
mapper.SetScalarRange(682.0, 2543.0)
# Connect the mapper to the reader
mapper.SetInputConnection(reader.GetOutputPort())

# Step 4 - Creating the Actor
# Create the actor
actor = vtk.vtkActor()
# Sets the mapper to the actor
actor.SetMapper(mapper)
# Add the actor to the renderer
renderer.AddViewProp(actor)
# Perform rendering
renwin.Render()
# Center the camera to see the full scene
renderer.ResetCamera()
# Final rendering
renwin.Render()

# Step 5 - Elevating our surface to 3D
# We elevate the surface with the vtkWarpScalarFilter
warp = vtk.vtkWarpScalar()
# Connect the filter to the reader
warp.SetInputConnection(reader.GetOutputPort())
# Update the pipeline
warp.Update()
print(warp.GetOutput().GetBounds())

# Show the elevated surface
mapper.SetInputConnection(warp.GetOutputPort())
renwin.Render()
renderer.ResetCamera()
renwin.Render()

# Step 5b - Drawing iso-surfaces
# Draw the iso-surface
isosurface = vtk.vtkContourFilter()
# Generate 10 iso-surfaces along the elevation
isosurface.GenerateValues(10,682.0,2543.0);
# Connect the filter to the reader
isosurface.SetInputConnection(warp.GetOutputPort())
# Update the pipeline
isosurface.Update()
mapper.SetInputConnection(isosurface.GetOutputPort())
renwin.Render()
renderer.ResetCamera()
renwin.Render()

# Step 6 - Exercise - Display iso-surface and data
# Render everything into one
mapper.SetInputConnection(warp.GetOutputPort())
# Create a new mapper
mapperiso = vtk.vtkDataSetMapper()
mapperiso.SetInputConnection(isosurface.GetOutputPort())
# Create the actor
actoriso = vtk.vtkActor()
actoriso.SetMapper(mapperiso)
# Disable the scalar coloring
mapperiso.ScalarVisibilityOff()
# Set the color to black
actoriso.GetProperty().SetColor(0,0,0)
# Set the line width larger
actoriso.GetProperty().SetLineWidth(2)
# add the actor to the rendering
renderer.AddViewProp(actoriso)

# Step 7 - Clipping the data
# Remove first the iso actor
renderer.RemoveViewProp(actoriso)
# Clip the data
cf = vtk.vtkClipDataSet()
# Set the clipping plane
plane = vtk.vtkPlane()
cf.SetClipFunction(plane)
print plane
# Set the plane origin
plane.SetOrigin(560000,5120000,2000)
# Connect the pipeline
cf.SetInputConnection(warp.GetOutputPort())
mapper.SetInputConnection(cf.GetOutputPort())

# Step 8 - Clipping Widget interaction
# Creates an implicit plane widget
widget = vtk.vtkImplicitPlaneWidget()
widget.PlaceWidget(warp.GetOutput().GetBounds())
widget.SetOrigin([plane.GetOrigin()[x] for x in 0,1,2])
widget.SetNormal([plane.GetNormal()[x] for x in 0,1,2])
widget.SetInteractor(iren)
# Connects the interaction event to the plane
def cb(obj,event):
     global plane
     obj.GetPlane(plane)
widget.AddObserver("InteractionEvent", cb)
widget.SetEnabled(1)
widget.DrawPlaneOn()
widget.TubingOn()
renwin.Render()
