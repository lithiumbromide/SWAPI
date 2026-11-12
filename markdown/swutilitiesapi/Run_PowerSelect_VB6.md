---
title: "Run PowerSelect Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Run_PowerSelect_VB6.htm"
---

# Run PowerSelect Example (VBA)

This example shows how to initialize, run, and close a PowerSelect session using the SOLIDWORKS Utilities API.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
'
' Postconditions:
' 1. Runs PowerSelect and selects the specified types of edges.
' 2. Examine the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swUtil As SWUtilities.gtcocswUtilities
    Dim swUtilPowerSelect As SWUtilities.gtcocswPowerSelect
    Dim errorcode As gtError_e
    Dim EntityCounts As Variant
```

```
    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks
```

```
    ' Get the SOLIDWORKS Utilities interface
    Set swUtil = swApp.GetAddInObject("Utilities.UtilitiesApp")
    Set swUtilPowerSelect = swUtil.GetToolInterface(gtSwToolPowerSelect, errorcode)
```

```
    ' Initialize PowerSelect
    errorcode = swUtilPowerSelect.Init()
```

```
    ' Set the types of entities to select
    errorcode = swUtilPowerSelect.SetSelectEntitiesTypes(gtPslSelectionType_Edge)

    ' Set the types of edges to select
    errorcode = swUtilPowerSelect.SetEdgeConvexityFilter(True, True, False)
```

```
    ' Run PowerSelect
    EntityCounts = swUtilPowerSelect.RunPowerSelect(False, errorcode)
```

```
    ' Select the PowerSelect results
    errorcode = swUtilPowerSelect.SelectResults()

    ' Close this PowerSelect session
    errorcode = swUtilPowerSelect.Close()
```

```
End Sub
```
