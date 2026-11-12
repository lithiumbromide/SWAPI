---
title: "Automatically Insert Center Marks Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Auto_Insert_Center_Marks_Example_VBNET.htm"
---

# Automatically Insert Center Marks Example (VB.NET)

This example shows how to automatically insert center marks in multiple drawing views.

```
'----------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
'
' Postconditions:
' 1. Clears the Tools > Options > Document Properties > Centerlines/Center Marks >
'    Scale by view scale check box.
' 2. Activates Sheet3.
' 3. Suppresses Drawing View9.
' 4. Inserts center marks in Drawing View9 and Drawing View11.
' 5. Unsuppresses Drawing View9.
' 6. Examine the drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim Draw As DrawingDoc
    Dim ModelDocExt As ModelDocExtension
    Dim swActiveView As View
    Dim boolstatus As Boolean

    Sub main()

        Part = swApp.ActiveDoc
        Draw = Part
        ModelDocExt = Part.Extension

        ' Clear the Scale by view scale check box to set gap
        ModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDetailingCenterMarkScaleByViewScale, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)

        Draw.ActivateSheet("Sheet3")

        ' Suppress Drawing View9
        boolstatus = ModelDocExt.SelectByID2("Drawing View9", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
        Draw.SuppressView()

        ' Insert center marks for all holes, fillets, and slots in the specified views
	boolstatus = Draw.ActivateView("Drawing View9")
        swActiveView = Draw.ActiveDrawingView
        boolstatus = swActiveView.AutoInsertCenterMarks2(7, _
                                                       11, _
                                                       True, _
                                                       True, _
                                                       True, _
                                                       0.0025, _
                                                       0.0025, _
                                                       True, _
                                                       True, _
                                                       0)

        boolstatus = Draw.ActivateView("Drawing View11")
        swActiveView = Draw.ActiveDrawingView
        boolstatus = swActiveView.AutoInsertCenterMarks2(7, _
                                                       11, _
                                                       True, _
                                                       True, _
                                                       False, _
                                                       0.005, _
                                                       0.005, _
                                                       True, _
                                                       False, _
                                                       0)

        Part.ClearSelection2(True)

        ' Unsuppress Drawing View9
        boolstatus = ModelDocExt.SelectByID2("Drawing View9", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
        Draw.UnsuppressView()

    End Sub

    Public swApp As SldWorks

End Class
```
