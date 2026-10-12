---
title: "Get Persistent Identifiers and Type for Sketch Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_VBNET.htm"
---

# Get Persistent Identifiers and Type for Sketch Points Example (VB.NET)

This example shows how to get the persistent identifiers and types for sketch points.

```vb
NOTE: SOLIDWORKS Design allocates a persistent ID for sketch points and segments, accessible by ISketchPoint::GetID. This method allows you to store the identifier and then return to the sketch entity at a later time. There are also sketch points that are not visible to the user. These are typically used internally by SOLIDWORKS Design for various purposes. Sketch points are also created from other operations; for example, creating a spline or adding a midpoint relation. Each sketch point has a read-only property, ISketchPoint::Type, that  indicates how it is used in the sketch.
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swSketch As Sketch
         Dim vSketchPtArr As Object
         Dim vSketchPt As Object
         Dim swSketchPt As SketchPoint
         Dim vID As Object

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSketch = swFeat.GetSpecificFeature

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)

         vSketchPtArr = swSketch.GetSketchPoints :  If IsNothing(vSketchPtArr) Then Exit  Sub

         For Each vSketchPt In vSketchPtArr
             swSketchPt = vSketchPt
             vID = swSketchPt.GetID
             Debug.Print("    Pt [" & vID(0) & ", " & vID(1) & "]  = (" & swSketchPt.X * 1000.0# & ", " & swSketchPt.Y * 1000.0# & ", " & swSketchPt.Z * 1000.0# & ") mm")
             Debug.Print("      Type = " & swSketchPt.Type)
         Next vSketchPt

     End Sub

     Public swApp As SldWorks

 End  Class
```
