---
title: "Get and Set Scene Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Scene_Properties_Example_VB.htm"
---

# Get and Set Scene Properties Example (VBA)

This example shows how to get a model's scene and get and set some scene properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
Option Explicit
 Dim Scene As SldWorks.swScene
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swConfig As SldWorks.Configuration
 Dim swPoint  As SldWorks.MathPoint
 Dim swVector As SldWorks.MathVector
 Dim point As Variant
 Dim vect As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
    Set swConfig = swModel.GetActiveConfiguration
     Debug.Print "Configuration: " & swConfig.name

    Set Scene = swConfig.GetScene
    Dim P2SFilename As String
     Scene.GetP2SFileName P2SFilename
     Debug.Print "Scene file: " & P2SFilename

    Debug.Print "Scene background top gradient color: " & Scene.BackgroundTopGradientColor
     Debug.Print "Scene background bottom gradient color: " & Scene.BackgroundBottomGradientColor

    Scene.GetFloorNormal swPoint, swVector
     point = swPoint.ArrayData
     Debug.Print "Scene floor normal point: " & point(0) & ", " & point(1) & ", " & point(2)
     vect = swVector.ArrayData
     Debug.Print "Scene floor normal vector: " & vect(0) & ", " & vect(1) & ", " & vect(2)

    Scene.BackgroundType = swSceneBackgroundType_e.swBackgroundType_UseEnvironment
     Debug.Print "Type of scene background as defined in swSceneBackgroundType_e: " & Scene.BackgroundType
     Debug.Print "Scene background environment image file: " & Scene.BackgroundEnvImage
     Debug.Print "Scene background image file: " & Scene.BackgroundImage
     Debug.Print "Scene environment rotation: " & Scene.EnvironmentRotation
     Scene.FitToSWWindow = True
     Debug.Print "Stretch to fit in SOLIDWORKS Design window? " & Scene.FitToSWWindow
     Debug.Print "Scale the scene floor uniformly? " & Scene.FixedAspectRatio
     Debug.Print "Flip the scene floor direction? " & Scene.FloorDirection
     Debug.Print "Automatically resize the scene floor based on the model bounding box? " & Scene.FloorAutoSize
     Debug.Print "Distance between scene floor and model: " & Scene.FloorOffset
     Debug.Print "Flip the scene floor offset direction? " & Scene.FloorOffsetDirection
     Scene.FloorReflections = True
     Debug.Print "Show model reflections on the scene floor? " & Scene.FloorReflections
     Debug.Print "Scene floor rotation: " & Scene.FloorRotation
     Debug.Print "Show model shadows on the scene floor? " & Scene.FloorShadows
     Debug.Print "Keep the scene background when changing the scene? " & Scene.KeepBackground
     Scene.FlattenFloor = True
     Debug.Print "Flatten the scene floor of the spherical environment? " & Scene.FlattenFloor
     Debug.Print "Horizon height: " & Scene.HorizonHeight
     Debug.Print "Environment size: " & Scene.EnvironmentSize

End Sub
```
