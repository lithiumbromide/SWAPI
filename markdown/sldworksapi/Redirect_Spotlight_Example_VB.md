---
title: "Redirect Spotlight Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Redirect_Spotlight_Example_VB.htm"
---

# Redirect Spotlight Example (VBA)

This examples shows how select a spotlight and two sketch points. The spotlight is then redirected to point along a vector that is defined by the two points.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Adds a spotlight.
' 3. Inserts a 3D sketch.
' 4. Selects the spotlight.
' 5. Selects a new root point and direction point for the spotlight.
' 6. Gets the current position and direction of the spotlight.
' 7. Modifies the position and direction of the spotlight.
' 8. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swModelView As SldWorks.ModelView
    Dim swFeature As SldWorks.Feature
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSketchManager As SldWorks.SketchManager
    Dim swSketch As SldWorks.Sketch
    Dim swMath As SldWorks.MathUtility
    Dim swLightFeature As SldWorks.Feature
    Dim swLight As SldWorks.Light
    Dim selRootSkPt As SldWorks.SketchPoint
    Dim selDirSkPt As SldWorks.SketchPoint
    Dim swSketchTrans As SldWorks.MathTransform
    Dim ptArr(2) As Double
    Dim dirArr(2) As Double
    Dim rootPoint As SldWorks.MathPoint
    Dim dirPoint As SldWorks.MathPoint
    Dim dirVector As SldWorks.MathVector
    Dim params As Variant
    Dim skSegment As Object
    Dim status As Boolean
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
    Dim rect As Variant
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\appearances\usb_flash_drive1.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Add spotlight
    status = swModel.AddLightSource("SW#5", 2, "Spot1")
    status = swModel.SetLightSourcePropertyValuesVB("SW#5", 2, 0.5, 8454143, 1, -9.99999999999991E-02, 0.170000000000101, 1.10999999999999, 0.179999999999999, -9.00000000001008E-02, -1.02999999999999, 45, 0, 0, 0, 0.4, 0.4, 0, False)
    status = swModel.LockLightToModel(4, True)
    Set swModelView = swModel.ActiveView
    swModelView.GraphicsRedraw (rect)
```

```
    'Insert 3D sketch
    Set swSketchManager = swModel.SketchManager
    swSketchManager.Insert3DSketch True
    Set skSegment = swSketchManager.CreateLine(-0.038076, 0.043671, -0#, -0.01322, 0.054563, -0#)
    Set swSketch = swModel.GetActiveSketch2()
    status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0)
    Set skSegment = swSketchManager.CreateLine(-0.01322, 0.054563, -0#, -0.01322, 0.08124, 0.018547)
    Set swSketch = swModel.GetActiveSketch2()
    status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0)
    Set skSegment = swSketchManager.CreateLine(-0.01322, 0.08124, 0.018547, 0.000568, 0.08124, 0.004759)
    Set swSketch = swSketchManager.ActiveSketch
    status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    'Select the light
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    status = swModelDocExt.SelectByID2("Spot1", "LIGHTS", 0, 0, 0, False, 0, Nothing, 0)
    Set swLightFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swLight = swLightFeature.GetSpecificFeature2
```

```
    'Select a root point
    status = swModel.Extension.SelectByID2("Point3@3DSketch1", "EXTSKETCHPOINT", 0, 0, 0, False, 0, Nothing, 0)
    Set selRootSkPt = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = selRootSkPt.GetSketch
```

```
    'Need the sketch to model transform
    Set swMath = swApp.GetMathUtility
    Set swSketchTrans = swSketch.ModelToSketchTransform.Inverse
    ptArr(0) = selRootSkPt.X
    ptArr(1) = selRootSkPt.Y
    ptArr(2) = selRootSkPt.Z
    Set rootPoint = swMath.CreatePoint((ptArr))
```

```
    'Make sure that the point is in model space
    Set rootPoint = rootPoint.MultiplyTransform(swSketchTrans)
```

```
    'Select a direction point
    status = swModelDocExt.SelectByID2("Point1@3DSketch1", "EXTSKETCHPOINT", 0, 0, 0, False, 0, Nothing, 0)
    Set selDirSkPt = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = selDirSkPt.GetSketch
    Set swSketchTrans = swSketch.ModelToSketchTransform.Inverse
    ptArr(0) = selDirSkPt.X
    ptArr(1) = selDirSkPt.Y
    ptArr(2) = selDirSkPt.Z
    Set dirPoint = swMath.CreatePoint((ptArr))
    Set dirPoint = dirPoint.MultiplyTransform(swSketchTrans)
```

```
    'Determine the direction of the spotlight
    Set dirVector = dirPoint.Subtract(rootPoint)
    params = rootPoint.ArrayData
    ptArr(0) = params(0)
    ptArr(1) = params(1)
    ptArr(2) = params(2)
    params = dirVector.ArrayData
    dirArr(0) = params(0)
    dirArr(1) = params(1)
    dirArr(2) = params(2)
```

```
    'Get the current parameters for the spotlight
    params = swModel.LightSourcePropertyValues(swLight.GetID())
    Dim nbrParams As Variant
    nbrParams = UBound(params)
    Dim i As Long
    Debug.Print ("Current position(3) and direction(3)")
    For i = 5 To (nbrParams - 8)
        Debug.Print params(i)
    Next i
```

```
    'Modify the root point and direction vector, then apply the changes
    params(5) = ptArr(0)
    params(6) = ptArr(1)
    params(7) = ptArr(2)
    params(8) = dirArr(0)
    params(9) = dirArr(1)
    params(10) = dirArr(2)
    swModel.LightSourcePropertyValues(swLight.GetID()) = params
    Debug.Print ""
    nbrParams = UBound(params)
    Debug.Print ("Modified position(3) and direction(3)")
    For i = 5 To (nbrParams - 8)
        Debug.Print params(i)
    Next i
```

```
End Sub
```
