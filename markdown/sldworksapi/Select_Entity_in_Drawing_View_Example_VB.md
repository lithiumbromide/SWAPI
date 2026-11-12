---
title: "Select Entity in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Entity_in_Drawing_View_Example_VB.htm"
---

# Select Entity in Drawing View Example (VBA)

This example shows how to select a model face, edge, or vertex in a drawing view and dimension it.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part or fully resolved assembly.
' 2. Verify that the specified template exists.
' 3. Select a face, edge, or vertex.
'
' Postconditions:
' 1. Creates a new drawing with three views.
' 2. Dimensions the selected face, edge, or vertex
'    in the first drawing view.
' 3. Examine the drawing.
'
' NOTE: The dimension is not guaranteed to be created if a face is selected.
'----------------------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Const sPathToTemplate       As String = "C:\ProgramData\SolidWorks\SOLIDWORKS 2016\data\templates\drawing.drwdot"
     Const nYoffset              As Double = 0.01
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swEnt                   As SldWorks.Entity
    Dim swDraw                  As SldWorks.DrawingDoc
     Dim swDrawModel             As SldWorks.ModelDoc2
     Dim swView                  As SldWorks.View
     Dim vOutline                As Variant
     Dim swDispDim               As SldWorks.DisplayDimension
    Dim nXpos                   As Double
     Dim nYpos                   As Double
    Dim bRet                    As Boolean
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swEnt = swSelMgr.GetSelectedObject6(1, -1)

    If Not swEnt Is Nothing Then
        Set swDraw = swApp.NewDrawing2(swDwgTemplateCustom, sPathToTemplate, swDwgPaperA1size, 0#, 0#)
         Set swDrawModel = swDraw

        bRet = swDraw.Create3rdAngleViews2(swModel.GetPathName)

        Set swView = swDraw.GetFirstView
         Set swView = swView.GetNextView

        bRet = swView.SelectEntity(swEnt, False)

        ' Work out where to place dimension -
         ' midway across view and slightly above
         vOutline = swView.GetOutline
         nXpos = (vOutline(0) + vOutline(2)) / 2#
         nYpos = vOutline(3) + nYoffset

        ' Create the dimension, even if the entity is not
         ' visible in the drawing view
         Set swDispDim = swDrawModel.Extension.AddDimension(nXpos, nYpos, 0#, swSmartDimensionDirection_Left)

    End If
End Sub
```
