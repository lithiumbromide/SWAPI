---
title: "StartRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "StartRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~StartRoute.html"
---

# StartRoute Method (IRouteManager)

Starts a route from one of the following:

- selected connection point
- selected routing component
- specified routing part and configuration

## Syntax

### Visual Basic (Declaration)

```vb
Function StartRoute( _
   ByVal Pathname As System.String, _
   ByVal ConfigName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim Pathname As System.String
Dim ConfigName As System.String
Dim value As System.Boolean

value = instance.StartRoute(Pathname, ConfigName)
```

### C#

```csharp
System.bool StartRoute(
   System.string Pathname,
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.bool StartRoute(
   System.String^ Pathname,
   System.String^ ConfigName
)
```

### Parameters

- `Pathname`: Path and file name of the routing part from which to start a route or "" if using a selected connection point or a selected routing component
- `ConfigName`: Configuration of the specified routing part from which to start the route or "" if using a selected connection point or a selected routing component

### Return Value

True if a route started, false if not

## VBA Syntax

See [RouteManager::StartRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~StartRoute.html).

## Examples

[Start Route (VBA)](Start_Route_Example_VB.htm)

## Remarks

Calling this method places the assembly in routing edit mode.

| To exit... | Call... |
| --- | --- |
| 1. Routing edit mode | IRouteManager::ExitRoute |
| 2. Assembly edit mode | IAssemblyDoc::EditAssembly |

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IRouteManager::AddToRoute](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~AddToRoute.html)
[IRouteManager::EditRoute](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~EditRoute.html)

## Availability

SOLIDWORKS Routing 2013 FCS
