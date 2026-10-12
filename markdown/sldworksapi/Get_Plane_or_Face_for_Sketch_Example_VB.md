---
title: "Get Plane or Face for Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Plane_or_Face_for_Sketch_Example_VB.htm"
---

# Get Plane or Face for Sketch Example (VBA)

This example shows how to get the plane or face on which a selected sketch was drawn.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open apart or assembly.
' 2. Select a sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Selects the plane or face on which the selected
'    sketch was drawn.
' 2. Examine the Immediate window and graphics area.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim pSWApp As SldWorks.SldWorks
    Dim pModel As SldWorks.ModelDoc2
    Dim pSelMgr As SldWorks.SelectionMgr
    Dim pFeat As SldWorks.Feature
    Dim pSketch As SldWorks.Sketch
    Dim pEntity As SldWorks.Entity
    Dim pPlaneFeat As SldWorks.Feature
    Dim pFace As SldWorks.Face2
    Dim pRefPlane As SldWorks.RefPlane
    Dim vPlaneParams As Variant
    Dim vNormal As Variant
    Dim bRet As Boolean
    Dim nEntType As Long
```

```
    Set pSWApp = CreateObject("SldWorks.Application")
    Set pModel = pSWApp.ActiveDoc
    Set pSelMgr = pModel.SelectionManager
    Set pFeat = pSelMgr.GetSelectedObject5(1)
    Set pSketch = pFeat.GetSpecificFeature2
    Set pEntity = pSketch.GetReferenceEntity(nEntType)
```

```
    Debug.Print "Sketch Name = " + pFeat.Name
```

```
    If nEntType = swSelDATUMPLANES Then
        Set pPlaneFeat = pEntity
        Set pRefPlane = pEntity
        vPlaneParams = pRefPlane.GetRefPlaneParams
        Debug.Print "Plane Selected!"
        Debug.Print "  Origin   = (" + Str(vPlaneParams(0) * 1000#) + "," + Str(vPlaneParams(1) * 1000#) + "," + Str(vPlaneParams(2) * 1000#) + ") mm"
        Debug.Print "  Xvector  = (" + Str(vPlaneParams(3)) + "," + Str(vPlaneParams(4)) + "," + Str(vPlaneParams(5)) + ")"
        Debug.Print "  Normal   = (" + Str(vPlaneParams(6)) + "," + Str(vPlaneParams(7)) + "," + Str(vPlaneParams(8)) + ")"
        ' Cannot select through Entity; must
        ' select through Feature
        bRet = pPlaneFeat.Select2(False, 0)
    End If
```

```
    If nEntType = swSelFACES Then
        Set pFace = pEntity
        vNormal = pFace.Normal
        Debug.Print "Face Selected!"
        Debug.Print "  Normal   = (" + Str(vNormal(0)) + "," + Str(vNormal(1)) + "," + Str(vNormal(2)) + ")"
        bRet = pEntity.Select2(False, 0)
    End If
```

```
End Sub
```
