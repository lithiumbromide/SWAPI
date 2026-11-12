---
title: "ICreateRouteThroughSketchEntities Method (IAutoRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IAutoRoute"
member: "ICreateRouteThroughSketchEntities"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~ICreateRouteThroughSketchEntities.html"
---

# ICreateRouteThroughSketchEntities Method (IAutoRoute)

Creates a route using the specified sketch entity types and IDs.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateRouteThroughSketchEntities( _
   ByVal conversionMode As System.Integer, _
   ByVal autoTangencyMode As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef EntityTypes As System.Integer, _
   ByRef EntityIDs As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoRoute
Dim conversionMode As System.Integer
Dim autoTangencyMode As System.Integer
Dim Count As System.Integer
Dim EntityTypes As System.Integer
Dim EntityIDs As System.Integer
Dim value As System.Integer

value = instance.ICreateRouteThroughSketchEntities(conversionMode, autoTangencyMode, Count, EntityTypes, EntityIDs)
```

### C#

```csharp
System.int ICreateRouteThroughSketchEntities(
   System.int conversionMode,
   System.int autoTangencyMode,
   System.int Count,
   ref System.int EntityTypes,
   ref System.int EntityIDs
)
```

### C++/CLI

```cpp
System.int ICreateRouteThroughSketchEntities(
   System.int conversionMode,
   System.int autoTangencyMode,
   System.int Count,
   System.int% EntityTypes,
   System.int% EntityIDs
)
```

### Parameters

- `conversionMode`: Type of route as defined in [swAutoRouteConversionMode_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteConversionMode_e.html)
- `autoTangencyMode`: Tangency mode as defined in [swAutoRouteAutoTangencyMode_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteAutoTangencyMode_e.html)
- `Count`: Number of sketch entities
- `EntityTypes`: - in-process, unmanaged C++: Pointer to an array of integers representing the types of sketch entities to use for the route as defined in [swAutoRouteSketchEntitiesTypes_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteSketchEntitiesTypes_e.html) (see **Remarks**)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `EntityIDs`: - in-process, unmanaged C++: Pointer to an array of integers representing the IDs of the sketch entities in EntityTypes (see **Remarks**)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Error code as defined in [swAutoRouteErrorType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAutoRouteErrorType_e.html)

## Remarks

The EntityTypes and EntityIDs arrays must be the same size. Specify the size of the arrays for Count.

The EntityIDs determine the path of the route. To get EntityIDs values, use [ISketchPoint::IGetID](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~IGetID.html) for sketch points and [ISketchSegment::IGetID](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~IGetID.html) for sketch lines, sketch arcs, and sketch spline.

If a segment already exists between two sketch entities, then that segment is used as part of the newly created route path.

Before calling this method:

1. Select a route feature in an assembly.
2. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).
3. Populate the EntityTypes and EntityIDs arrays with the types and IDs of the sketch entities.

## See Also

[IAutoRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute.html)
[IAutoRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute_members.html)
[IAutoRoute::CreateRouteThroughSketchEntities Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~CreateRouteThroughSketchEntities.html)

## Availability

SOLIDWORKS Routing 2014 FCS
