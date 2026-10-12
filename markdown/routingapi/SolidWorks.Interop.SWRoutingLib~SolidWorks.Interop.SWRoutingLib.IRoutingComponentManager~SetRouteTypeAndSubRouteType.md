---
title: "SetRouteTypeAndSubRouteType Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetRouteTypeAndSubRouteType"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetRouteTypeAndSubRouteType.html"
---

# SetRouteTypeAndSubRouteType Method (IRoutingComponentManager)

Sets the route type and sub-type for the connection point of the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRouteTypeAndSubRouteType( _
   ByVal RouteType As System.Integer, _
   ByVal SubRouteType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim RouteType As System.Integer
Dim SubRouteType As System.Integer

instance.SetRouteTypeAndSubRouteType(RouteType, SubRouteType)
```

### C#

```csharp
void SetRouteTypeAndSubRouteType(
   System.int RouteType,
   System.int SubRouteType
)
```

### C++/CLI

```cpp
void SetRouteTypeAndSubRouteType(
   System.int RouteType,
   System.int SubRouteType
)
```

### Parameters

- `RouteType`: Type of route as defined in [swComponentRouteType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swComponentRouteType_e.html)
- `SubRouteType`: Type of electrical sub-route as defined in [swComponentRouteType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swComponentRouteType_e.html); only valid if RouteType is Electrical or 3

## VBA Syntax

See [RoutingComponentManager::SetRouteTypeAndSubRouteType](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetRouteTypeAndSubRouteType.html).

## Remarks

When a connection point is added to a routing component in the Routing Component Wizard, the **Connection Point** PropertyManager page is launched. This method sets the route type and sub-type fields on that page.

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
