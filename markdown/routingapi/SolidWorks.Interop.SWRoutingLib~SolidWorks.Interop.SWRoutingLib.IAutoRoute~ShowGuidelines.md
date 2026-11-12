---
title: "ShowGuidelines Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "ShowGuidelines"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~ShowGuidelines.html"
---

# ShowGuidelines Method (IAutoRoute)

Displays a preview of the connections imported from a from-to list.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowGuidelines() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim value As System.Integer

value = instance.ShowGuidelines()
```

### C#

```csharp
System.int ShowGuidelines()
```

### C++/CLI

```cpp
System.int ShowGuidelines();
```

### Return Value

Number of displayed guidelines.

## VBA Syntax

See [AutoRoute::ShowGuidelines](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~ShowGuidelines.html).

## Examples

[Merge Guidelines into a Route Example (C#)](Merge_Guidelines_into_a_Route_Example_CSharp.htm)
[Merge Guidelines into a Route Example (VB.NET)](Merge_Guidelines_into_a_Route_Example_VBNET.htm)
[Merge Guidelines into a Route Example (VBA)](Merge_Guidelines_into_a_Route_Example_VB.htm)
[Convert Guidelines into a Route Example (C#)](Convert_Guidelines_into_a_Route_Example_CSharp.htm)
[Convert Guidelines into a Route Example (VB.NET)](Convert_Guidelines_into_a_Route_Example_VBNET.htm)
[Convert Guidelines into a Route Example (VBA)](Convert_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IRouteManager::ImportFromToList](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~ImportFromToList.html).
2. In the FeatureManager design tree, select the assembly that contains the route for which to show guidelines.
3. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
