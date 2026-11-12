---
title: "SetComponentType Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetComponentType"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentType.html"
---

# SetComponentType Method (IRoutingComponentManager)

Sets the type of the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetComponentType( _
   ByVal ComponentType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim ComponentType As System.Integer

instance.SetComponentType(ComponentType)
```

### C#

```csharp
void SetComponentType(
   System.int ComponentType
)
```

### C++/CLI

```cpp
void SetComponentType(
   System.int ComponentType
)
```

### Parameters

- `ComponentType`: Type of component as defined in [swRouteComponentTypeID_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swRouteComponentTypeID_e.html)

## VBA Syntax

See [RoutingComponentManager::SetComponentType](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetComponentType.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetComponentType Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentType.html)

## Availability

SOLIDWORKS Routing 2011 FCS
