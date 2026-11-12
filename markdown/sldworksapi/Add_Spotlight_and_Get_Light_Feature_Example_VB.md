---
title: "Add Spotlight and Get Light Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Spotlight_and_Get_Light_Feature_Example_VB.htm"
---

# Add Spotlight and Get Light Feature Example (VBA)

This example shows how to add a spotlight to a model and get its light feature.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Adds a spotlight.
' 3. Gets the spotlight's feature and prints its ID to
'    the Immediate window.
' 4. Examine the Immediate window, FeatureManager design tree, and
'    graphics area.
'
' NOTE: Because this assembly document is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swModelView As SldWorks.ModelView
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swLight As SldWorks.Light
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim rect As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\appearances\usb_flash_drive1.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Add spotlight
    status = swModel.AddLightSource("SW#5", 2, "Spot1")
    status = swModel.SetLightSourcePropertyValuesVB("SW#5", 2, 0.5, 8454143, 1, -9.99999999999991E-02, 0.170000000000101, 1.10999999999999, 0.179999999999999, -9.00000000001008E-02, -1.02999999999999, 45, 0, 0, 0, 0.4, 0.4, 0, False)
    status = swModel.LockLightToModel(4, True)
    Set swModelView = swModel.ActiveView
    swModelView.GraphicsRedraw (rect)
```

```
    'Get spotlight's feature ID
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Spot1", "LIGHTS", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swLight = swFeature.GetSpecificFeature2
    Debug.Print "Light ID: " & swLight.GetID
```

```
End Sub
```
