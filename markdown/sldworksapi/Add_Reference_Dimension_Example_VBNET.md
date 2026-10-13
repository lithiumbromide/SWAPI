---
title: "Add Reference Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Reference_Dimension_Example_VBNET.htm"
---

# Add Reference Dimension Example (VB.NET)

This example shows how to add a reference dimension to a model in a drawing.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Activates a drawing view, selects an edge on the model, and
'    creates a dimension.
' 3. Prints to the Immediate window whether the dimension
'    is a reference dimension.
' 4. Examine the Immediate window.
'
' NOTE: Because the drawing document is used elsewhere, do not
' save any changes.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDrawingDoc As DrawingDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swDisplayDimension As DisplayDimension
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20.SLDDRW"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swDrawingDoc = swModel
        swModelDocExt = swModel.Extension

        status = swDrawingDoc.ActivateView("Drawing View1")
        status = swModelDocExt.SelectByID2("", "EDGE", 0.512187343878665, 0.498697444621999, 249.953027873291, False, 0, Nothing, 0)
        swDisplayDimension = swModelDocExt.AddDimension(0.698326046410311, 0.699228314873418, 0, swSmartDimensionDirection_e.swSmartDimensionDirection_Up)
        Debug.Print("Is reference dimension? " & swDisplayDimension.IsReferenceDim)

        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
