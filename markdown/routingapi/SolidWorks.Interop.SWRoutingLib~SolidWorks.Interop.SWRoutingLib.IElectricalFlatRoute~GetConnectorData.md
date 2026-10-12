---
title: "GetConnectorData Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "GetConnectorData"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetConnectorData.html"
---

# GetConnectorData Method (IElectricalFlatRoute)

Gets the specified connector's data for this electrical flattened route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectorData( _
   ByVal connectorName As System.String, _
   ByRef fittingPoint As System.Object, _
   ByRef fittingDirection As System.Object, _
   ByRef isVisible As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalFlatRoute
Dim connectorName As System.String
Dim fittingPoint As System.Object
Dim fittingDirection As System.Object
Dim isVisible As System.Boolean
Dim value As System.Boolean

value = instance.GetConnectorData(connectorName, fittingPoint, fittingDirection, isVisible)
```

### C#

```csharp
System.bool GetConnectorData(
   System.string connectorName,
   out System.object fittingPoint,
   out System.object fittingDirection,
   out System.bool isVisible
)
```

### C++/CLI

```cpp
System.bool GetConnectorData(
   System.String^ connectorName,
   [Out] System.Object^ fittingPoint,
   [Out] System.Object^ fittingDirection,
   [Out] System.bool isVisible
)
```

### Parameters

- `connectorName`: Name of the connector
- `fittingPoint`: Location of the fitting's connection point in the flattened configuration
- `fittingDirection`: Array of doubles for the direction in which the route exits the fitting at the connection point in the flattened configuration
- `isVisible`: TRUE if the connector is visible, FALSE if not

### Return Value

True if successful, false if not

## VBA Syntax

See [ElectricalFlatRoute::GetConnectorData](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalFlatRoute~GetConnectorData.html).

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)
[IElectricalFlatRoute::IGetConnectorData Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~IGetConnectorData.html)

## Availability

SOLIDWORKS Routing 2008 FCS
