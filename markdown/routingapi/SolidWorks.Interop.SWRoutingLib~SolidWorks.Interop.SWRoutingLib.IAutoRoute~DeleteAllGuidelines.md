---
title: "DeleteAllGuidelines Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "DeleteAllGuidelines"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~DeleteAllGuidelines.html"
---

# DeleteAllGuidelines Method (IAutoRoute)

Deletes all guidelines.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteAllGuidelines()
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute

instance.DeleteAllGuidelines()
```

### C#

```csharp
void DeleteAllGuidelines()
```

### C++/CLI

```cpp
void DeleteAllGuidelines();
```

## VBA Syntax

See [AutoRoute::DeleteAllGuidelines](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~DeleteAllGuidelines.html).

## Remarks

Before calling this method:

1. In the FeatureManager design tree, select the assembly that contains the route whose guidelines to delete.
2. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
