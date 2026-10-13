---
title: "SetRouteComponentTypeSetThrRLM Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetRouteComponentTypeSetThrRLM"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetRouteComponentTypeSetThrRLM.html"
---

# SetRouteComponentTypeSetThrRLM Method (IRoutingComponentManager)

Sets whether the type of the active routing component is set through the Routing Library Manager.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRouteComponentTypeSetThrRLM( _
   ByVal ComponentType As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim ComponentType As System.Boolean

instance.SetRouteComponentTypeSetThrRLM(ComponentType)
```

### C#

```csharp
void SetRouteComponentTypeSetThrRLM(
   System.bool ComponentType
)
```

### C++/CLI

```cpp
void SetRouteComponentTypeSetThrRLM(
   System.bool ComponentType
)
```

### Parameters

- `ComponentType`: True to indicate that the type of the component is set through the Routing Library Manager, false to indicate that the type is not set through the Routing Library Manager

## VBA Syntax

See [RoutingComponentManager::SetRouteComponentTypeSetThrRLM](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetRouteComponentTypeSetThrRLM.html).

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetRouteComponentTypeSetThrRLM Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetRouteComponentTypeSetThrRLM.html)

## Availability

SOLIDWORKS Routing 2011 FCS
