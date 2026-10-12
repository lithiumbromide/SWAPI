---
title: "IGetSketchSegments Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "IGetSketchSegments"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~IGetSketchSegments.html"
---

# IGetSketchSegments Method (IElectricalFlatRoute)

Gets all of the SOLIDWORKS sketch segments in the specified route segment for this flattened route.

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
Dim instance As IElectricalFlatRoute
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

ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html

## Remarks

Call [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) to get the value for RouteSegmentID.

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)
[IElectricalFlatRoute::GetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetSketchSegments.html)

## Availability

SOLIDWORKS Routing 2009 FCS
