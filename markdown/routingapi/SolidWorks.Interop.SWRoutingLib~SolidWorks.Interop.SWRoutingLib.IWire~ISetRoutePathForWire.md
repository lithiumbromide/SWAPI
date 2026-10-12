---
title: "ISetRoutePathForWire Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "ISetRoutePathForWire"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ISetRoutePathForWire.html"
---

# ISetRoutePathForWire Method (IWire)

Sets a new route path for this wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetRoutePathForWire( _
   ByVal numRouteSegmentIds As System.Integer, _
   ByRef RouteSegmentIDs As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim numRouteSegmentIds As System.Integer
Dim RouteSegmentIDs As System.Integer
Dim value As System.Integer

value = instance.ISetRoutePathForWire(numRouteSegmentIds, RouteSegmentIDs)
```

### C#

```csharp
System.int ISetRoutePathForWire(
   System.int numRouteSegmentIds,
   ref System.int RouteSegmentIDs
)
```

### C++/CLI

```cpp
System.int ISetRoutePathForWire(
   System.int numRouteSegmentIds,
   System.int% RouteSegmentIDs
)
```

### Parameters

- `numRouteSegmentIds`: Number of route segments in this wire
- `RouteSegmentIDs`: - in-process, unmanaged C++: Pointer to an array of route segment IDs for this wire
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Status of setting a new route path as defined in [swSetRoutePathForWireErrorType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swSetRoutePathForWireErrorType_e.html)

## VBA Syntax

See [Wire::ISetRoutePathForWire](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~ISetRoutePathForWire.html).

## Remarks

This method checks to see if the route segment IDs are valid. If so, then:

- the existing wire path is cleared.
- a new wire path with new route segments is created.

You can pass new route segments by either:

- preselecting the route segments or preselecting two connectors. This method automatically detects the route segments between the two selected connectors.
  - or -
- Passing an array of route segment IDs.

Before calling this method, call [IWire::GetRouteSegmentIDsCount](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDsCount.html) to get numRouteSegmentIDs.

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::SetRoutePathForWire Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~SetRoutePathForWire.html)

## Availability

SOLIDWORKS Routing 2014 FCS
