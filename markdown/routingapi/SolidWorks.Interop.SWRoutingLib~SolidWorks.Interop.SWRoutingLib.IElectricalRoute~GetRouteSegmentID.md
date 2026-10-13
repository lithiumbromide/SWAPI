---
title: "GetRouteSegmentID Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetRouteSegmentID"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteSegmentID.html"
---

# GetRouteSegmentID Method (IElectricalRoute)

Gets the route segment ID for the specified SOLIDWORKS sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteSegmentID( _
   ByVal SketchSegment As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim SketchSegment As System.Object
Dim value As System.Integer

value = instance.GetRouteSegmentID(SketchSegment)
```

### C#

```csharp
System.int GetRouteSegmentID(
   System.object SketchSegment
)
```

### C++/CLI

```cpp
System.int GetRouteSegmentID(
   System.Object^ SketchSegment
)
```

### Parameters

- `SketchSegment`: SOLIDWORKS [sketch segment](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

### Return Value

Route segment ID

## VBA Syntax

See [ElectricalRoute::GetRouteSegmentID](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetRouteSegmentID.html).

## Remarks

If the sketch segment is not a route, then RouteSegmentID is set to -1.

Use [IElectricalRoute::GetSketchSegments](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegments.html) or [IElectricalRoute::IGetSketchSegments](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute~IGetSketchSegments.html) to get the SOLIDWORKS sketch segments.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::GetRouteProperty Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteProperty.html)
[IElectricalRoute::GetSketchSegmentsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegmentsCount.html)
[IWire::GetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html)
[IWire::IGetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~IGetRouteSegmentIDs.html)
[IWire::GetRouteSegmentIDsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDsCount.html)

## Availability

SOLIDWORKS Routing 2006 FCS
