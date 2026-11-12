---
title: "GetCPointConfiguration Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetCPointConfiguration"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetCPointConfiguration.html"
---

# GetCPointConfiguration Method (IRoutingComponentManager)

Gets the rules for including and enabling connection points when the active routing component is placed in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCPointConfiguration() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.Integer

value = instance.GetCPointConfiguration()
```

### C#

```csharp
System.int GetCPointConfiguration()
```

### C++/CLI

```cpp
System.int GetCPointConfiguration();
```

### Return Value

Type of connection point configuration as defined in [swCPointConfig_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swCPointConfig_e.html)

## VBA Syntax

See [RoutingComponentManager::GetCPointConfiguration](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetCPointConfiguration.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## Remarks

The connection point configuration is specified on the **Routing Functionality Points** page of the Routing Component Wizard.

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::SetCPointConfiguration Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetCPointConfiguration.html)

## Availability

SOLIDWORKS Routing 2011 FCS
