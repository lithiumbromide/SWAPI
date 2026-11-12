---
title: "GetRouteProperty Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetRouteProperty"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetRouteProperty.html"
---

# GetRouteProperty Method (IElectricalRoute)

Gets the [IRouteProperty](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteProperty.html) object for the specified route segment ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteProperty( _
   ByVal RouteSegmentID As System.Integer _
) As RouteProperty
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim RouteSegmentID As System.Integer
Dim value As RouteProperty

value = instance.GetRouteProperty(RouteSegmentID)
```

### C#

```csharp
RouteProperty GetRouteProperty(
   System.int RouteSegmentID
)
```

### C++/CLI

```cpp
RouteProperty^ GetRouteProperty(
   System.int RouteSegmentID
)
```

### Parameters

- `RouteSegmentID`: Route segment ID (see **Remarks**)

### Return Value

Pointer to [IRouteProperty](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteProperty.html) object

## VBA Syntax

See [ElectricalRoute::GetRouteProperty](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetRouteProperty.html).

## Examples

See the [IElectricalRoute](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html) examples.

## Remarks

To get the value for RouteSegmentID, call [IWire::GetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteSegmentIDs.html) or [IWire::IGetRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~IGetRouteSegmentIDs.html) before calling this method.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
