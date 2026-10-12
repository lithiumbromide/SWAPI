---
title: "ExitRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "ExitRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~ExitRoute.html"
---

# ExitRoute Method (IRouteManager)

Exits the route edit mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ExitRoute()
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager

instance.ExitRoute()
```

### C#

```csharp
void ExitRoute()
```

### C++/CLI

```cpp
void ExitRoute();
```

## VBA Syntax

See [RouteManager::ExitRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~ExitRoute.html).

## Examples

[Create Auto Route Example (C#)](Create_Auto_Route_Example_CSharp.htm)
[Create Auto Route Example (VB.NET)](Create_Auto_Route_Example_VBNET.htm)
[Create Auto Route Example (VBA)](Create_Auto_Route_Example_VB.htm)
[Convert Guidelines into a Route Example (C#)](Convert_Guidelines_into_a_Route_Example_CSharp.htm)
[Convert Guidelines into a Route Example (VB.NET)](Convert_Guidelines_into_a_Route_Example_VBNET.htm)
[Convert Guidelines into a Route Example (VBA)](Convert_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

| Call... | To... |
| --- | --- |
| IRouteManager::EditRoute | Put the assembly in routing edit mode to start or edit a route |
| IRouteManager::StartRoute | Put the assembly in routing edit mode to start a route |
| IAssemblyDoc::EditAssembly | Exit editing the assembly |

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
