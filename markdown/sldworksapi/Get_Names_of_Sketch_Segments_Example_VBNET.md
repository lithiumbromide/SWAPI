---
title: "Get Names of Sketch Segments Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Sketch_Segments_Example_VBNET.htm"
---

# Get Names of Sketch Segments Example (VB.NET)

This example shows how to get the names of the sketch segments in a sheet metal bend.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part or a drawing containing a bend.
 ' 2. Unsuppress the flat pattern for the bend.
 ' 3. Select a bend feature in the FeatureManager design tree.

 ' Postconditions: Inspect the Immediate window for information about each
 ' sketch segment in the bend feature.
 '--------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swMathUtil As MathUtility
         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swOneBend As OneBendFeatureData
         Dim vSketchSegs As Object
         Dim swSketchSeg As SketchSegment
         Dim swSketch As Sketch
         Dim swSketchFeat As Feature
         Dim swSketchLine As SketchLine
         Dim swSkStartPt As SketchPoint
         Dim swSkEndPt As SketchPoint
         Dim swSelData As SelectData
         Dim nPt(2) As Double
         Dim vPt As Object
         Dim swStartPt As MathPoint
         Dim swEndPt As MathPoint
         Dim swSkXform As MathTransform
         Dim vID As Object
         Dim i As  Long

         swMathUtil = swApp.GetMathUtility
         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSelData = swSelMgr.CreateSelectData
         swOneBend = swFeat.GetDefinition
         Debug.Print("Type of bend (swBendType_e): " & swOneBend.GetType())
         Debug.Print("Number of sketch segments: " & swOneBend.GetFlatPatternSketchSegmentCount2)
         vSketchSegs = swOneBend.FlatPatternSketchSegments2

         For i = 0 To UBound(vSketchSegs)
             swSketchSeg = vSketchSegs(i)
             swSketch = swSketchSeg.GetSketch
             swSketchLine = swSketchSeg
             swSkStartPt = swSketchLine.GetStartPoint2
             swSkEndPt = swSketchLine.GetEndPoint2
             vID = swSketchSeg.GetID

             ' Get sketch feature
             swSketchFeat = swSketch
             swSkXform = swSketch.ModelToSketchTransform
             swSkXform = swSkXform.Inverse

             nPt(0) = swSkStartPt.X
             nPt(1) = swSkStartPt.Y
             nPt(2) = swSkStartPt.Z
             vPt = nPt
             swStartPt = swMathUtil.CreatePoint(vPt)
             swStartPt = swStartPt.MultiplyTransform(swSkXform)

             nPt(0) = swSkEndPt.X
             nPt(1) = swSkEndPt.Y
             nPt(2) = swSkEndPt.Z
             vPt = nPt
             swEndPt = swMathUtil.CreatePoint(vPt)
             swEndPt = swEndPt.MultiplyTransform(swSkXform)

             Debug.Print("File = " & swModel.GetPathName)
             Debug.Print("  Feature = " & swFeat.Name & " [" & swFeat.GetTypeName2 & "]")
             Debug.Print("    Sketch             = " & swSketchFeat.Name)
             Debug.Print("    SegID              = [" & vID(0)   ", " & vID(1) & "]")
             Debug.Print("    Start with respect to sketch   = (" & swSkStartPt.X * 1000.0# & ", " & swSkStartPt.Y * 1000.0# & ", " & swSkStartPt.Z * 1000.0# & ") mm")
             Debug.Print("    End with respect to sketch   = (" & swSkEndPt.X * 1000.0# & ", " & swSkEndPt.Y * 1000.0# & ", " & swSkEndPt.Z * 1000.0# & ") mm")
             Debug.Print("    Start with respect to model    = (" & swStartPt.ArrayData(0) * 1000.0# & ", " & swStartPt.ArrayData(1) * 1000.0#   ", " & swStartPt.ArrayData(2) * 1000.0#   ") mm")
             Debug.Print("    End with respect to model    = (" & swEndPt.ArrayData(0) * 1000.0# & ", " & swEndPt.ArrayData(1) * 1000.0#   ", " & swEndPt.ArrayData(2) * 1000.0# & ") mm")
         Next i
     End Sub

     Public swApp As SldWorks

 End  Class
```
