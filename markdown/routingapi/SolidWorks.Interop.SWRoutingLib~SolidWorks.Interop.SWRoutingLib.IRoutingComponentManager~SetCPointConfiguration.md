---
title: "SetCPointConfiguration Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetCPointConfiguration"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetCPointConfiguration.html"
---

# SetCPointConfiguration Method (IRoutingComponentManager)

Sets the configuration for including and enabling connection points when the active routing component is placed in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCPointConfiguration( _
   ByVal type As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim type As System.Integer

instance.SetCPointConfiguration(type)
```

### C#

```csharp
void SetCPointConfiguration(
   System.int type
)
```

### C++/CLI

```cpp
void SetCPointConfiguration(
   System.int type
)
```

### Parameters

- `type`: Type of connection point configuration as defined in [swCPointConfig_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swCPointConfig_e.html)

## VBA Syntax

See [RoutingComponentManager::SetCPointConfiguration](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetCPointConfiguration.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetCPointConfiguration Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetCPointConfiguration.html)

## Availability

SOLIDWORKS Routing 2011 FCS
