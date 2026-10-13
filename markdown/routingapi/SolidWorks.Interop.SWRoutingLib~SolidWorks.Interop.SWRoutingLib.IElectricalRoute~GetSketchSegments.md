---
title: "GetSketchSegments Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetSketchSegments"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegments.html"
---

# GetSketchSegments Method (IElectricalRoute)

Gets the SOLIDWORKS sketch segments in the route segment using the specified route segment ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegments( _
   ByVal RouteSegmentID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim RouteSegmentID As System.Integer
Dim value As System.Object

value = instance.GetSketchSegments(RouteSegmentID)
```

### C#

```csharp
System.object GetSketchSegments(
   System.int RouteSegmentID
)
```

### C++/CLI

```cpp
System.Object^ GetSketchSegments(
   System.int RouteSegmentID
)
```

### Parameters

- `RouteSegmentID`: Route segment ID (see Remarks)

### Return Value

Array of SOLIDWORKS [sketch segments](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [ElectricalRoute::GetSketchSegments](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetSketchSegments.html).

## Examples

[Get Wires, Sketch Segments, and Sketches (VBA)](Get_Wires_Sketch_Segments_and_Sketches_Example_VB.htm)

## Remarks

Use [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) to get the value for RouteSegmentID.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::IGetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetSketchSegments.html)
[IElectricalRoute::GetSketchSegmentsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegmentsCount.html)
[IElectricalRoute::GetRouteProperty Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteProperty.html)
[IElectricalRoute::GetRouteSegmentID Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteSegmentID.html)
[IWire::GetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html)
[IWire::IGetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~IGetRouteSegmentIDs.html)
[IWire::GetRouteSegmentIDsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDsCount.html)

## Availability

SOLIDWORKS Routing 2006 FCS
