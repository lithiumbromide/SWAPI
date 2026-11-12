---
title: "Set Override Option for Auto Relief Default Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_VB.htm"
---

# Set Override Option for Auto Relief Default Parameters Example (VBA)

This example shows how to set the override option for the auto relief default parameters of a sheet metal feature in a multibody sheet metal part.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a multibody sheet metal part that contains
'    a Sheet-Metal3 feature in the Sheet-Metal folder.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether the default parameters are overridden
'    for Sheet-Metal3.
' 2. Sets the override option for the auto relief default
'    parameters of Sheet-Metal3.
' 3. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swSheetMetalFeatureData As SldWorks.SheetMetalFeatureData
Dim errors As Long
Dim status As Boolean
Dim override As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Sheet-Metal3", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swSheetMetalFeatureData = swFeature.GetDefinition
    Debug.Print ("Get override parameter values for Sheet-Metal3:")
    errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_BendParameters, override)
    Debug.Print ("  Bend parameters: " & override)
    errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_BendAllowance, override)
    Debug.Print ("  Bend allowance: " & override)
    errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, override)
    Debug.Print ("  Auto relief: " & override)
    swSheetMetalFeatureData.AccessSelections swModel, Nothing
    If override Then
        errors = swSheetMetalFeatureData.SetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, False)
    Else
        errors = swSheetMetalFeatureData.SetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, True)
    End If
    swFeature.ModifyDefinition swSheetMetalFeatureData, swModel, Nothing
    errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, override)
    Debug.Print ("Override auto relief default parameters for Sheet-Metal3?  " & override)
```

```
End Sub
```
