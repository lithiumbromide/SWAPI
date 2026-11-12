---
title: "GetSketchSegments Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "GetSketchSegments"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetSketchSegments.html"
---

# GetSketchSegments Method (IElectricalFlatRoute)

Gets all of the SOLIDWORKS sketch segments in the specified route segment for this flattened route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegments( _
   ByVal RouteSegmentID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalFlatRoute
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

- `RouteSegmentID`: Route segment ID (see **Remarks**)

### Return Value

Array of SOLIDWORKS [ISketchSegment](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [ElectricalFlatRoute::GetSketchSegments](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalFlatRoute~GetSketchSegments.html).

## Remarks

Use [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) to get the value for RouteSegmentID.

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)
[IElectricalFlatRoute::GetSketchSegmentsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetSketchSegmentsCount.html)
[IElectricalFlatRoute::IGetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~IGetSketchSegments.html)

## Availability

SOLIDWORKS Routing 2009 FCS
