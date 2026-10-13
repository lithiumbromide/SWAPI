---
title: "CreateRouteThroughSketchEntities Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "CreateRouteThroughSketchEntities"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~CreateRouteThroughSketchEntities.html"
---

# CreateRouteThroughSketchEntities Method (IAutoRoute)

Creates a route using the specified sketch entity types and IDs.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRouteThroughSketchEntities( _
   ByVal conversionMode As System.Integer, _
   ByVal autoTangencyMode As System.Integer, _
   ByVal EntityTypes As System.Object, _
   ByVal EntityIDs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim conversionMode As System.Integer
Dim autoTangencyMode As System.Integer
Dim EntityTypes As System.Object
Dim EntityIDs As System.Object
Dim value As System.Integer

value = instance.CreateRouteThroughSketchEntities(conversionMode, autoTangencyMode, EntityTypes, EntityIDs)
```

### C#

```csharp
System.int CreateRouteThroughSketchEntities(
   System.int conversionMode,
   System.int autoTangencyMode,
   System.object EntityTypes,
   System.object EntityIDs
)
```

### C++/CLI

```cpp
System.int CreateRouteThroughSketchEntities(
   System.int conversionMode,
   System.int autoTangencyMode,
   System.Object^ EntityTypes,
   System.Object^ EntityIDs
)
```

### Parameters

- `conversionMode`: Type of route as defined in [swAutoRouteConversionMode_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteConversionMode_e.html)
- `autoTangencyMode`: Tangency mode as defined in [swAutoRouteAutoTangencyMode_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteAutoTangencyMode_e.html)
- `EntityTypes`: Array of the types of sketch entities to use for the route as defined in [swAutoRouteSketchEntitiesTypes_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteSketchEntitiesTypes_e.html) (see **Remarks**)
- `EntityIDs`: Array of IDs of the sketch entities in EntityTypes (see **Remarks**)

### Return Value

Error code as defined in [swAutoRouteErrorType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteErrorType_e.html)

## VBA Syntax

See [AutoRoute::CreateRouteThroughSketchEntities](ms-its:routingapivb6.chm::/SWRoutingLib~AutoRoute~CreateRoutethroughSketchEntities.html).

## Examples

[Create Route Through Sketch Entities (C#)](Create_Route_Through_Sketch_Entities_Example_CSharp.htm)
[Create Route Through Sketch Entities (VB.NET)](Create_Route_Through_Sketch_Entities_Example_VBNET.htm)
[Create Route Through Sketch Entities (VBA)](Create_Route_Through_Sketch_Entities_Example_VB.htm)

## Remarks

The EntityTypes and EntityIDs arrays must be the same size.

The EntityIDs determine the path of the route. To get EntityIDs values, use [ISketchPoint::GetID](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~GetID.html) for sketch points and [ISketchSegment::GetID](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetID.html) for sketch lines, sketch arcs, and sketch spline.

If a segment already exists between two sketch entities, then that segment is used as part of the newly created route path.

Before calling this method:

1. Select a route feature in an assembly.
2. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).
3. Populate the EntityTypes and EntityIDs arrays with the types and IDs of the sketch entities.

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)
[IAutoRoute::ICreateRouteThroughSketchEntities Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~ICreateRouteThroughSketchEntities.html)

## Availability

SOLIDWORKS Routing 2014 FCS
