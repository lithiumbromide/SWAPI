---
title: "Get Polylines Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Polylines_Information_Example_VB.htm"
---

# Get Polylines Information Example (VBA)

This example shows how to use IView::GetPolyLines5 and IView::GetSketch. This example also illustrates the differences between projected model geometry and sketched geometry.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains:
'    * drawing views of a model comprised of arcs, circles,
'      ellipses, splines, and straight lines.
'    * sketched arcs, circles, ellipses, splines, and
'      straight lines on the drawing.
' 2. Verify that c:\temp exists.
'
' Postconditions:
' 1. Gets the drawing's polylines and any sketches on the
'    drawing information.
' 2. Open c:\temp\PolylinesInformation.txt in a text editor
'    and examine the contents of the file.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim swDrawing As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swSheetView As SldWorks.View
    Dim swSketch As SldWorks.Sketch
```

```
    ' Get SOLIDWORKS Design application
    Set swApp = Application.SldWorks
```

```
    ' Get active document
    Set swModel = swApp.ActiveDoc
```

```
    ' Open output file for polylines information
    Open "c:\temp\PolylinesInformation.txt" For Output As #1
```

```
    ' Downcast model to a drawing
    Set swDrawing = swModel
```

```
    ' Get the first view, which is the drawing sheet
    Set swSheetView = swDrawing.GetFirstView
```

```
    ' Print its contents
    PrintView swSheetView
```

```
    ' Get the sketch for the drawing sheet view
    Set swSketch = swSheetView.GetSketch
```

```
    ' Print its contents
    PrintSketch swSketch
```

```
    ' Traverse all drawing views on the sheet
    ' First drawing view on the sheet
    Set swView = swSheetView.GetNextView
    Do While Not swView Is Nothing
        PrintView swView
        Set swSketch = swView.GetSketch
        PrintSketch swSketch
        ' Go to next drawing view on the sheet
        Set swView = swView.GetNextView
    Loop
```

```
    ' Close c:\temp\PolylinesInformation.txt
    Close #1
```

```
End Sub
```

```
Function PrintView(swView As SldWorks.View) As Boolean
    Dim vPolyLinesBuffer As Variant
    Dim vLines As Variant
    Dim lNumGeomData As Long
    Dim i As Integer
    Dim iGeomIndex As Integer
    Dim lNumLines As Long
    Dim lItemType As Long
    Dim lBufferSize As Long
    Dim lBufferIdx As Long
    Dim lGeomDataSize As Long
    Dim dGeomData(11) As Double
    Dim lLineData(3) As Long
    Dim lLayerData(1) As Long
    Dim lNumPoints As Long
    Dim dPoint(2) As Double
    Dim lGeomDataIdx As Long
    Dim lLineDataIdx As Long
    Dim lLayerDataIdx As Long
    Dim lStartIdx As Long
    Dim lEndIdx As Long
    Dim lLineDataSize As Long
    Dim lLayerDataSize As Long
    Dim lNumProjectedElements As Long
    Dim lNumSketchedElements As Long
```

```
    If swView Is Nothing Then
        Exit Function
    End If
```

```
    Write #1, ""
    Write #1, "View = " + swView.GetName2
```

```
    ' Report projected model geometry
    ' Initialize the number of projected elements for data is contained in the buffer
    lNumProjectedElements = 0
```

```
    ' Get all the polyline data into a buffer
    ' No cross-hatch lines
    vPolyLinesBuffer = swView.GetPolylines5(0)
```

```
    ' Any polyline data present ?
    If Not IsEmpty(vPolyLinesBuffer) Then
        ' Entries for line data and layer data have a fixed size
        lLineDataSize = 4
        lLayerDataSize = 2
        ' Get the total buffer size
    	lBufferSize = UBound(vPolyLinesBuffer) - LBound(vPolyLinesBuffer) + 1
        ' Start to traverse the buffer at index 0
        lBufferIdx = 0
        ' Traverse the buffer, consuming data elements
        Do While lBufferIdx < lBufferSize
            ' Determine type
            lItemType = vPolyLinesBuffer(lBufferIdx)
            lBufferIdx = lBufferIdx + 1
            ' Found another projected element
            lNumProjectedElements = lNumProjectedElements + 1
            ' Handle type specific data
            If lItemType = 0 Then
                ' HERE: polyline
                Write #1, "    Polyline"
                ' Get GeomDataSize:
                ' should be zero, but consume it anyway
                lGeomDataSize = vPolyLinesBuffer(lBufferIdx)
                lBufferIdx = lBufferIdx + 1
                ' Ignore GeomData
            Else
                ' HERE: arc:
                ' Next to the piecewise linear approximation of the projected model geometry,
                ' the buffer also contains the arc defining the model geometry projection
                Write #1, "    Arc"
                ' Get GeomDataSize:
                ' should be 12
                lGeomDataSize = vPolyLinesBuffer(lBufferIdx)
                lBufferIdx = lBufferIdx + 1
                ' Get GeomData
                lGeomDataIdx = 0
                lStartIdx = lBufferIdx
                lEndIdx = lStartIdx + (lGeomDataSize - 1)
                For lBufferIdx = lStartIdx To lEndIdx
                    dGeomData(lGeomDataIdx) = vPolyLinesBuffer(lBufferIdx)
                    lGeomDataIdx = lGeomDataIdx + 1
                Next lBufferIdx
                Write #1, "      Center point = (" & dGeomData(0) * 1000# & ", " & dGeomData(1) * 1000# & ", " & dGeomData(2) * 1000# & ") mm"
                Write #1, "      Start  point = (" & dGeomData(3) * 1000# & ", " & dGeomData(4) * 1000# & ", " & dGeomData(5) * 1000# & ") mm"
                Write #1, "      End    point = (" & dGeomData(6) * 1000# & ", " & dGeomData(7) * 1000# & ", " & dGeomData(8) * 1000# & ") mm"
                Write #1, "      Normal       = (" & dGeomData(9) & ", " & dGeomData(10) & ", " & dGeomData(11) & ")"
            End If
```

```
            ' Get line data
            lLineDataIdx = 0
            lStartIdx = lBufferIdx
            lEndIdx = lStartIdx + (lLineDataSize - 1)
            For lBufferIdx = lStartIdx To lEndIdx
                lLineData(lLineDataIdx) = vPolyLinesBuffer(lBufferIdx)
                lLineDataIdx = lLineDataIdx + 1
            Next lBufferIdx
             ' Get layer data
            lLayerDataIdx = 0
            lStartIdx = lBufferIdx
            lEndIdx = lStartIdx + (lLayerDataSize - 1)
            For lBufferIdx = lStartIdx To lEndIdx
                lLayerData(lLayerDataIdx) = vPolyLinesBuffer(lBufferIdx)
                lLayerDataIdx = lLayerDataIdx + 1
            Next lBufferIdx
            ' Get point data
            If lBufferIdx <= UBound(vPolyLinesBuffer) Then
            	lNumPoints = vPolyLinesBuffer(lBufferIdx)
                Write #1, "      Number of points = " & CStr(lNumPoints)
                lBufferIdx = lBufferIdx + 1
                lStartIdx = lBufferIdx
                lEndIdx = lStartIdx + lNumPoints * 3 - 1
                For lBufferIdx = lStartIdx To lEndIdx Step 3
                    dPoint(0) = vPolyLinesBuffer(lBufferIdx)
                    dPoint(1) = vPolyLinesBuffer(lBufferIdx + 1)
                    dPoint(2) = vPolyLinesBuffer(lBufferIdx + 2)
                Next lBufferIdx
            End If
        Loop
    End If
```

```
    ' Report the number of projected elements found
    Write #1, "  Number of projected elements = " & CStr(lNumProjectedElements)
```

```
    ' Report sketched geometry:
    ' only show lines
```

```
    ' Initialize to zero
    lNumSketchedElements = 0
    lNumLines = swView.GetLineCount2(1)
    If lNumLines <> 0 Then
        vLines = swView.GetLines4(1)
        If Not IsEmpty(vLines) Then
            For i = 0 To lNumLines - 1
                Write #1, "    line[" & i & "]"
                Write #1, "      Start point = (" & vLines(i * 12 + 6) * 1000# & ", " & vLines(i * 12 + 7) * 1000# & ", " & vLines(i * 12 + 8) * 1000# & ") mm"
                Write #1, "      End   point = (" & vLines(i * 12 + 9) * 1000# & ", " & vLines(i * 12 + 10) * 1000# & ", " & vLines(i * 12 + 11) * 1000# & ") mm"
            Next i
        End If
    End If
    lNumSketchedElements = lNumSketchedElements + lNumLines
    lNumSketchedElements = lNumSketchedElements + swView.GetArcCount
    lNumSketchedElements = lNumSketchedElements + swView.GetEllipseCount
    lNumSketchedElements = lNumSketchedElements + swView.GetParabolaCount
```

```
    ' Report the number of sketched elements found
    Write #1, "  Number of sketched elements = " & CStr(lNumSketchedElements)
```

```
End Function
```

```
Function PrintSketch(swSketch As SldWorks.Sketch) As Boolean
    Dim vSegments As Variant
    Dim lNumSegments As Long
```

```
    If swSketch Is Nothing Then
        Write #1, "No sketch"
    End If
```

```
    ' Get the sketch segments
    vSegments = swSketch.GetSketchSegments
```

```
    ' Determine number of segments
    If Not IsEmpty(vSegments) Then
        lNumSegments = UBound(vSegments) - LBound(vSegments) + 1
    Else
        lNumSegments = 0
    End If
```

```
    Write #1, "Sketch = "
    Write #1, "  Number of points   = " & CStr(swSketch.GetUserPointsCount())
    Write #1, "  Number of segments = " & CStr(lNumSegments)
```

```
    ' Get number of specific sketch segments
    If lNumSegments > 0 Then
        Write #1, "    Number of arcs      = " & CStr(swSketch.GetArcCount())
        Write #1, "    Number of lines     = " & CStr(swSketch.GetLineCount2(1))
        Write #1, "    Number of ellipses  = " & CStr(swSketch.GetEllipseCount())
        Write #1, "    Number of parabolas = " & CStr(swSketch.GetParabolaCount())
    End If
```

```
End Function
```
