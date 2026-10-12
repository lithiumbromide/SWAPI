---
title: "Get Plane On Which Sketch Created Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Plane_on_which_Sketch_Created_Example_VB.htm"
---

# Get Plane On Which Sketch Created Example (VBA)

This example shows how to get the plane on which the sketch used for the feature was created.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cstick.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the plane on which the sketch for Revolve1
'    was created.
' 2. Examine the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim boolstatus As Boolean
Dim longstatus As Long
Dim parents As Variant
Dim swParentFeat As SldWorks.Feature
Dim swSketch As SldWorks.Sketch
Dim swSketchPlane As Object
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    boolstatus = swModel.Extension.SelectByID2("Revolve1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    parents = swFeat.GetParents
    For i = 0 To UBound(parents)
        Set swParentFeat = parents(i)
        If swParentFeat.GetTypeName = "ProfileFeature" Then
           Set swSketch = swParentFeat.GetSpecificFeature2
           Set swSketchPlane = swSketch.GetReferenceEntity(longstatus)
           'The plane can be either a face or a Feature object
           Debug.Print ("Type of reference entity (4 = swSelectType_e.swSelDATUMPLANES): " & longstatus)
        End If
    Next i
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
