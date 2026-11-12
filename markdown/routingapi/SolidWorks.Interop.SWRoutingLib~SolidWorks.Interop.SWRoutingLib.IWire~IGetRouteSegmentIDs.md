---
title: "IGetRouteSegmentIDs Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "IGetRouteSegmentIDs"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~IGetRouteSegmentIDs.html"
---

# IGetRouteSegmentIDs Method (IWire)

Gets the route segment IDs in this wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRouteSegmentIDs( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetRouteSegmentIDs(Count)
```

### C#

```csharp
System.IntPtr IGetRouteSegmentIDs(
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetRouteSegmentIDs(
   [Out] System.int Count
)
```

### Parameters

- `Count`: Number of route segment IDs

### Return Value

- in-process, unmanaged C++: Pointer to an array of route segment IDs for the wire
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IWire::GetRouteSegmentIDsCount](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDsCount.html) to get Count.

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::GetRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html)
[IElectricalRoute::GetRouteProperty Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteProperty.html)
[IElectricalRoute::GetRouteSegmentID Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteSegmentID.html)
[IElectricalRoute::GetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegments.html)
[IElectricalRoute::GetSketchSegmentsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetSketchSegmentsCount.html)
[IElectricalRoute::IGetSketchSegments Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetSketchSegments.html)

## Availability

SOLIDWORKS Routing 2006 FCS
