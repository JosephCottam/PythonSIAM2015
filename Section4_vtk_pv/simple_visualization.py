from paraview.simple import *

# Create a cone
myCone = Cone()

# Get documentation on cone and its properties
help(myCone)

# Examine a property
myCone.Center

# Change a property
myCone.Center = [0,0,1]

# Show the result
Show(myCone)
Render()
# Apply a filter
myClip = Clip()

# Show the result
Show(myClip)
Render()
# Forgot to hide the cone
Hide(myCone)
Render()
# Change camera
cam = GetActiveCamera()
cam.GetPosition()
cam.SetPosition(-1,0,2.5)
Render()
