---
title: "Insert Coordinate System at Center of Mass Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm"
---

# Insert Coordinate System at Center of Mass Example (VBA)

This example shows how to insert a coordinate system on the center of mass.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a 3D sketch at the center of mass.
' 2. Inserts a coordinate system at center of mass.
' 3. Examine the graphics area and the Immediate window.
'-------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeat As SldWorks.Feature
    Dim swModDocExt As SldWorks.ModelDocExtension
    Dim swMass As SldWorks.MassProperty
    Dim vCofG As Variant
    Dim vXaxis As Variant
    Dim vYAxis As Variant
    Dim vZAxis As Variant
    Dim swSkCofG As SldWorks.SketchPoint
    Dim swSkXaxis As SldWorks.SketchLine
    Dim swSkYaxis As SldWorks.SketchLine
    Dim swSkSegXaxis As SldWorks.SketchSegment
    Dim swSkSegYaxis As SldWorks.SketchSegment
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swModDocExt = swModel.Extension
    Set swMass = swModDocExt.CreateMassProperty
    vCofG = swMass.CenterOfMass
    vXaxis = swMass.PrincipleAxesOfInertia(0)
    vYAxis = swMass.PrincipleAxesOfInertia(1)
    vZAxis = swMass.PrincipleAxesOfInertia(2)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Mass             = " & swMass.Mass * 1000# & " g"
    Debug.Print "  Surface Area     = " & swMass.SurfaceArea * 1000000# & " mm^2"
    Debug.Print "  Volume           = " & swMass.Volume * 1000000000# & " mm^3"
    Debug.Print "  Density          = " & swMass.Density & " kg/m^3"
    Debug.Print "  CenterOfMass     = (" & vCofG(0) * 1000# & ", " & vCofG(1) * 1000# & ", " & vCofG(2) * 1000# & ") mm"
    Debug.Print "  X axis           = (" & vXaxis(0) & ", " & vXaxis(1) & ", " & vXaxis(2) & ")"
    Debug.Print "  Y axis           = (" & vYAxis(0) & ", " & vYAxis(1) & ", " & vYAxis(2) & ")"
    Debug.Print "  Z axis           = (" & vZAxis(0) & ", " & vZAxis(1) & ", " & vZAxis(2) & ")"
```

```
    swModel.Insert3DSketch2 False
    swModel.SetAddToDB True
```

```
    Set swSkCofG = swModel.CreatePoint2(vCofG(0), vCofG(1), vCofG(2))
    Set swSkXaxis = swModel.CreateLine2(vCofG(0), vCofG(1), vCofG(2), vCofG(0) + vXaxis(0), vCofG(1) + vXaxis(1), vCofG(2) + vXaxis(2))
    Set swSkYaxis = swModel.CreateLine2(vCofG(0), vCofG(1), vCofG(2), vCofG(0) + vYAxis(0), vCofG(1) + vYAxis(1), vCofG(2) + vYAxis(2))
    Set swSkSegXaxis = swSkXaxis
    Set swSkSegYaxis = swSkYaxis
```

```
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
    swModel.ClearSelection2 True
```

```
    swSelData.Mark = 1
    bRet = swSkCofG.Select4(True, swSelData): Debug.Assert bRet
    swSelData.Mark = 2
    bRet = swSkSegXaxis.Select4(True, swSelData): Debug.Assert bRet
    swSelData.Mark = 4
    bRet = swSkSegYaxis.Select4(True, swSelData): Debug.Assert bRet
```

```
    bRet = swModel.InsertCoordinateSystem(False, False, False): Debug.Assert bRet
```

```
End Sub
```
