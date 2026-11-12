---
title: "RouteWires Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "RouteWires"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~RouteWires.html"
---

# RouteWires Method (IElectricalRoute)

Route all wires that are not already routed or that have errors in their path, using a from-to list.

## Syntax

### Visual Basic (Declaration)

```vb
Function RouteWires() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim value As System.Boolean

value = instance.RouteWires()
```

### C#

```csharp
System.bool RouteWires()
```

### C++/CLI

```cpp
System.bool RouteWires();
```

### Return Value

True if the some or all wires are routed, false if not (see Remarks)

## VBA Syntax

See [ElectricalRoute::RouteWires](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~RouteWires.html).

## Examples

[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)

## Remarks

Wires are routed if the "from" and "to" component references are defined and if there is a valid path in the route from the "from" and "to" components.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)

## Availability

SOLIDWORKS Routing 2006 FCS
