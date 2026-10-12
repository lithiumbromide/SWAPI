---
title: "ChangeRoutingLibComponentPaths Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "ChangeRoutingLibComponentPaths"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~ChangeRoutingLibComponentPaths.html"
---

# ChangeRoutingLibComponentPaths Method (IRouteManager)

Replaces the old routing library paths with new routing library paths.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ChangeRoutingLibComponentPaths( _
   ByVal oldLibPaths As System.Object, _
   ByVal newLibPaths As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim oldLibPaths As System.Object
Dim newLibPaths As System.Object

instance.ChangeRoutingLibComponentPaths(oldLibPaths, newLibPaths)
```

### C#

```csharp
void ChangeRoutingLibComponentPaths(
   System.object oldLibPaths,
   System.object newLibPaths
)
```

### C++/CLI

```cpp
void ChangeRoutingLibComponentPaths(
   System.Object^ oldLibPaths,
   System.Object^ newLibPaths
)
```

### Parameters

- `oldLibPaths`: Old routing library paths
- `newLibPaths`: New routing library paths

## VBA Syntax

See [RouteManager::ChangeRoutingLibComponentPaths](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~ChangeRoutingLibComponentPaths.html).

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2007 SP1
