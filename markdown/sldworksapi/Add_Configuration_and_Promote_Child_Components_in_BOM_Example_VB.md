---
title: "Add Configuration and Promote Child Components in BOM Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VB.htm"
---

# Add Configuration and Promote Child Components in BOM Example (VBA)

This example shows how to add a configuration to an assembly and promote its child components one level in a BOM.

```
'----------------------------------------
' Preconditions:
' 1. Specified assembly document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Adds a new configuration named Config2.
' 3. Sets the option to dissolve the assembly's
'    configuration when it appears in a BOM and
'    promote all of its child components one level.
' 4. To verify, examine the option value printed to
'    the Immediate window.
'
' NOTE: Because this assembly document is used
' elsewhere, do not save changes when closing it.
'----------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swAssembly As SldWorks.AssemblyDoc
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swConfig As SldWorks.Configuration
Dim fileName As String
Dim status As Boolean
Dim errors As Long, warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm"
    Set swAssembly = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swAssembly

    'Add configuration named Config2
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("bowl and chute.SLDASM", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swConfig = swModel.AddConfiguration3("Config2", "", "", swConfigurationOptions2_e.swConfigOption_DoDisolveInBOM + swConfigurationOptions2_e.swConfigOption_DontShowPartsInBOM)
```

```
    'Dissolve the assembly's configuration
    'when it appears in a BOM and promote all of
    'its child components one level
    swConfig.ChildComponentDisplayInBOM = swChildComponentInBOMOption_e.swChildComponent_Promote
    Debug.Print ("Child component display option in BOM: " & swConfig.ChildComponentDisplayInBOM)
```

```
End Sub
```
