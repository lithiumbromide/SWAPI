---
title: "Get Persistent Identifiers and Type for Sketch Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Persistent_Identifiers_and_Type_for_Sketch_Points_Example_VB.htm"
---

# Get Persistent Identifiers and Type for Sketch Points Example (VBA)

This example shows how to get the persistent identifiers and types for sketch points.

**NOTE**: SOLIDWORKS Design allocates a persistent ID for sketch points and segments, accessible by ISketchPoint::GetID. This method allows you to store the identifier and then return to the sketch entity at a later time. There are also sketch points that are not visible to the user. These are typically used internally by SOLIDWORKS Design for various purposes. Sketch points are also created from other operations; for example, creating a spline or adding a midpoint relation. Each sketch point has a read-only property, ISketchPoint::Type, that indicates how it is used in the sketch.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly.
 ' 2. Select a 2D or 3D sketch.
 '
 ' Postconditions:
 ' 1. Gets the selected sketch's sketch-point IDs and types.
 ' 2. Examine the Immediate window.
 '
 ' NOTES:
 ' * Both SketchPoint::ID and ISketchPoint::Type are read-only.
 ' * The identifier is unique to the sketch and may be duplicated
 '   in the model. To unambiguously resolve a sketch entity, you need both
 '   the sketch and the sketch identifier.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swSketch                As SldWorks.Sketch
     Dim vSketchPtArr            As Variant
     Dim vSketchPt               As Variant
     Dim swSketchPt              As SldWorks.SketchPoint
     Dim vID                     As Variant
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSketch = swFeat.GetSpecificFeature
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
    vSketchPtArr = swSketch.GetSketchPoints: If IsEmpty(vSketchPtArr) Then Exit Sub
    For Each vSketchPt In vSketchPtArr
         Set swSketchPt = vSketchPt
         vID = swSketchPt.GetID
         Debug.Print "    Pt [" & vID(0) & ", " & vID(1) & "]  = (" & swSketchPt.X * 1000# & ", " & swSketchPt.Y * 1000# & ", " & swSketchPt.Z * 1000# & ") mm"
         Debug.Print "      Type = " & swSketchPt.Type
     Next vSketchPt
End Sub
```
