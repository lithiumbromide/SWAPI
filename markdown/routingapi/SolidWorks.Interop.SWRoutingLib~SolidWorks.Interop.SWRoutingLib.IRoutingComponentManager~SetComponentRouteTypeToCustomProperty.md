---
title: "SetComponentRouteTypeToCustomProperty Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetComponentRouteTypeToCustomProperty"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentRouteTypeToCustomProperty.html"
---

# SetComponentRouteTypeToCustomProperty Method (IRoutingComponentManager)

Sets the route type for the custom property for the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetComponentRouteTypeToCustomProperty( _
   ByVal RouteType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim RouteType As System.Integer

instance.SetComponentRouteTypeToCustomProperty(RouteType)
```

### C#

```csharp
void SetComponentRouteTypeToCustomProperty(
   System.int RouteType
)
```

### C++/CLI

```cpp
void SetComponentRouteTypeToCustomProperty(
   System.int RouteType
)
```

### Parameters

- `RouteType`: Type of route as defined in [swComponentRouteType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swComponentRouteType_e.html)

## VBA Syntax

See [RoutingComponentManager::SetComponentRouteTypeToCustomProperty](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetComponentRouteTypeToCustomProperty.html).

## Examples

[Set User-defined Route (C#)](Set_User-defined_Route_Example_CSharp.htm)
[Set User-defined Route (VB.NET)](Set_User-defined_Route_Example_VBNET.htm)
[Set User-defined Route (VBA)](Set_User-defined_Route_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetComponentRouteTypeFromCustomProperty Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentRouteTypeFromCustomProperty.html)
[IRoutingComponentManager::GetComponentRouteType Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentRouteType.html)

## Availability

SOLIDWORKS Routing 2013 FCS
