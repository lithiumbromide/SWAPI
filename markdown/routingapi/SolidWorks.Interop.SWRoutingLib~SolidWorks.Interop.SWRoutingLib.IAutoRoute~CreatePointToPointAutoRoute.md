---
title: "CreatePointToPointAutoRoute Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "CreatePointToPointAutoRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~CreatePointToPointAutoRoute.html"
---

# CreatePointToPointAutoRoute Method (IAutoRoute)

Connects two selected entities on a route.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePointToPointAutoRoute( _
   ByVal conversionMode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim conversionMode As System.Integer
Dim value As System.Integer

value = instance.CreatePointToPointAutoRoute(conversionMode)
```

### C#

```csharp
System.int CreatePointToPointAutoRoute(
   System.int conversionMode
)
```

### C++/CLI

```cpp
System.int CreatePointToPointAutoRoute(
   System.int conversionMode
)
```

### Parameters

- `conversionMode`: Route style as defined in [swPointToPointAutoRouteConversionMode_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swPointToPointAutoRouteConversionMode_e.html)

### Return Value

Error code as defined in [swPointToPointAutoRouteErrorType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swPointToPointAutoRouteErrorType_e.html)

## VBA Syntax

See [AutoRoute::CreatePointToPointAutoRoute](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~CreatePointToPointAutoRoute.html).

## Examples

[Create Auto Route Example (C#)](Create_Auto_Route_Example_CSharp.htm)
[Create Auto Route Example (VB.NET)](Create_Auto_Route_Example_VBNET.htm)
[Create Auto Route Example (VBA)](Create_Auto_Route_Example_VB.htm)

## Remarks

Call this method to automatically connect one of the following in a route:

- two points
- a point and a clip axis
- a point and a line

Before calling this method:

1. In the FeatureManager design tree, select the assembly that contains the route to which to add connections.
2. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).
3. Call [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) twice, specifying type SKETCHPOINT to select two points on the route.

After calling this method:

1. Call [IRouteManager::ExitRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~ExitRoute.html).
2. Call [IAssemblyDoc::EditAssembly](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EditAssembly.html).

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
