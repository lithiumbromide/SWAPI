---
title: "Get and Set Routing Component Grouping Options for BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_VB.htm"
---

# Get and Set Routing Component Grouping Options for BOM Table Example (VBA)

This example shows how to get and set the routing component grouping options for this BOM table in a drawing of an assembly containing routing components.

```
'----------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\AutoRouteThroughSketchEntities.sldddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the Bill of Materials1 feature.
' 2. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swBomFeature As SldWorks.BomFeature
    Dim status As Boolean
    Dim options As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    status = swModelDocExt.SelectByID2("Bill of Materials1", "BOMFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swBomFeature = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "Name of configuration used for BOM table: " & swBomFeature.Configuration
```

```
    'Get current routing component grouping options
    Debug.Print "Current routing component grouping options: " & swBomFeature.RoutingComponentGrouping
```

```
    'Set new routing component grouping options
    options = swRoutingComponentGroupingOption_e.swShowOnlyRoutingComponentsInBOM + swRoutingComponentGroupingOption_e.swDisplayUnitsInBOM
    swBomFeature.RoutingComponentGrouping = options
    Debug.Print "Modified routing component grouping options: " & swBomFeature.RoutingComponentGrouping

End Sub
```
