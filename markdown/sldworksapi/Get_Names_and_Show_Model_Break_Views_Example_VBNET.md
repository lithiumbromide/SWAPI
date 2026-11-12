---
title: "Get Names and Show Model Break Views Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_and_Show_Model_Break_Views_Example_VBNET.htm"
---

# Get Names and Show Model Break Views Example (VB.NET)

This example shows how to:

- get the names of the Model Break Views in the current configuration of an active model.
- show one of the Model Break Views.

```
'--------------------------------------
' Preconditions:
' 1. Open a part document with multiple
'    hidden Model Break Views.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number and names of the Model Break
'    Views in the current configuration of the
'    active model.
' 2. Shows one of the Model Break Views.
' 3. Examine the Immediate window and the
'    graphics area.
'----------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim names As Object
    Dim nbr As Integer
    Dim i As Integer

    Public Sub Main()

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        'Get and print number and names of Model Break
        'Views in current configuration of the active
        'model
        nbr = swModelDocExt.GetModelBreakViewNames(names)

        Debug.Print("Model Break Views:")
        Debug.Print("  Number: " & nbr)
        Debug.Print("  Names: ")
        For i = 0 To (nbr - 1)
            Debug.Print("    " & names(i))
        Next
        'Show Model Break View
        swModelDocExt.ShowModelBreakView(True, names(nbr - 1))

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
