---
title: "GetWires Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetWires"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetWires.html"
---

# GetWires Method (IElectricalRoute)

Gets the wires in the route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWires() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim value As System.Object

value = instance.GetWires()
```

### C#

```csharp
System.object GetWires()
```

### C++/CLI

```cpp
System.Object^ GetWires();
```

### Return Value

Array of [wires](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire.html)

## VBA Syntax

See [ElectricalRoute::GetWires](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetWires.html).

## Examples

[Get Wires (VBA)](Get_Wires_Example_VB.htm)
[Get Wires, Sketch Segments, and Sketches (VBA)](Get_Wires_Sketch_Segments_and_Sketches_Example_VB.htm)
[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)
[Set New Route Paths for Wires (C#)](Set_New_Route_Paths_for_Wires_Example_CSharp.htm)
[Set New Route Paths for Wires (VB.NET)](Set_New_Route_Paths_for_Wires_Example_VBNET.htm)
[Set New Route Paths for Wires (VBA)](Set_New_Route_Paths_for_Wires_Example_VB.htm)

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::IGetWires Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetWires.html)
[IElectricalRoute::GetWiresCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetWiresCount.html)

## Availability

SOLIDWORKS Routing 2006 FCS
