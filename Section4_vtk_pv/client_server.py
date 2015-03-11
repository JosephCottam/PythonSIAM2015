from paraview.simple import *
Connect('localhost')
s = Sphere()
pid = ProcessIdScalars()
Show()
Render()
