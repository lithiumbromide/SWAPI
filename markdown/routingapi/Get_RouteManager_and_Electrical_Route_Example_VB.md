---
title: "Get RouteManager and Electrical Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_RouteManager_and_Electrical_Route_Example_VB.htm"
---

# Get RouteManager and Electrical Route Example (VBA)

This example shows how to get the RouteManager from an assembly and then how to get the electrical route.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document that contains a routing assembly.
 ' 2. Select a component representing a routing assembly.
 '
 ' Postconditions: None
 '---------------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Sub Main()

    Dim swModel              As SldWorks.ModelDoc2
    Dim swTopLevelAssembly   As SldWorks.AssemblyDoc
    Dim swRoutingAssembly    As SldWorks.AssemblyDoc
    Dim rtRouteManager       As SWRoutingLib.RouteManager
    Dim swComponent          As SldWorks.Component2
    Dim rtElectricalRoute    As SWRoutingLib.ElectricalRoute
    Dim bRetVal              As Boolean

    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks

    ' Get the active document
    Set swModel = swApp.ActiveDoc

    ' Downcast from model document to assembly document
    Set swTopLevelAssembly = swModel

    ' Select the component that represents a routing assembly
    Set swComponent = swModel.SelectionManager.GetSelectedObject6(1, 0)

    If swComponent Is Nothing Then
        Debug.Print "No component selected"
        Exit Sub
    End If

    ' Get the assembly document for this component
    Set swRoutingAssembly = swComponent.GetModelDoc

    ' Get the RouteManager from the routing assembly
    Set rtRouteManager = swRoutingAssembly.GetRouteManager

    If rtRouteManager Is Nothing Then
        Debug.Print "No RouteManager found in sub-assembly document: " & swRoutingAssembly.GetPathName
        Exit Sub
    End If

    '
    ' Must be editing component for route properties to be available
    '

    ' Clear selection
    swModel.ClearSelection2 True

    ' Make sure the component representing the routing assembly is selected
    bRetVal = swComponent.Select3(True, Nothing)

    ' Start editing the routing assembly
    swTopLevelAssembly.EditAssembly

    ' Get the electrical route
    Set rtElectricalRoute = rtRouteManager.GetElectricalRoute

    ' Check for an electrical route
    If rtElectricalRoute Is Nothing Then
        Debug.Print "No electrical route found."
    Else
        Debug.Print "Electrical route found."

        Debug.Print "Number of cables = " & rtElectricalRoute.GetCablesCount
        Debug.Print "Number of wires  = " & rtElectricalRoute.GetWiresCount

        '
        ' Make edits ...
        '

    End If

    ' Return to editing the top-level assembly
    swTopLevelAssembly.EditAssembly

End Sub
```
