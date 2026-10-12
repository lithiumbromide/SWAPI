---
title: "Set New Route Paths for Wires Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Set_New_Route_Paths_for_Wires_Example_VB.htm"
---

# Set New Route Paths for Wires Example (VBA)

This example shows how to set new route paths for wires.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
'   (in the IDE select Tools > References).
' 3. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
' 4. Open the Immediate window.
' 5. Run the macro.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere, do not save
' any changes when saving it.
'---------------------------------------------------------------------------

Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDoc As SldWorks.ModelDocExtension
    Dim swTopLevelAssembly As SldWorks.AssemblyDoc
    Dim rtRouteManager As SWRoutingLib.RouteManager
    Dim rtElectricalRoute As SWRoutingLib.electricalRoute
    Dim rtWire As SWRoutingLib.Wire
    Dim status As Boolean
    Dim count As Long
    Dim wires As Variant
    Dim cableName As String
    Dim cuttingLength As Double
    Dim routePathStatus As Long
    Dim routeSegmentIDs As Variant
    Dim routeSegmentIDsCount As Long
    Dim i As Long
    Dim j As Long
    Dim k As Long
```

```
    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks
```

```
    ' Get the active document
    Set swModel = swApp.ActiveDoc
    Set swModelDoc = swModel.Extension
```

```
    ' Downcast from model document to assembly document
    Set swTopLevelAssembly = swModel
```

```
    ' Get the RouteManager from the top-level assembly
    Set rtRouteManager = swTopLevelAssembly.GetRouteManager
```

```
    If rtRouteManager Is Nothing Then
        Debug.Print "No RouteManager found in top-level document"
        Exit Sub
    End If
```

```
    ' Select and edit a route
    status = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditRoute
```

```
    ' Get electrical route
    Set rtElectricalRoute = rtRouteManager.GetElectricalRoute
    If rtElectricalRoute Is Nothing Then
        Debug.Print "Electrical route not found"
        Exit Sub
    End If
    Debug.Print "Electrical route found"
```

```
    ' Get the number of wires and get the wires
    count = rtElectricalRoute.GetWiresCount
    Debug.Print "Number of wires: " & count
    wires = rtElectricalRoute.GetWires
```

```
    ' For each wire...
    For i = 0 To count - 1
```

```
        ' Get wire
        Set rtWire = wires(i)
         If rtWire Is Nothing Then
            Exit Sub
        End If
```

```
        Debug.Print ""
        ' Get wire's cutting length and name of the cable
        cuttingLength = rtWire.GetCuttingLength
        Debug.Print "  Cutting length: " & cuttingLength
        cableName = rtWire.UserName
        Debug.Print "  Cable name: " & cableName
```

```
        ' Get and set wire's route segments and their IDs
        routeSegmentIDs = rtWire.GetRouteSegmentIDs
        routeSegmentIDsCount = rtWire.GetRouteSegmentIDsCount
        For j = 0 To routeSegmentIDsCount - 1
            Debug.Print "    Original route segment ID: " & routeSegmentIDs(j)
            routeSegmentIDs(j) = routeSegmentIDs(j) - 1
        Next j

        ' Set new IDs for the route segments in the wire, clear
        ' the previous selected route path, and create a new
        ' route path for the route segments in the wire
        routePathStatus = rtWire.SetRoutePathForWire(routeSegmentIDs)
        Debug.Print "    Status of creating new route path (0 = success): " & routePathStatus
```

```
        ' Get the wire's route segments and their IDs
        routeSegmentIDs = rtWire.GetRouteSegmentIDs
        routeSegmentIDsCount = rtWire.GetRouteSegmentIDsCount
        For k = 0 To routeSegmentIDsCount - 1
            Debug.Print "    New route segment ID: " & routeSegmentIDs(k)
        Next k

    Next i
```

```
    ' Clear selection
    swModel.ClearSelection2 True
```

```
    ' Exit edit mode
    swTopLevelAssembly.EditAssembly
```

```
End Sub
```
