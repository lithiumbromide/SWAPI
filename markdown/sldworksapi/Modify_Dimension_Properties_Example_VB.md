---
title: "Modify Dimension Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Dimension_Properties_Example_VB.htm"
---

# Modify Dimension Properties Example (VBA)

This example shows how to modify the properties of a selected display dimension in a drawing.

```
'------------------------------------------------------
' Preconditions:
' 1. Open a drawing document with one or more display
'    dimensions.
' 2. Select a display dimension.
'
' Postconditions:
' 1. The properties of the selected display dimension
'    are modified as specified.
' 2. Examine the display dimension to verify.
' -----------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim boolstatus As Boolean
```

```
Option Explicit

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    boolstatus = swModelDocExt.EditDimensionProperties(swTolBASIC, 0, 0, "", "", True, 9, swDimArrowsSmart, False, swSLASH_ARROWHEAD, swSLASH_ARROWHEAD, "", "", True, "", "", "Example of lower text", True, swThisConfiguration, "")

    swModel.ClearSelection2 True
```

```
End Sub
```
