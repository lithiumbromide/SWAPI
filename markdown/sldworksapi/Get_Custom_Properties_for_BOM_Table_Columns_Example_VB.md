---
title: "Get Custom Properties for BOM Table Columns Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_for_BOM_Table_Columns_Example_VB.htm"
---

# Get Custom Properties for BOM Table Columns Example (VBA)

This example shows how to get the custom properties used to fill columns in a BOM table.

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
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swBOMTableAnnotation As SldWorks.BomTableAnnotation
Dim swTableAnnotation As SldWorks.TableAnnotation
Dim status As Boolean
Dim anchorType As Long
Dim bomType As Long
Dim errors As Long
Dim warnings As Long
Dim tableTemplate As String
Dim config As String
Dim i As Long
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
    status = swDrawing.ActivateView("Drawing View1")
    Set swView = swDrawing.ActiveDrawingView
```

```
    ' Insert indented BOM table and get custom properties for each column in BOM table
    anchorType = swBOMConfigurationAnchor_TopLeft
    bomType = swBomType_Indented
    tableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
    config = ""
    Set swBOMTableAnnotation = swView.InsertBomTable4(False, 0.4, 0.3, anchorType, bomType, config, tableTemplate, False, swNumberingType_Detailed, True)
    Set swTableAnnotation = swBOMTableAnnotation
    For i = 0 To swTableAnnotation.ColumnCount
        Debug.Print "  Column(" & i & ") = " & swBOMTableAnnotation.GetColumnCustomProperty(i)
    Next i
```

```
    swDrawing.ForceRebuild
```

```
End Sub
```
