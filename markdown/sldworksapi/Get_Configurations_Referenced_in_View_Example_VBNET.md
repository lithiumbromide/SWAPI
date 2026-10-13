---
title: "Get Configurations Referenced in View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configurations_Referenced_in_View_Example_VBNET.htm"
---

# Get Configurations Referenced in View Example (VB.NET)

This example shows how to get the names and persistent reference IDs of the configurations referenced in each drawing view in the first drawing sheet.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a drawing document with multiple
'    drawing views and multiple referenced
'    configurations in the first drawing sheet
'    in the drawing.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the drawing views in the first
'    drawing sheet and gets each drawing view's:
'    *  name
'    *  referenced model name
'    *  referenced configuration name and
'       persistent reference ID
' 2. Examine the Immediate window.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDraw As DrawingDoc
        Dim swView As View

        swModel = swApp.ActiveDoc
        swDraw = swModel
        Debug.Print("File = " & swModel.GetPathName)

        ' First drawing view is actually the first drawing sheet,
        ' so skip getting model name and configuration from
        ' the drawing sheet
        swView = swDraw.GetFirstView
        ' Get first drawing view in first drawing sheet
        swView = swView.GetNextView
        Do While Not swView Is Nothing
            Debug.Print("  Drawing view = " + swView.Name)
            Debug.Print("    Referenced model = " & swView.GetReferencedModelName)
            Debug.Print("    Referenced configuration name = " & swView.ReferencedConfiguration)
            Debug.Print("    Referenced configuration persistent reference ID = " & swView.ReferencedConfigurationID)
            'Get next drawing view
            swView = swView.GetNextView
        Loop

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
