---
title: "MergeGuidelines Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "MergeGuidelines"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~MergeGuidelines.html"
---

# MergeGuidelines Method (IAutoRoute)

Merges selected guidelines to form a single route.

## Syntax

### Visual Basic (Declaration)

```vb
Function MergeGuidelines() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim value As System.Boolean

value = instance.MergeGuidelines()
```

### C#

```csharp
System.bool MergeGuidelines()
```

### C++/CLI

```cpp
System.bool MergeGuidelines();
```

### Return Value

True if successful, false if not

## VBA Syntax

See [AutoRoute::MergeGuidelines](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~MergeGuidelines.html).

## Examples

[Merge Guidelines into a Route Example (C#)](Merge_Guidelines_into_a_Route_Example_CSharp.htm)
[Merge Guidelines into a Route Example (VB.NET)](Merge_Guidelines_into_a_Route_Example_VBNET.htm)
[Merge Guidelines into a Route Example (VBA)](Merge_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IRouteManager::ImportFromToList](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~ImportFromToList.html).
2. In the FeatureManager design tree, select the assembly that contains the route whose guidelines to select.
3. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).
4. Call [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) multiple times, specifying type SKETCHSEGMENT to mark the guidelines you want to merge.
  - or -
  Call [IAutoRoute::SelectGuidelines](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IAutoRoute~SelectGuidelines.html) to select all the guidelines.

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
