---
title: "Get Available Custom Properties for BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Available_Custom_Properties_for_BOM_Table_Example_VB.htm"
---

# Get Available Custom Properties for BOM Table Example (VBA)

This example shows how to get a list of all of the custom properties available to a BOM table.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Specified drawing and BOM table template exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts an indented BOM table.
' 3. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save any changes.
'---------------------------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swBOMAnnotation As SldWorks.BomTableAnnotation
Dim status As Boolean
Dim anchorType As Long
Dim bomType As Long
Dim errors As Long
Dim warnings As Long
Dim tableTemplate As String
Dim customPropArray As Variant
Dim config As String
Dim customProp As Variant
```

```
Option Explicit
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawing = swModel
    Set swModelDocExt = swModel.Extension
    status = swDrawing.ActivateView("Drawing View1")
    Set swView = swDrawing.ActiveDrawingView
```

```
    ' Insert indented BOM table and get available custom properties
    anchorType = swBOMConfigurationAnchor_TopLeft
    bomType = swBomType_Indented
    tableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
    config = ""
    Set swBOMAnnotation = swView.InsertBomTable4(False, 0.4, 0.3, anchorType, bomType, config, tableTemplate, False, swNumberingType_Detailed, True)
    customPropArray = swBOMAnnotation.GetAllCustomProperties
    For Each customProp In customPropArray
        Debug.Print "  " & customProp
    Next customProp
```

```
    swDrawing.ForceRebuild
```

```
End Sub
```
