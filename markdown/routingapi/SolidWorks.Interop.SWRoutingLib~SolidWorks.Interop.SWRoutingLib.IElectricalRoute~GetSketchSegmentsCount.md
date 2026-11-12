---
title: "GetSketchSegmentsCount Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetSketchSegmentsCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegmentsCount.html"
---

# GetSketchSegmentsCount Method (IElectricalRoute)

Gets the number of SOLIDWORKS sketch segments in the route segment using the specified route segment ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegmentsCount( _
   ByVal RouteSegmentID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
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

Number of sketch segments

## VBA Syntax

See [ElectricalRoute::GetSketchSegmentsCount](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetSketchSegmentsCount.html).

## Remarks

Use [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) to get the value for RouteSegmentID.

Call this method before calling [IElectricalRoute::IGetSketchSegments](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute~IGetSketchSegments.html) to determine the size of the array for the sketch segments.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::GetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegments.html)
[IElectricalRoute::GetRouteProperty Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteProperty.html)
[IElectricalRoute::GetRouteSegmentID Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteSegmentID.html)
[IWire::GetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html)
[IWire::IGetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~IGetRouteSegmentIDs.html)
[IWire::GetRouteSegmentIDsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDsCount.html)

## Availability

SOLIDWORKS Routing 2006 FCS
