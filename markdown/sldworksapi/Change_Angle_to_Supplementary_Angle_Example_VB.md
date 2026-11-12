---
title: "Change Angle to Supplementary Angle Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Angle_to_Supplementary_Angle_Example_VB.htm"
---

# Change Angle to Supplementary Angle Example (VBA)

This example shows how to change the angle in an angular dimension to its supplementary angle.

```
'-----------------------------------------------------------
' Preconditions: Verify that the drawing exists.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Selects the angular dimension.
' 3. Changes the angle to its supplementary angle.
' 4. Examine the graphics area.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim status As Boolean
Dim warnings As Long
Dim errors As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Select angular dimension
    status = swModelDocExt.SelectByID2("RD1@Drawing View1", "DIMENSION", 0.115166498498499, 0.167429477477477, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swDisplayDimension = swSelectionMgr.GetSelectedObject6(1, -1)
```

```
    'Change angle to supplementary angle
    status = swDisplayDimension.SupplementaryAngle
```

```
End Sub
```
