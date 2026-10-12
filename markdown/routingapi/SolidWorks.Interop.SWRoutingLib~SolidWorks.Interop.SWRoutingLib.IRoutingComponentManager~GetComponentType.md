---
title: "GetComponentType Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetComponentType"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentType.html"
---

# GetComponentType Method (IRoutingComponentManager)

Gets the type of the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.Integer

value = instance.GetComponentType()
```

### C#

```csharp
System.int GetComponentType()
```

### C++/CLI

```cpp
System.int GetComponentType();
```

### Return Value

Type of component as defined in [swRouteComponentTypeID_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swRouteComponentTypeID_e.html)

## VBA Syntax

See [RoutingComponentManager::GetComponentType](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetComponentType.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## Remarks

The component type is based on the number of connection and routing points.

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::SetComponentType Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentType.html)

## Availability

SOLIDWORKS Routing 2011 FCS
