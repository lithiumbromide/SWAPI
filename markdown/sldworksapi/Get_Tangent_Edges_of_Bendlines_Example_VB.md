---
title: "Get Tangent Edges of Bendlines Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tangent_Edges_of_Bendlines_Example_VB.htm"
---

# Get Tangent Edges of Bendlines Example (VBA)

This example shows how to get each bendline's visible tangent edges in a flat-pattern view in a drawing of a sheet metal part.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a SOLIDWORKS Design drawing of a sheet metal part
'    that has a flat-pattern view with
'    bend lines with tangent edges.
' 2. Open the Immediate window.
'
' Preconditions: Examine the Immediate window.
'---------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swView As SldWorks.View
Dim nbrBendlines As Long
Dim BendlinesArr As Variant
Dim nbrRelatedTangentEdges As Long
Dim RelatedTangentEdgesArr As Variant
Dim i As Long
Dim swSketchSegment As SldWorks.SketchSegment
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawing = swModel
```

```
    ' Get drawing sheet
    Set swSheet = swDrawing.GetCurrentSheet
```

```
    ' Get name of drawing sheet
    Debug.Print "Name of drawing sheet: " & swSheet.GetName
```

```
    ' Get number of views on drawing sheet
    Debug.Print "  Number of drawing views on drawing sheet: " & swDrawing.GetViewCount
```

```
    ' First view is the current drawing sheet
    Set swView = swDrawing.GetFirstView
    Debug.Print "    First drawing view is the current drawing sheet, so..."
```

```
    ' Get first drawing view on drawing sheet
    Set swView = swView.GetNextView
```

```
    While Not swView Is Nothing
        Debug.Print "        Get next drawing view on drawing sheet..."
```

```
        ' Get first true drawing view on current drawing sheet
        Debug.Print "           Is this drawing view a flat-pattern view? " & swView.IsFlatPatternView
```

```
        ' If this drawing view is a flat pattern view, then
        ' get its bendlines and their related tangent edges
        If swView.IsFlatPatternView Then
```

```
            ' Get number of bendlines in the drawing view
            nbrBendlines = swView.GetBendLineCount
            Debug.Print "            Number of bendlines in this drawing view: " & nbrBendlines
            If (nbrBendlines > 0) Then
                BendlinesArr = swView.GetBendLines
                    For i = 0 To UBound(BendlinesArr)
                    Set swSketchSegment = BendlinesArr(i)
                    Debug.Print "             Is bend line " & i & " really a bend line? " & swSketchSegment.IsBendLine
```

```
                    ' Get the number of tangent lines related to
                    ' the bendline
                     nbrRelatedTangentEdges = swView.GetRelatedTangentEdgeCount(BendlinesArr(i))
                        Debug.Print "               Number of tangent edges for Bendline " & i & ": " & nbrRelatedTangentEdges
```

```
                        ' Get the tangent lines related to the bendline
                        If (nbrRelatedTangentEdges > 0) Then
                            RelatedTangentEdgesArr = swView.GetRelatedTangentEdges(BendlinesArr(i))
                            nbrRelatedTangentEdges = nbrRelatedTangentEdges - 1
                        End If
                    Next i
            End If
        End If
```

```
        ' Get next drawing view
        Set swView = swView.GetNextView
    Wend
```

```
End Sub
```
