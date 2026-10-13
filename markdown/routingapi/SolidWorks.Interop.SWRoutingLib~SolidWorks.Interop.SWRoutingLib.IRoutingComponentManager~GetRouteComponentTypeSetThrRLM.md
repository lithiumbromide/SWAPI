---
title: "GetRouteComponentTypeSetThrRLM Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetRouteComponentTypeSetThrRLM"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetRouteComponentTypeSetThrRLM.html"
---

# GetRouteComponentTypeSetThrRLM Method (IRoutingComponentManager)

Gets whether the type of the active routing component is set through the Routing Library Manager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteComponentTypeSetThrRLM() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.Boolean

value = instance.GetRouteComponentTypeSetThrRLM()
```

### C#

```csharp
System.bool GetRouteComponentTypeSetThrRLM()
```

### C++/CLI

```cpp
System.bool GetRouteComponentTypeSetThrRLM();
```

### Return Value

True if the type is set through the Routing Library Manager, false if not

## VBA Syntax

See [RoutingComponentManager::GetRouteComponentTypeSetThrRLM](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetRouteComponentTypeSetThrRLM.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::SetRouteComponentTypeSetThrRLM Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetRouteComponentTypeSetThrRLM.html)

## Availability

SOLIDWORKS Routing 2011 FCS
