---
title: "GetAdvancedRouteSelector Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetAdvancedRouteSelector"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetAdvancedRouteSelector.html"
---

# GetAdvancedRouteSelector Method (IRouteManager)

Gets access to the SOLIDWORKS Highlight Search tool.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAdvancedRouteSelector() As AdvancedRouteSelector
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim value As AdvancedRouteSelector

value = instance.GetAdvancedRouteSelector()
```

### C#

```csharp
AdvancedRouteSelector GetAdvancedRouteSelector()
```

### C++/CLI

```cpp
AdvancedRouteSelector^ GetAdvancedRouteSelector();
```

### Return Value

[SOLIDWORKS Highlight Search tool](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IAdvancedRouteSelector.html)

## VBA Syntax

See [RouteManager::GetAdvancedRouteSelector](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetAdvancedRouteSelector.html).

## Examples

[Select Connector Using Highlight Search Tool (VBA)](Select_Connector_Using_Highlight_Search_Tool_Example_VB.htm)
[Select Connector Using Highlight Search Tool (VB.NET)](Select_Connector_Using_Highlight_Search_Tool_Example_VBNET.htm)
[Select Connector Using Highlight Search Tool (C#)](Select_Connector_Using_Highlight_Search_Tool_Example_CSharp.htm)

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
