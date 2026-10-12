---
title: "Get Polyline Data from Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Polyline_Data_from_View_Example_VB.htm"
---

# Get Polyline Data from Drawing View Example (VBA)

This example shows how to retrieve the defining data of arcs, circles, ellipses, splines, and lines in a drawing view.

```vb
' -----------------------------------------------------------------------------
 ' Preconditions: Open a drawing of a part.
 '
 ' Postconditions: Inspect the Immediate window for edge and geometry data.
 ' -----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Sub main()
    Dim swModel               As SldWorks.ModelDoc2
     Dim swDrawing             As SldWorks.DrawingDoc
     Dim swView                As SldWorks.View
     Dim swSheetView           As SldWorks.View
     Dim swSketch              As SldWorks.Sketch

     ' Get SOLIDWORKS Design application.
     Set swApp = Application.SldWorks

    ' Get active document.
     Set swModel = swApp.ActiveDoc

     ' Downcast model to a drawing.
     Set swDrawing = swModel

    ' The first view is the drawing sheet.
     Set swSheetView = swDrawing.GetFirstView

     ' Print its contents.
     PrintView swSheetView

     ' Get the sketch for the drawing sheet view.
     Set swSketch = swSheetView.GetSketch

    ' Print its contents.
     PrintSketch swSketch

    '
     ' Traverse all "real" views on the sheet.
     '
    ' First view on the sheet.
     Set swView = swSheetView.GetNextView

    Do While Not swView Is Nothing

        PrintView swView

        Set swSketch = swView.GetSketch

        PrintSketch swSketch

        ' Go to next view on the sheet.
         Set swView = swView.GetNextView

    Loop

End Sub

Function PrintView(swView As SldWorks.View) As Boolean
    Dim vEdges As Variant
     Dim vPolyLinesBuffer       As Variant
     Dim vLines                 As Variant
     Dim lNumGeomData           As Long
     Dim i                      As Integer
     Dim iGeomIndex             As Integer
     Dim lNumLines              As Long
     Dim lItemType              As Long
     Dim lBufferSize            As Long
     Dim lBufferIdx             As Long
     Dim lGeomDataSize          As Long
     Dim dGeomData(11)          As Double
     Dim lLineData(3)           As Long
     Dim lLayerData(1)          As Long
     Dim lNumPoints             As Long
     Dim dPoint(2)              As Double
     Dim lGeomDataIdx           As Long
     Dim lLineDataIdx           As Long
     Dim lLayerDataIdx          As Long
     Dim lStartIdx              As Long
     Dim lEndIdx                As Long
     Dim lLineDataSize          As Long
     Dim lLayerDataSize         As Long
     Dim lNumProjectedElements  As Long
     Dim lNumSketchedElements   As Long
    If swView Is Nothing Then
         Exit Function
     End If

     Debug.Print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
     Debug.Print "View = " + swView.Name

     '
     ' Report projected model geometry.
     '
     ' Initialize the number of projected elements for data is contained in the buffer.
     lNumProjectedElements = 0

     ' Get the edges and put all the polyline data into a buffer.
     ' - no cross-hatch lines.
     vEdges = swView.GetPolylines7(1, vPolyLinesBuffer)

    If Not IsEmpty(vEdges) Then
         Debug.Print "Number of edges: " & (UBound(vEdges) - LBound(vEdges) + 1)
    End If

    ' Any polyline data present ?
     If Not IsEmpty(vPolyLinesBuffer) Then

         ' Entries for line data and layer data have a fixed size.
         lLineDataSize = 4
         lLayerDataSize = 2

        ' Get the total buffer size.
         lBufferSize = UBound(vPolyLinesBuffer) - LBound(vPolyLinesBuffer) + 1

         ' We start to traverse the buffer at index 0.
         lBufferIdx = 0

         ' Traverse the buffer, consuming data elements.
         Do While lBufferIdx < lBufferSize

            ' Determine type.
             lItemType = vPolyLinesBuffer(lBufferIdx)
             lBufferIdx = lBufferIdx + 1

             ' We have found another projected element.
             lNumProjectedElements = lNumProjectedElements + 1

             ' Handle type specific data.
             If lItemType = 0 Then

                ' HERE: polylines

                 Debug.Print "    polyline"

                ' Get GeomDataSize:
                 ' - should be zero, but consume it anyway.
                 lGeomDataSize = vPolyLinesBuffer(lBufferIdx)
                 lBufferIdx = lBufferIdx + 1

                ' Ignore GeomData.

            Else

                ' HERE: arc:
                 ' - next to the piecewise linear approximation of the projected model geometry,
                 '   the buffer also contains the arc definining the model geometry projection.

                Debug.Print "    arc"

                 ' Get GeomDataSize:
                 ' - should be 12.
                 lGeomDataSize = vPolyLinesBuffer(lBufferIdx)
                 lBufferIdx = lBufferIdx + 1

                 ' Get GeomData.
                 lGeomDataIdx = 0
                 lStartIdx = lBufferIdx
                 lEndIdx = lStartIdx + (lGeomDataSize - 1)
                 For lBufferIdx = lStartIdx To lEndIdx

                    dGeomData(lGeomDataIdx) = vPolyLinesBuffer(lBufferIdx)

                    lGeomDataIdx = lGeomDataIdx + 1

                Next lBufferIdx

                Debug.Print "      center pt = (" & dGeomData(0) * 1000# & ", " & dGeomData(1) * 1000# & ", " & dGeomData(2) * 1000# & ") mm"
                 Debug.Print "      start  pt = (" & dGeomData(3) * 1000# & ", " & dGeomData(4) * 1000# & ", " & dGeomData(5) * 1000# & ") mm"
                 Debug.Print "      end    pt = (" & dGeomData(6) * 1000# & ", " & dGeomData(7) * 1000# & ", " & dGeomData(8) * 1000# & ") mm"
                 Debug.Print "      normal    = (" & dGeomData(9) & ", " & dGeomData(10) & ", " & dGeomData(11) & ")"

            End If

             ' Get line data.
             lLineDataIdx = 0
             lStartIdx = lBufferIdx
             lEndIdx = lStartIdx + (lLineDataSize - 1)

            For lBufferIdx = lStartIdx To lEndIdx

                lLineData(lLineDataIdx) = vPolyLinesBuffer(lBufferIdx)

                lLineDataIdx = lLineDataIdx + 1

            Next lBufferIdx

              ' Get layer data.
             lLayerDataIdx = 0
             lStartIdx = lBufferIdx
             lEndIdx = lStartIdx + (lLayerDataSize - 1)

            For lBufferIdx = lStartIdx To lEndIdx

                lLayerData(lLayerDataIdx) = vPolyLinesBuffer(lBufferIdx)

                lLayerDataIdx = lLayerDataIdx + 1

            Next lBufferIdx

             ' Get point data.
             lNumPoints = vPolyLinesBuffer(lBufferIdx)

            Debug.Print "      #points = " & CStr(lNumPoints)

            lBufferIdx = lBufferIdx + 1
             lStartIdx = lBufferIdx
             lEndIdx = lStartIdx + lNumPoints * 3 - 1

            For lBufferIdx = lStartIdx To lEndIdx Step 3

                dPoint(0) = vPolyLinesBuffer(lBufferIdx)
                 dPoint(1) = vPolyLinesBuffer(lBufferIdx + 1)
                 dPoint(2) = vPolyLinesBuffer(lBufferIdx + 2)

            Next lBufferIdx

        Loop
    End If

    ' Report the number of projected elements we found.
     Debug.Print "  #projected elements = " & CStr(lNumProjectedElements)

    '
     ' Report sketched geometry; only show lines.
     '

    ' Initialize to zero.
     lNumSketchedElements = 0

     lNumLines = swView.GetLineCount2(1)
    If lNumLines <> 0 Then
        vLines = swView.GetLines4(1)

        If Not IsEmpty(vLines) Then

            For i = 0 To lNumLines - 1

                Debug.Print "    line[" & i & "]"

                Debug.Print "      start pt = (" & vLines(i * 12 + 6) * 1000# & ", " & vLines(i * 12 + 7) * 1000# & ", " & vLines(i * 12 + 8) * 1000# & ") mm"
                 Debug.Print "      end   pt = (" & vLines(i * 12 + 9) * 1000# & ", " & vLines(i * 12 + 10) * 1000# & ", " & vLines(i * 12 + 11) * 1000# & ") mm"

            Next i

        End If
    End If

    lNumSketchedElements = lNumSketchedElements + lNumLines
     lNumSketchedElements = lNumSketchedElements + swView.GetArcCount
     lNumSketchedElements = lNumSketchedElements + swView.GetEllipseCount
     lNumSketchedElements = lNumSketchedElements + swView.GetParabolaCount

    ' Report the number of sketched elements found.
     Debug.Print "  #sketched elements = " & CStr(lNumSketchedElements)

End Function

Function PrintSketch(swSketch As SldWorks.Sketch) As Boolean
    Dim vSegments              As Variant
     Dim lNumSegments           As Long

     If swSketch Is Nothing Then
         Debug.Print "No Sketch"
     End If

     ' Get the sketch segments.
     vSegments = swSketch.GetSketchSegments

     ' Determine number of segments.
     If Not IsEmpty(vSegments) Then
         lNumSegments = UBound(vSegments) - LBound(vSegments) + 1
     Else
         lNumSegments = 0
     End If

     Debug.Print "Sketch = "
     Debug.Print "  #points   = " & CStr(swSketch.GetUserPointsCount())
     Debug.Print "  #segments = " & CStr(lNumSegments)

    ' Get count of specific sketch segments.
     If lNumSegments > 0 Then

        Debug.Print "    #arcs      = " & CStr(swSketch.GetArcCount())
         Debug.Print "    #lines     = " & CStr(swSketch.GetLineCount2(1))
         Debug.Print "    #ellipses  = " & CStr(swSketch.GetEllipseCount())
         Debug.Print "    #parabolas = " & CStr(swSketch.GetParabolaCount())

    End If

End Function
```
