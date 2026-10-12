---
title: "Swap To and From Components on Each Wire Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm"
---

# Swap To and From Components on Each Wire Example (VBA)

This example shows how to swap the "to" and "from" components on each wire.

```vb
 '--------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document that contains a routing assembly.
 ' 2. Select a component representing a routing assembly.
 '
 ' Postconditions: "To" and "from" components are swapped.
 '--------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Sub Main()
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swTopLevelAssembly      As SldWorks.AssemblyDoc
    Dim swRoutingAssembly       As SldWorks.AssemblyDoc
    Dim rtRouteManager          As SWRoutingLib.RouteManager
    Dim swComponent             As SldWorks.Component2
    Dim rtElectricalRoute       As SWRoutingLib.ElectricalRoute
    Dim bRetVal                 As Boolean
    Dim vWires                  As Variant
    Dim vWire                   As Variant
    Dim rtWire                  As SWRoutingLib.Wire
    Dim strNewWireName          As String
    Dim strNewToComponent       As String
    Dim strNewFromComponent     As String
    Dim strNewToPin             As String
    Dim strNewFromPin           As String

    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks

    ' Get the active document
    Set swModel = swApp.ActiveDoc

    ' Downcast from model document to assembly document
    Set swTopLevelAssembly = swModel

    ' Select the component that represents a routing assembly
    Set swComponent = swModel.SelectionManager.GetSelectedObject6(1, 0)

    If swComponent Is Nothing Then
        Debug.Print "No component selected."
        Exit Sub
    End If

    ' Get the assembly document for this component
    Set swRoutingAssembly = swComponent.GetModelDoc

    ' Get the RouteManager from the routing assembly
    Set rtRouteManager = swRoutingAssembly.GetRouteManager

    If rtRouteManager Is Nothing Then
        Debug.Print "No route manager found in sub-assembly document: " & swRoutingAssembly.GetPathName
        Exit Sub
    End If

    '
    ' Must be editing component for route properties to be available
    '

    ' Clear selection
    swModel.ClearSelection2 True

    ' Make sure that the component representing the routing assembly is selected
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

        '
        ' Swap "to" and "from" component on each wire
        '

        ' Get the wires
        vWires = rtElectricalRoute.GetWires

        ' Loop over the wires.
        If Not IsEmpty(vWires) Then
            For Each vWire In vWires
                Set rtWire = vWire
                Debug.Assert (Not rtWire Is Nothing)

                ' Give the wire a new name
                strNewWireName = rtWire.UserName & "-swapped"

                rtWire.UserName = strNewWireName

                ' Swap references
                strNewToComponent = rtWire.FromComponentReference
                strNewToPin = rtWire.FromPinReference
                strNewFromComponent = rtWire.ToComponentReference
                strNewFromPin = rtWire.ToPinReference

                rtWire.FromComponentReference = strNewFromComponent
                rtWire.FromPinReference = strNewFromPin

                rtWire.ToComponentReference = strNewToComponent
                rtWire.ToPinReference = strNewToPin

            Next vWire

            ' Commit the changes
            bRetVal = rtElectricalRoute.RouteWires
            If bRetVal = False Then
                Debug.Print "Routing of wires failed."
            Else
                Debug.Print "Routing of wires successful."
            End If

        End If

    End If

    ' Return to editing the top-level assembly
    swTopLevelAssembly.EditAssembly

End Sub
```
