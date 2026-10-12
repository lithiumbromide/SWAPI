---
title: "GetFittingFilePath Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "GetFittingFilePath"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetFittingFilePath.html"
---

# GetFittingFilePath Method (IElectricalFlatRoute)

Gets the path and filename of the fitting for the specified connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFittingFilePath( _
   ByVal connectorName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalFlatRoute
Dim connectorName As System.String
Dim value As System.String

value = instance.GetFittingFilePath(connectorName)
```

### C#

```csharp
System.string GetFittingFilePath(
   System.string connectorName
)
```

### C++/CLI

```cpp
System.String^ GetFittingFilePath(
   System.String^ connectorName
)
```

### Parameters

- `connectorName`: Name of the connector

### Return Value

Path and filename of the fitting

## VBA Syntax

See [ElectricalFlatRoute::GetFittingFilePath](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalFlatRoute~GetFittingFilePath.html).

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)

## Availability

SOLIDWORKS Routing 2008 FCS
