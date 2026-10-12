---
title: "Calculate Closest Distance Between Model Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm"
---

# Calculate Closest Distance Between Model Components Example (VBA)

This example shows how to calculate the closest distance between two components in an assembly.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\landing_gear.sldasm.
' 2. Click a face on oleostrut<1>.
' 3. Ctrl+click a face on lwrsway_lnk<1>.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Creates a 3D sketch using the selection points and calculates
'    the distance between the components.
' 2. Examine the Immediate window, graphics area, and
'    the FeatureManager design tree.
'
' NOTE: Because this assembly is used elsewhere, do not save
' changes.
'------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace1 As SldWorks.Face2
    Dim swFace2 As SldWorks.Face2
    Dim vPt1 As Variant
    Dim vPt2 As Variant
    Dim nDist As Double
    Dim swSkPoint1 As SldWorks.SketchPoint
    Dim swSkPoint2 As SldWorks.SketchPoint
    Dim swSkLine As SldWorks.SketchLine
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace1 = swSelMgr.GetSelectedObject6(1, -1)
    Set swFace2 = swSelMgr.GetSelectedObject6(2, -1)
```

```
    nDist = swModel.ClosestDistance(swFace1, swFace2, vPt1, vPt2)
```

```
    Debug.Assert nDist > 0#
    Debug.Assert Not IsEmpty(vPt1)
    Debug.Assert Not IsEmpty(vPt2)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Selection type (swSelFaces = 2)"
    Debug.Print "    1 = " & swSelMgr.GetSelectedObjectType2(1)
    Debug.Print "    2 = " & swSelMgr.GetSelectedObjectType2(2)
    Debug.Print "  Coordinates of selection point"
    Debug.Print "    1 = (" & vPt1(0) * 1000# & ", " & vPt1(1) * 1000# & ", " & vPt1(2) * 1000# & ") mm"
    Debug.Print "    2 = (" & vPt2(0) * 1000# & ", " & vPt2(1) * 1000# & ", " & vPt2(2) * 1000# & ") mm"
    Debug.Print "  Distance between selection points = " & nDist * 1000# & " mm"
```

```
    swModel.SetAddToDB True
```

```
    swModel.Insert3DSketch2 False
```

```
    Set swSkPoint1 = swModel.CreatePoint2(vPt1(0), vPt1(1), vPt1(2))
    Set swSkPoint2 = swModel.CreatePoint2(vPt2(0), vPt2(1), vPt2(2))
    Set swSkLine = swModel.CreateLine2(vPt1(0), vPt1(1), vPt1(2), vPt2(0), vPt2(1), vPt2(2))
```

```
    swModel.SetAddToDB False
```

```
    swModel.Insert3DSketch2 True
```

```
End Sub
```
