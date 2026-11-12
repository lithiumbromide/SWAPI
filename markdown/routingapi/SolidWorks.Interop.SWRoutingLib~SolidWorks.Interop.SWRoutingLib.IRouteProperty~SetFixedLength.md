---
title: "SetFixedLength Method (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "SetFixedLength"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~SetFixedLength.html"
---

# SetFixedLength Method (IRouteProperty)

Changes the length of a fixed-length route segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFixedLength( _
   ByVal NewLength As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim NewLength As System.Double
Dim value As System.Integer

value = instance.SetFixedLength(NewLength)
```

### C#

```csharp
System.int SetFixedLength(
   System.double NewLength
)
```

### C++/CLI

```cpp
System.int SetFixedLength(
   System.double NewLength
)
```

### Parameters

- `NewLength`: Fixed length

### Return Value

Fixed length error code as defined in [swSetRouteFixedLengthError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetRouteFixedLengthError_e.html)

## VBA Syntax

See [RouteProperty::SetFixedLength](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~SetFixedLength.html).

## Examples

See the [IRouteProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html) examples.

## Remarks

This method changes lengths only for route segments that have been constrained to have a fixed length in the SOLIDWORKS user interface. To constrain a route segment to a fixed length, right-click on the route segment and select **Fixed Length**.

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)
[IRouteProperty::GetFixedLength Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~GetFixedLength.html)

## Availability

SOLIDWORKS Routing 2009 SP4
