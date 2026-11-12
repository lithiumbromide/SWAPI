---
title: "Get Corner Points of a Reference Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corner_Points_of_Reference_Plane_Example_VBNET.htm"
---

# Get Corner Points of a Reference Plane Example (VB.NET)

This example shows how to obtain the four corner points of a reference plane.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Creates 3DSketch1 containing four corner points of the reference plane.
' 3. Gets the coordinates of each corner point.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim boolstatus As Boolean
     Dim swFeature As Feature
     Dim swRefPlane As RefPlane
     Dim swModelExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim vMathPoints As Object
     Dim vArrayData As Object
     Dim pMathPoint As MathPoint
     Dim i As Integer
     Dim swSketch As Sketch
     Dim sketchMgr As SketchManager
     Dim sketchPt As SketchPoint
     Dim swRefPlaneFeatData As RefPlaneFeatureData
     Dim filename As String
     Dim errors As Long
     Dim warnings As Long
    Sub main()
        filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
         swModel = swApp.OpenDoc6(filename, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         sketchMgr = swModel.SketchManager
         boolstatus = swModelExt.SelectByID2("Plane4", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
         swFeature = swSelMgr.GetSelectedObject6(1, -1)
         swRefPlane = swFeature.GetSpecificFeature2
         vMathPoints = swRefPlane.CornerPoints 'Four (4) MathPoint objects are always returned
         sketchMgr.Insert3DSketch(True)
         For i = 0 To UBound(vMathPoints)
             vArrayData = vMathPoints(i).ArrayData
             Debug.Print(" Point x = " & vArrayData(0))
             Debug.Print(" Point y = " & vArrayData(1))
             Debug.Print(" Point z = " & vArrayData(2))
             Debug.Print("")
             sketchPt = sketchMgr.CreatePoint(vArrayData(0), vArrayData(1), vArrayData(2))
         Next i
         sketchMgr.Insert3DSketch(True)
     End Sub
    Public swApp As SldWorks
End Class
```
