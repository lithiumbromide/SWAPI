---
title: "SetRoutePathForWire Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "SetRoutePathForWire"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~SetRoutePathForWire.html"
---

# SetRoutePathForWire Method (IWire)

Sets a new route path for this wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRoutePathForWire( _
   ByVal RouteSegmentIDs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim RouteSegmentIDs As System.Object
Dim value As System.Integer

value = instance.SetRoutePathForWire(RouteSegmentIDs)
```

### C#

```csharp
System.int SetRoutePathForWire(
   System.object RouteSegmentIDs
)
```

### C++/CLI

```cpp
System.int SetRoutePathForWire(
   System.Object^ RouteSegmentIDs
)
```

### Parameters

- `RouteSegmentIDs`: Array of route segment IDs (see **Remarks**)

### Return Value

Status of setting a new route path as defined in [swSetRoutePathForWireErrorType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swSetRoutePathForWireErrorType_e.html)

## VBA Syntax

See [Wire::SetRoutePathForWire](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~SetRoutePathForWire.html).

## Examples

[Set New Route Paths for Wires (C#)](Set_New_Route_Paths_for_Wires_Example_CSharp.htm)
[Set New Route Paths for Wires (VB.NET)](Set_New_Route_Paths_for_Wires_Example_VBNET.htm)
[Set New Route Paths for Wires (VBA)](Set_New_Route_Paths_for_Wires_Example_VB.htm)

## Remarks

This method checks to see if the route segment IDs are valid. If so, then the existing wire path is cleared and a new wire path with new route segments is created.

You can pass new route segments by either:

- preselecting the route segments or preselecting two connectors. This method automatically detects the route segments between the two selected connectors.
  - or -
- Passing an array of route segment IDs.

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::ISetRoutePathForWire Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ISetRoutePathForWire.html)

## Availability

SOLIDWORKS Routing 2014 FCS
