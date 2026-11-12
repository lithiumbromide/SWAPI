---
title: "Automatically Solve Equations in Sequence Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Automatically_Solve_Equations_in_Sequence_Example_VBNET.htm"
---

# Automatically Solve Equations in Sequence Example (VB.NET)

This example shows how to automatically sequence the equations in an order determined to produce accurate results.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sets the equation's Automatic solve order option
'    to true, which results in the model's
'    independent equations executing before
'    dependent equations, if any.
' 2. Examine the Immediate window.
'
' NOTE: Because this model is used elsewhere,
' do save changes.
'-----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swEquationMgr As EquationMgr
        Dim fileName As String
        Dim errors As Integer, warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\partEquations.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swEquationMgr = swModel.GetEquationMgr
        'Make sure that this model includes equations
        'by getting the number of equations
        Debug.Print("Number of equations: " & swEquationMgr.GetCount)
        If swEquationMgr.GetCount >= 1 Then
            'Get whether equations are automatically
            'solved in sequence
            Debug.Print("  Are equations automatically solved in sequence? " & swEquationMgr.AutomaticSolveOrder)
            If swEquationMgr.AutomaticSolveOrder Then
                Exit Sub
            Else
                'Automatically solve equations in sequence
                swEquationMgr.AutomaticSolveOrder = True
                Debug.Print("  Are equations automatically solved in sequence? " & swEquationMgr.AutomaticSolveOrder)
            End If
        Else
            Debug.Print("No equations included with this model.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
