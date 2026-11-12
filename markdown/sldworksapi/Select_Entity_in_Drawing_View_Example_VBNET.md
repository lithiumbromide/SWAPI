---
title: "Select Entity in Drawing View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Entity_in_Drawing_View_Example_VBNET.htm"
---

# Select Entity in Drawing View Example (VB.NET)

This example shows how to select a model face, edge, or vertex in a drawing view and dimension it.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Const sPathToTemplate As String = "C:\ProgramData\SolidWorks\SOLIDWORKS 2016\data\templates\drawing.drwdot"
         Const nYoffset As Double = 0.01

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swEnt As Entity

         Dim swDraw As DrawingDoc
         Dim swDrawModel As ModelDoc2
         Dim swView As View
         Dim vOutline As Object
         Dim swDispDim As DisplayDimension

         Dim nXpos As Double
         Dim nYpos As Double

         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swEnt = swSelMgr.GetSelectedObject6(1, -1)

         If Not swEnt Is Nothing Then

             swDraw = swApp.NewDrawing2(swDwgTemplates_e.swDwgTemplateCustom, sPathToTemplate, swDwgPaperSizes_e.swDwgPaperA1size, 0.0#, 0.0#)
             swDrawModel = swDraw

             bRet = swDraw.Create3rdAngleViews2(swModel.GetPathName)

             swView = swDraw.GetFirstView
             swView = swView.GetNextView

             bRet = swView.SelectEntity(swEnt, False)

             ' Work out where to place dimension -
             ' midway across view and slightly above
             vOutline = swView.GetOutline
             nXpos = (vOutline(0) + vOutline(2)) / 2.0#
             nYpos = vOutline(3) + nYoffset

             ' Create the dimension, even if the entity is not
             ' visible in the drawing view
             swDispDim = swDrawModel.Extension.AddDimension(nXpos, nYpos, 0.0#, swSmartDimensionDirection_e.swSmartDimensionDirection_Left)

         End If

     End Sub

     Public swApp As SldWorks

 End Class
```
