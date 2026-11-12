---
title: "GetAutoRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetAutoRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetAutoRoute.html"
---

# GetAutoRoute Method (IRouteManager)

Gets the interface to Auto Route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoRoute() As AutoRoute
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim value As AutoRoute

value = instance.GetAutoRoute()
```

### C#

```csharp
AutoRoute GetAutoRoute()
```

### C++/CLI

```cpp
AutoRoute^ GetAutoRoute();
```

### Return Value

[IAutoRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IAutoRoute.html)

## VBA Syntax

See [RouteManager::GetAutoRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetAutoRoute.html).

## Examples

[Create Auto Route Example (C#)](Create_Auto_Route_Example_CSharp.htm)
[Create Auto Route Example (VB.NET)](Create_Auto_Route_Example_VBNET.htm)
[Create Auto Route Example (VBA)](Create_Auto_Route_Example_VB.htm)
[Convert Guidelines into a Route Example (C#)](Convert_Guidelines_into_a_Route_Example_CSharp.htm)
[Convert Guidelines into a Route Example (VB.NET)](Convert_Guidelines_into_a_Route_Example_VBNET.htm)
[Convert Guidelines into a Route Example (VBA)](Convert_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

Before calling this method:

1. In the FeatureManager design tree, select the assembly that contains the route to which to add connections.
2. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
