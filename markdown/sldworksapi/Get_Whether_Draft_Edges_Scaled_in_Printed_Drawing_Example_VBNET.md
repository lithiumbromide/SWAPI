---
title: "Get Whether Draft Edges Scaled in Printed Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VBNET.htm"
---

# Get Whether Draft Edges Scaled in Printed Drawing Example (VB.NET)

This example shows how to get whether draft edges are scaled when printing a drawing in high quality.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Examine the Immediate window.
'------------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swDrawing As DrawingDoc
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swPageSetup As PageSetup
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swDrawing
        swModelDocExt = swModel.Extension
        swPageSetup = swModelDocExt.AppPageSetup
        If swPageSetup.HighQuality Then
            Debug.Print("Drawing set to print in high quality. Are draft edges scaled? " & swPageSetup.ScaleDraftEdges)
        Else
            Debug.Print("Drawing not set to print in high quality. Can only scale draft edges when drawing set to print in high quality.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
