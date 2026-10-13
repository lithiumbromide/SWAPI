---
title: "EditRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "EditRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~EditRoute.html"
---

# EditRoute Method (IRouteManager)

Places the route in edit mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditRoute()
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager

instance.EditRoute()
```

### C#

```csharp
void EditRoute()
```

### C++/CLI

```cpp
void EditRoute();
```

## VBA Syntax

See [RouteManager::EditRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~EditRoute.html).

## Examples

[Create Auto Route Example (C#)](Create_Auto_Route_Example_CSharp.htm)
[Create Auto Route Example (VB.NET)](Create_Auto_Route_Example_VBNET.htm)
[Create Auto Route Example (VBA)](Create_Auto_Route_Example_VB.htm)
[Convert Guidelines into a Route Example (C#)](Convert_Guidelines_into_a_Route_Example_CSharp.htm)
[Convert Guidelines into a Route Example (VB.NET)](Convert_Guidelines_into_a_Route_Example_VBNET.htm)
[Convert Guidelines into a Route Example (VBA)](Convert_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

Before calling this method, you must select the assembly that contains the route.

| To exit... | Call... |
| --- | --- |
| 1. Routing edit mode | IRouteManager::ExitRoute |
| 2. Assembly edit mode | IAssemblyDoc::EditAssembly |

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IRouteManager::StartRoute](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~StartRoute.html)

## Availability

SOLIDWORKS Routing 2011 FCS
