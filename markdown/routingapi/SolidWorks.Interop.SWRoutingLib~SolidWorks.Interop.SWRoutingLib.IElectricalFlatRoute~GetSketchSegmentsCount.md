---
title: "GetSketchSegmentsCount Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "GetSketchSegmentsCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetSketchSegmentsCount.html"
---

# GetSketchSegmentsCount Method (IElectricalFlatRoute)

Gets the number of SOLIDWORKS sketch segments for the specified route segment in this flattened route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegmentsCount( _
   ByVal RouteSegmentID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalFlatRoute
Dim RouteSegmentID As System.Integer
Dim value As System.Integer

value = instance.GetSketchSegmentsCount(RouteSegmentID)
```

### C#

```csharp
System.int GetSketchSegmentsCount(
   System.int RouteSegmentID
)
```

### C++/CLI

```cpp
System.int GetSketchSegmentsCount(
   System.int RouteSegmentID
)
```

### Parameters

- `RouteSegmentID`: Route segment ID (see Remarks)

### Return Value

Number of segment segments

## VBA Syntax

See [ElectricalFlatRoute::GetSketchSegmentsCount](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalFlatRoute~GetSketchSegmentsCount.html).

## Remarks

Use [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) to get the value for RouteSegmentID.

Call this method before calling [IElectricalFlatRoute::IGetSketchSegments](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalFlatRoute~IGetSketchSegments.html) to determine the size of the array for the sketch segments.

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)
[IElectricalFlatRoute::GetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetSketchSegments.html)

## Availability

SOLIDWORKS Routing 2009 FCS
