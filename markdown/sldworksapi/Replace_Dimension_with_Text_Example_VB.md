---
title: "Replace Dimension with Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Dimension_with_Text_Example_VB.htm"
---

# Replace Dimension with Text Example (VBA)

This example shows how to temporarily replace the selected dimension with text.

```
'----------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
'
' Postconditions:
' 1. Selects a dimension.
' 2. Replaces the selected dimension with display text.
' 3. Reselects the dimension.
' 4. Examine drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
    Dim model As SldWorks.ModelDoc2
    Dim selMgr As SldWorks.SelectionMgr
    Dim selObj As Object
    Dim selType As Long, selCount As Long
    Dim selDim As SldWorks.DisplayDimension
    Dim textFont As SldWorks.TextFormat
    Dim entType As Long
    Dim triData(0 To 8) As Double, vEntData As Variant
    Dim dotData(0 To 3) As Double, arcData(0 To 11) As Double, textPos(0 To 2) As Double
    Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set model = swApp.ActiveDoc
    Set selMgr = model.SelectionManager
    boolstatus = model.Extension.SelectByID2("RD19@Drawing View1", "DIMENSION", 0.277820016554234, 0.29219884729064, 0, False, 0, Nothing, 0)
    selCount = selMgr.GetSelectedObjectCount()
    If selCount > 0 Then
        selType = selMgr.GetSelectedObjectType3(1, -1)
        Set selObj = selMgr.GetSelectedObject6(1, -1)
        If selType = SwConst.swSelDIMENSIONS Then
            Set selDim = selObj
            triData(0) = 0.12
            triData(1) = 0.1
            triData(2) = 0#
            triData(3) = 0.15
            triData(4) = 0.1
            triData(5) = 0#
            triData(6) = 0.13
            triData(7) = 0.13
            triData(8) = 0#
            vEntData = triData
            boolstatus = selDim.AddDisplayEnt(2, (vEntData))    ' Filled triangle
            dotData(0) = 0.11
            dotData(1) = 0.14
            dotData(2) = 0#
            dotData(3) = 0.005
            vEntData = dotData
            boolstatus = selDim.AddDisplayEnt(6, (vEntData))    ' Filled dot
            dotData(0) = 0.16
            dotData(1) = 0.14
            dotData(2) = 0#
            dotData(3) = 0.009
            vEntData = dotData
            boolstatus = selDim.AddDisplayEnt(6, (vEntData))    ' Filled dot
            arcData(0) = 0.135
            arcData(1) = 0.11
            arcData(2) = 0#
            arcData(3) = 0#
            arcData(4) = 0#
            arcData(5) = 1#
            arcData(6) = 0.09
            arcData(7) = 0.11
            arcData(8) = 0#
            arcData(9) = 0.18
            arcData(10) = 0.11
            arcData(11) = 0#
            vEntData = arcData
            boolstatus = selDim.AddDisplayEnt(4, (vEntData))    ' Arc
            textPos(0) = 0.09
            textPos(1) = 0.065
            textPos(2) = 0#
            vEntData = textPos
            Set textFont = model.GetUserPreferenceTextFormat(SwConst.swDetailingDimensionTextFormat)
            textFont.CharHeightInPts = 48
            boolstatus = selDim.AddDisplayText("Hi!", (vEntData), textFont, SwConst.swTextJustificationCenter, 1#)
        End If
    End If
```

```
    model.ClearSelection2 True
    boolstatus = model.Extension.SelectByID2("RD19@Drawing View1", "DIMENSION", 0.277820016554234, 0.29219884729064, 0, False, 0, Nothing, 0)
```

```
End Sub
```
