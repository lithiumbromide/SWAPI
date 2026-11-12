---
title: "AddToRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "AddToRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~AddToRoute.html"
---

# AddToRoute Method (IRouteManager)

Creates a route from one or more selected connection points or on the connection points of a selected routing component in a routing assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToRoute() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim value As System.Boolean

value = instance.AddToRoute()
```

### C#

```csharp
System.bool AddToRoute()
```

### C++/CLI

```cpp
System.bool AddToRoute();
```

### Return Value

True if a route is added, false if not

## VBA Syntax

See [RouteManager::AddToRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~AddToRoute.html).

## Examples

[Add to Route (VBA)](Add_to_Route_Example_VB.htm)

## Remarks

Before calling this method, you must call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html) to place the routing assembly in edit mode.

| To exit... | Call... |
| --- | --- |
| 1. Routing edit mode | IRouteManager::ExitRoute |
| 2. Assembly edit mode | IAssemblyDoc::EditAssembly |

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IRouteManager::StartRoute](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~StartRoute.html)

## Availability

SOLIDWORKS Routing 2013 FCS
