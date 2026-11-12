---
title: "Display Elevation Symbol Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Elevation_Symbol_Example_VB.htm"
---

# Display Elevation Symbol Example (VBA)

This example shows how to display an elevation symbol at the end of each ordinate dimension extension line in a part.

```vb
'-----------------------------------------------------
'
' Preconditions: Part document called Block.SLDPRT is
                 open and contains the selected dimensions.
'
' Postconditions: An elevation symbol and the word "Dowel" are displayed
                 at the end of each extension line of each selected dimension.
'
'------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDim As SldWorks.DisplayDimension
Dim boolstatus As Boolean
Dim longstatus As Long
Dim longwarnings As Long
Dim selType As Long
Dim i As Long

Sub SelectDimensions()
    boolstatus = swModelDocExt.SelectByID2("D1@Sketch1@Block.SLDPRT", "DIMENSION", -0.1000132239804, 0.1006163020026, 0.015, True, 0, Nothing, swSelectOptionDefault)
    boolstatus = swModelDocExt.SelectByID2("D2@Sketch1@Block.SLDPRT", "DIMENSION", -0.06157715941924, 0.1015772036167, 0.015, True, 0, Nothing, swSelectOptionDefault)
    boolstatus = swModelDocExt.SelectByID2("D3@Sketch1@Block.SLDPRT", "DIMENSION", -0.02362154566506, 0.1054208100728, 0.015, True, 0, Nothing, swSelectOptionDefault)
    boolstatus = swModelDocExt.SelectByID2("D4@Sketch1@Block.SLDPRT", "DIMENSION", 0.01481451889614, 0.1063817116868, 0.015, True, 0, Nothing, swSelectOptionDefault)
    boolstatus = swModelDocExt.SelectByID2("D5@Sketch1@Block.SLDPRT", "DIMENSION", 0.04940697700122, 0.1063817116868, 0.015, True, 0, Nothing, swSelectOptionDefault)
    boolstatus = swModelDocExt.SelectByID2("D6@Sketch1@Block.SLDPRT", "DIMENSION", 0.08592123833436, 0.1068621624938, 0.015, True, 0, Nothing, swSelectOptionDefault)
End Sub

Sub main()
    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.ActiveDoc
    Set swModelDocExt = swModelDoc.Extension
    Set swSelMgr = swModelDoc.SelectionManager

    swModelDoc.ClearSelection2 True

    Call SelectDimensions

    Dim selCount As Long
    selCount = swSelMgr.GetSelectedObjectCount

    For i = 1 To selCount

        selType = swSelMgr.GetSelectedObjectType2(i)

        If selType = swSelDIMENSIONS Then

            Set swDisplayDim = swSelMgr.GetSelectedObject5(i)

            swDisplayDim.SetText swDimensionTextAll, "Dowel"
            swDisplayDim.EndSymbol = swOrdDimEndSymbol_Dowel
            swDisplayDim.Elevation = True

        End If

    Next i

    swModelDoc.ClearSelection2 True

End Sub
```
