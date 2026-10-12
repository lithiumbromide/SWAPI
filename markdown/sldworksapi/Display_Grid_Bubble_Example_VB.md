---
title: "Display Grid Bubble Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Grid_Bubble_Example_VB.htm"
---

# Display Grid Bubble Example (VBA)

This example shows how to set the text of ordinate dimensions and display a grid bubble at the end of each ordinate dimension extension line.

```
'--------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\2012-sm.slddrw.
'
' Postconditions:
' 1. Creates ordinate dimensions.
' 2. Selects the ordinate dimensions.
' 3. Sets the text of the ordinate dimensions to B and displays
'    a grid bubble at the end of each ordinate dimension's extension
'    line.
' 4. Examine the drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDim As SldWorks.DisplayDimension
Dim boolstatus As Boolean
Dim error As Long
Dim selType As Long
Dim i As Long
```

```
Sub SelectDimensions()
boolstatus = swModelDocExt.SelectByID2("D1@Sketch3@2012-sm.SLDDRW", "DIMENSION", 8.77948412666479E-02, 0.282838220689655, 0, False, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("D2@Sketch3@2012-sm.SLDDRW", "DIMENSION", 0.100748137818372, 0.284091765517241, 0, True, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("D3@Sketch3@2012-sm.SLDDRW", "DIMENSION", 0.115372827473544, 0.283256068965517, 0, True, 0, Nothing, 0)
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.ActiveDoc
    Set swDrawingDoc = swModelDoc
    Set swModelDocExt = swModelDoc.Extension
```

```
    'Add ordinate dimensions
    boolstatus = swDrawingDoc.ActivateView("Drawing View1")
    boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 8.69591447149237E-02, 0.257349475858578, -499.97349537912, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 0.101583834370096, 0.256931627582716, -499.97349537912, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 0.114954979197682, 0.256931627582716, -499.97349537912, True, 0, Nothing, 0)
    error = swModelDocExt.AddOrdinateDimension(swAddOrdinateDims_e.swHorizontalOrdinate, 8.65412964390616E-02, 0.280748979310345, 0)
```

```
    'Select the ordinate dimensions
    Set swSelMgr = swModelDoc.SelectionManager
    Call SelectDimensions
```

```
    'Change dimension values to letter B and
    'add grid bubble at end of extension lines
    Dim selCount As Long
    selCount = swSelMgr.GetSelectedObjectCount
    For i = 1 To selCount
        selType = swSelMgr.GetSelectedObjectType2(i)
        If selType = swSelDIMENSIONS Then
            Set swDisplayDim = swSelMgr.GetSelectedObject6(i, -1)
            swDisplayDim.SetText swDimensionTextAll, "B"
            swDisplayDim.GridBubble = True
        End If
    Next i
```

```
    swModelDoc.ClearSelection2 True
```

```
End Sub
```
