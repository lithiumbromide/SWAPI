---
title: "SelectGuidelines Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "SelectGuidelines"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~SelectGuidelines.html"
---

# SelectGuidelines Method (IAutoRoute)

Selects all of the guidelines in the route.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectGuidelines() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim value As System.Integer

value = instance.SelectGuidelines()
```

### C#

```csharp
System.int SelectGuidelines()
```

### C++/CLI

```cpp
System.int SelectGuidelines();
```

### Return Value

Number of selected guidelines

## VBA Syntax

See [AutoRoute::SelectGuidelines](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~SelectGuidelines.html).

## Examples

[Merge Guidelines into a Route Example (C#)](Merge_Guidelines_into_a_Route_Example_CSharp.htm)
[Merge Guidelines into a Route Example (VB.NET)](Merge_Guidelines_into_a_Route_Example_VBNET.htm)
[Merge Guidelines into a Route Example (VBA)](Merge_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IRouteManager::ImportFromToList](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~ImportFromToList.html).
2. In the FeatureManager design tree, select the assembly that contains the route whose guidelines to select.
3. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).

After calling this method, you can call:

- [IAutoRoute::MergeGuidelines](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IAutoRoute~MergeGuidelines.html)
  - or -
- [IAutoRoute::ConvertGuidelinesToRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IAutoRoute~ConvertGuidelinesToRoute.html)

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)
[IAutoRoute::DeleteAllGuidelines Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~DeleteAllGuidelines.html)

## Availability

SOLIDWORKS Routing 2011 FCS
