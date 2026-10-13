---
title: "IGetSketchSegments Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "IGetSketchSegments"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetSketchSegments.html"
---

# IGetSketchSegments Method (IElectricalRoute)

Gets the SOLIDWORKS sketch segments in the specified route segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchSegments( _
   ByVal RouteSegmentID As System.Integer, _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim RouteSegmentID As System.Integer
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetSketchSegments(RouteSegmentID, Count)
```

### C#

```csharp
System.IntPtr IGetSketchSegments(
   System.int RouteSegmentID,
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetSketchSegments(
   System.int RouteSegmentID,
   [Out] System.int Count
)
```

### Parameters

- `RouteSegmentID`: Route segment ID (see Remarks)
- `Count`: Number of SOLIDWORKS sketch segments

### Return Value

- in-process, unmanaged C++: Pointer to an array of SOLIDWORKS [sketch segments](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) to get the value for RouteSegmentID.

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
