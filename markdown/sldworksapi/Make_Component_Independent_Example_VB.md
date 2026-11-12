---
title: "Make Component Independent Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Component_Independent_Example_VB.htm"
---

# Make Component Independent Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "c:\temp\mobile gantry.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swAssembly = swModel
```

```
    'Select leg<1>
    status = swModelDocExt.SelectByID2("leg-1@mobile gantry", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
    'Make leg<1> independent, save it as a new part,
    'and reference the new part in the assembly
    status = swAssembly.MakeIndependent("c:\temp\my leg.sldprt")
```

```
End Sub
```
