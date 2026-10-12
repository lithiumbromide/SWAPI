---
title: "ConvertGuidelinesToRoute Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "ConvertGuidelinesToRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~ConvertGuidelinesToRoute.html"
---

# ConvertGuidelinesToRoute Method (IAutoRoute)

Converts selected guidelines into unique routes.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertGuidelinesToRoute() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim value As System.Boolean

value = instance.ConvertGuidelinesToRoute()
```

### C#

```csharp
System.bool ConvertGuidelinesToRoute()
```

### C++/CLI

```cpp
System.bool ConvertGuidelinesToRoute();
```

### Return Value

True if successful, false if not

## VBA Syntax

See [AutoRoute::ConvertGuidelinesToRoute](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~ConvertGuidelinesToRoute.html).

## Examples

[Convert Guidelines into a Route Example (C#)](Convert_Guidelines_into_a_Route_Example_CSharp.htm)
[Convert Guidelines into a Route Example (VB.NET)](Convert_Guidelines_into_a_Route_Example_VBNET.htm)
[Convert Guidelines into a Route Example (VBA)](Convert_Guidelines_into_a_Route_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IRouteManager::ImportFromToList](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~ImportFromToList.html).
2. In the FeatureManager design tree, select the assembly that contains the route whose guidelines you want to select.
3. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).
4. Call [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) multiple times specifying type SKETCHSEGMENT to mark the guidelines you want to convert or call [IAutoRoute::SelectGuidelines](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IAutoRoute~SelectGuidelines.html) to select all guidelines.

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
