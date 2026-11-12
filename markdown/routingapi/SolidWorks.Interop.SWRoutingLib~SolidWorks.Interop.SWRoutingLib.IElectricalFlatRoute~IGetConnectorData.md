---
title: "IGetConnectorData Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "IGetConnectorData"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~IGetConnectorData.html"
---

# IGetConnectorData Method (IElectricalFlatRoute)

Gets the specified connector's data for this electrical flattened route.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConnectorData( _
   ByVal connectorName As System.String, _
   ByRef fittingPoint As System.Object, _
   ByRef fittingDirection As System.Double, _
   ByRef isVisible As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalFlatRoute
Dim connectorName As System.String
Dim fittingPoint As System.Object
Dim fittingDirection As System.Double
Dim isVisible As System.Boolean
Dim value As System.Boolean

value = instance.IGetConnectorData(connectorName, fittingPoint, fittingDirection, isVisible)
```

### C#

```csharp
System.bool IGetConnectorData(
   System.string connectorName,
   out System.object fittingPoint,
   out System.double fittingDirection,
   out System.bool isVisible
)
```

### C++/CLI

```cpp
System.bool IGetConnectorData(
   System.String^ connectorName,
   [Out] System.Object^ fittingPoint,
   [Out] System.double fittingDirection,
   [Out] System.bool isVisible
)
```

### Parameters

- `connectorName`: Name of the connector
- `fittingPoint`: Location of the fitting's connection point in the flattened configuration
- `fittingDirection`: - in-process, unmanaged C++: Pointer to an array of doubles for the direction in which the route exits the fitting at the connection point in the flattened configuration
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `isVisible`: True if the connector is visible, false if not

### Return Value

True if successful, false if not

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)
[IElectricalFlatRoute::GetConnectorData Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetConnectorData.html)

## Availability

SOLIDWORKS Routing 2008 FCS
