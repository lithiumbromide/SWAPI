---
title: "Make Component Independent Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Component_Independent_Example_VBNET.htm"
---

# Make Component Independent Example (VB.NET)

This example shows how to:

- make a selected component independent.
- save the selected component as a new part.
- reference the new part in the assembly.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Verify that c:\temp exists.
' 2. Copy these files from public_documents\samples\tutorial\driveworksxpress
'    to c:\temp:
'    * leg.sldprt
'    * mobile gantry.sldasm
'    * universal beam.sldpart
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects the leg<1> component.
' 3. Makes the selected component independent, saves the component as
'    a new part, c:\temp\my leg.sldprt, and references the new part in
'    the assembly.
' 4. Examine the FeatureManager design tree and c:\temp.
'------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssembly As AssemblyDoc
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "c:\temp\mobile gantry.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swAssembly = swModel

        'Select leg<1>
        status = swModelDocExt.SelectByID2("leg-1@mobile gantry", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

        'Make leg<1> independent, save it as a new part,
        'and reference the new part in the assembly
        status = swAssembly.MakeIndependent("c:\temp\my leg.sldprt")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
