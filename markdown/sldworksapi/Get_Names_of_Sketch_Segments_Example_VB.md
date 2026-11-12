---
title: "Get Names of Sketch Segments Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Sketch_Segments_Example_VB.htm"
---

# Get Names of Sketch Segments Example (VBA)

This example shows how to get the names of the sketch segments in a sheet metal bend.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part or a drawing containing a sketched bend.
 ' 2. Unsuppress the flat pattern for the bend.
 ' 3. Select a bend feature in the FeatureManager design tree.
'
 ' Postconditions: Inspect the Immediate window for information about each
 ' sketch segment in the bend feature.
 '--------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swMathUtil              As SldWorks.MathUtility
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swOneBend               As SldWorks.OneBendFeatureData
     Dim vSketchSegs             As Variant
     Dim swSketchSeg             As SldWorks.SketchSegment
     Dim swSketch                As SldWorks.Sketch
     Dim swSketchFeat            As SldWorks.Feature
     Dim swSketchLine            As SldWorks.SketchLine
     Dim swSkStartPt             As SldWorks.SketchPoint
     Dim swSkEndPt               As SldWorks.SketchPoint
     Dim swSelData               As SldWorks.SelectData
     Dim nPt(2)                  As Double
     Dim vPt                     As Variant
     Dim swStartPt               As SldWorks.MathPoint
     Dim swEndPt                 As SldWorks.MathPoint
     Dim swSkXform               As SldWorks.MathTransform
     Dim vID                     As Variant
     Dim i                       As Long
    Set swApp = Application.SldWorks
     Set swMathUtil = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSelData = swSelMgr.CreateSelectData
     Set swOneBend = swFeat.GetDefinition
     Debug.Print "Type of bend (swBendType_e): " & swOneBend.GetType()
     Debug.Print "Number of sketch segments: " & swOneBend.GetFlatPatternSketchSegmentCount2
     vSketchSegs = swOneBend.FlatPatternSketchSegments2

    For i = 0 To UBound(vSketchSegs)
         Set swSketchSeg = vSketchSegs(i)
         Set swSketch = swSketchSeg.GetSketch
         Set swSketchLine = swSketchSeg
         Set swSkStartPt = swSketchLine.GetStartPoint2
         Set swSkEndPt = swSketchLine.GetEndPoint2
         vID = swSketchSeg.GetID

        ' Get sketch feature
         Set swSketchFeat = swSketch
         Set swSkXform = swSketch.ModelToSketchTransform
         Set swSkXform = swSkXform.Inverse

        nPt(0) = swSkStartPt.X
         nPt(1) = swSkStartPt.Y
         nPt(2) = swSkStartPt.Z
         vPt = nPt
         Set swStartPt = swMathUtil.CreatePoint(vPt)
         Set swStartPt = swStartPt.MultiplyTransform(swSkXform)

        nPt(0) = swSkEndPt.X
         nPt(1) = swSkEndPt.Y
         nPt(2) = swSkEndPt.Z
         vPt = nPt
         Set swEndPt = swMathUtil.CreatePoint(vPt)
         Set swEndPt = swEndPt.MultiplyTransform(swSkXform)

        Debug.Print "File = " & swModel.GetPathName
         Debug.Print "  Feature = " & swFeat.Name & " [" & swFeat.GetTypeName2 & "]"
         Debug.Print "    Sketch             = " & swSketchFeat.Name
         Debug.Print "    SegID              = [" & vID(0) & ", " & vID(1) & "]"
         Debug.Print "    Start with respect to sketch   = (" & swSkStartPt.X * 1000# & ", " & swSkStartPt.Y * 1000# & ", " & swSkStartPt.Z * 1000# & ") mm"
         Debug.Print "    End with respect to sketch   = (" & swSkEndPt.X * 1000# & ", " & swSkEndPt.Y * 1000# & ", " & swSkEndPt.Z * 1000# & ") mm"
         Debug.Print "    Start with respect to model    = (" & swStartPt.ArrayData(0) * 1000# & ", " & swStartPt.ArrayData(1) * 1000# & ", " & swStartPt.ArrayData(2) * 1000# & ") mm"
         Debug.Print "    End with respect to model    = (" & swEndPt.ArrayData(0) * 1000# & ", " & swEndPt.ArrayData(1) * 1000# & ", " & swEndPt.ArrayData(2) * 1000# & ") mm"
     Next i
 End Sub
```
