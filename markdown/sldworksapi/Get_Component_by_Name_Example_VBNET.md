---
title: "Get Component by Name Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_by_Name_Example_VBNET.htm"
---

# Get Component by Name Example (VB.NET)

This examples shows how to get a component by name and to determine if that component is fixed or floating.

```
'-------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\EDraw\claw\claw-mechanism.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the specified component.
' 2. Gets whether the specified component is fixed.
' 3. Examine the Immediate window.
'-------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swAssy As AssemblyDoc
    Dim swComp As Component2

    Public Sub main()

        swModel = swApp.ActiveDoc
        swAssy = swModel
        Dim CompName As String
        CompName = "center-1"
        swComp = swAssy.GetComponentByName(CompName)
        Debug.Print("Is component fixed: " & swComp.IsFixed)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
