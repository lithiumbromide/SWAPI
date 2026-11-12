---
title: "GetElectricalFlatRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetElectricalFlatRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetElectricalFlatRoute.html"
---

# GetElectricalFlatRoute Method (IRouteManager)

Gets the specified electrical flattened configuration for a selected route assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElectricalFlatRoute( _
   ByVal FlatRouteName As System.String _
) As ElectricalFlatRoute
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim FlatRouteName As System.String
Dim value As ElectricalFlatRoute

value = instance.GetElectricalFlatRoute(FlatRouteName)
```

### C#

```csharp
ElectricalFlatRoute GetElectricalFlatRoute(
   System.string FlatRouteName
)
```

### C++/CLI

```cpp
ElectricalFlatRoute^ GetElectricalFlatRoute(
   System.String^ FlatRouteName
)
```

### Parameters

- `FlatRouteName`: Name of the electrical flattened configuration

### Return Value

[Electrical flattened route](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalFlatRoute.html)

## VBA Syntax

See [RouteManager::GetElectricalFlatRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetElectricalFlatRoute.html).

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2008 FCS
