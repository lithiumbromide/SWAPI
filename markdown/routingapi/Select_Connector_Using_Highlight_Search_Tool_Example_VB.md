---
title: "Select Connector Using Highlight Search Tool Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Select_Connector_Using_Highlight_Search_Tool_Example_VB.htm"
---

# Select Connector Using Highlight Search Tool Example (VBA)

This example shows how to select a connector using the SOLIDWORKS Routing Highlight Search tool.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document containing an electrical route and
 '    connector (3pin) female-1.
 ' 2. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    click Launch Routing Library Manager and set the locations of your
 '    SOLIDWORKS Routing files.
 ' 4. In the IDE, click Tools > References, select
 '    SOLIDWORKS <version> Routing Type Library, and click OK.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Finds the specified component.
 ' 2. Prints the number of instances of the specified component.
 ' 3. Selects the component in the FeatureManager design tree.
 ' 4. Prints the number of components attached to the selected component.
 ' 5. Colors the selected component gray in the graphics area.
 ' 6. Inspect the Immediate window, the FeatureManager design tree,
 '    and the graphics area.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssemblyDoc As SldWorks.AssemblyDoc
 Dim rtRouteMgr As SWRoutingLib.RouteManager
 Dim rtAdvancedRouteSelector As SWRoutingLib.AdvancedRouteSelector
 Dim nbrConnectors As Long
 Dim selName As Variant
 Dim attachNames As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssemblyDoc = swModel
    ' Get SOLIDWORKS RouteManager
     Set rtRouteMgr = swAssemblyDoc.GetRouteManager()

    ' Access the Highlight Search tool
     Set rtAdvancedRouteSelector = rtRouteMgr.GetAdvancedRouteSelector

    ' Find the specified component and add it to the selection list
     nbrConnectors = rtAdvancedRouteSelector.Find("connector (3pin) female-1", swRoutingComponentSearch, True, False)
     Debug.Print "Number of instances of the specified component in this assembly: " & nbrConnectors

    ' Get the number of components attached to the selected component
     Debug.Print "Number of components attached to the specified connector: " & rtAdvancedRouteSelector.getAttachedComponentsCount(0)

    ' Color the selection gray
     rtAdvancedRouteSelector.SetSelectionColor True, 0

    ' Select the component and return an array of its attached components
     attachNames = rtAdvancedRouteSelector.Select(0, False, Nothing, swBoth, selName)

 End Sub
```
