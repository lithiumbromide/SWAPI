---
title: "SetRoutingComponentDescription Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetRoutingComponentDescription"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetRoutingComponentDescription.html"
---

# SetRoutingComponentDescription Method (IRoutingComponentManager)

Sets the description of the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRoutingComponentDescription( _
   ByVal StringID As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim StringID As System.String

instance.SetRoutingComponentDescription(StringID)
```

### C#

```csharp
void SetRoutingComponentDescription(
   System.string StringID
)
```

### C++/CLI

```cpp
void SetRoutingComponentDescription(
   System.String^ StringID
)
```

### Parameters

- `StringID`: Description of the routing component

## VBA Syntax

See [RoutingComponentManager::SetRoutingComponentDescription](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetRoutingComponentDescription.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetRoutingComponentDescription Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetRoutingComponentDescription.html)

## Availability

SOLIDWORKS Routing 2011 FCS
