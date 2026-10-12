---
title: "Delete Subassemblies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Subassemblies_Example_VB.htm"
---

# Delete Subassemblies Example (VBA)

This example shows how to delete the subassembly in which the selected subassembly is a component.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects and deletes the [Assem4^Assem3_assemSubAssems]<1>
'    subassembly and the subassembly in which it is a component.
' 3. Examine the FeatureManager design tree and Immediate
'    window.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assemSubAssems.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssembly = swModel
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Assem3^assemSubAssems-1@assemSubAssems/Assem4^Assem3_assemSubAssems-1@Assem3^assemSubAssems", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swAssembly.DeleteSelections(swAssemblyDeleteOptions_e.swDelete_SubAssembly)
    Debug.Print "Selected subassembly and the subassembly in which it is a component deleted? " & status
```

```
End Sub
```
