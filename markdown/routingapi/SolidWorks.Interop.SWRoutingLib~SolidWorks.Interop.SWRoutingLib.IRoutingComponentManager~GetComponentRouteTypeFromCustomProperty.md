---
title: "GetComponentRouteTypeFromCustomProperty Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetComponentRouteTypeFromCustomProperty"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentRouteTypeFromCustomProperty.html"
---

# GetComponentRouteTypeFromCustomProperty Method (IRoutingComponentManager)

Gets the route type from the custom property for the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentRouteTypeFromCustomProperty() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.Integer

value = instance.GetComponentRouteTypeFromCustomProperty()
```

### C#

```csharp
System.int GetComponentRouteTypeFromCustomProperty()
```

### C++/CLI

```cpp
System.int GetComponentRouteTypeFromCustomProperty();
```

### Return Value

Type of route as defined in [swComponentRouteType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swComponentRouteType_e.html)

## VBA Syntax

See [RoutingComponentManager::GetComponentRouteTypeFromCustomProperty](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetComponentRouteTypeFromCustomProperty.html).

## Examples

[Get and Set Routing Component Properties (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::SetComponentRouteTypeToCustomProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentRouteTypeToCustomProperty.html)
[IRoutingComponentManager::GetComponentType](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentRouteType.html)

## Availability

SOLIDWORKS Routing 2013 FCS
