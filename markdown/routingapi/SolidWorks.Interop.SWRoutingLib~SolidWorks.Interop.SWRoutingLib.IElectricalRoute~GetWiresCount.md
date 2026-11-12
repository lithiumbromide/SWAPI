---
title: "GetWiresCount Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetWiresCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetWiresCount.html"
---

# GetWiresCount Method (IElectricalRoute)

Gets the number of wires in the route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWiresCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim value As System.Integer

value = instance.GetWiresCount()
```

### C#

```csharp
System.int GetWiresCount()
```

### C++/CLI

```cpp
System.int GetWiresCount();
```

### Return Value

Number of wires in the route

## VBA Syntax

See [ElectricalRoute::GetWiresCount](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetWiresCount.html).

## Examples

[Get RouteManager and Electrical Route (VBA)](Get_RouteManager_and_Electrical_Route_Example_VB.htm)
[Get Wires (VBA)](Get_Wires_Example_VB.htm)
[Set New Route Paths for Wires (C#)](Set_New_Route_Paths_for_Wires_Example_CSharp.htm)
[Set New Route Paths for Wires (VB.NET)](Set_New_Route_Paths_for_Wires_Example_VBNET.htm)
[Set New Route Paths for Wires (VBA)](Set_New_Route_Paths_for_Wires_Example_VB.htm)

## Remarks

Call this method before calling [IElectricalRoute::IGetWires](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute~IGetWires.html) to determine the size of the array for the wires for that method.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::GetWires Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetWires.html)

## Availability

SOLIDWORKS Routing 2006 FCS
