---
title: "GetComponentRouteType Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetComponentRouteType"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentRouteType.html"
---

# GetComponentRouteType Method (IRoutingComponentManager)

Gets the route type of the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentRouteType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.Integer

value = instance.GetComponentRouteType()
```

### C#

```csharp
System.int GetComponentRouteType()
```

### C++/CLI

```cpp
System.int GetComponentRouteType();
```

### Return Value

Type of route as defined in [swComponentRouteType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swComponentRouteType_e.html)

## VBA Syntax

See [RoutingComponentManager::GetComponentRouteType](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetComponentRouteType.html).

## Examples

[Get and Set Routing Component Properties (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetComponentRouteTypeFromCustomProperty Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentRouteTypeFromCustomProperty.html)

## Availability

SOLIDWORKS Routing 2011 FCS
