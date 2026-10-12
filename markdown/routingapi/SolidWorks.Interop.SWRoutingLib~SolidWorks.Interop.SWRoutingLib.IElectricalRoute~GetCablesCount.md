---
title: "GetCablesCount Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetCablesCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetCablesCount.html"
---

# GetCablesCount Method (IElectricalRoute)

Gets the number of cables in the route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCablesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim value As System.Integer

value = instance.GetCablesCount()
```

### C#

```csharp
System.int GetCablesCount()
```

### C++/CLI

```cpp
System.int GetCablesCount();
```

### Return Value

Number of cables

## VBA Syntax

See [ElectricalRoute::GetCablesCount](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetCablesCount.html).

## Examples

[Get RouteManager and Electrical Route (VBA)](Get_RouteManager_and_Electrical_Route_Example_VB.htm)
[Get Cable Cores (VBA)](Get_Cores_Example_VB.htm)
[Get Cable Cores (VB.NET)](Get_Cores_Example_VBNET.htm)
[Get Cable Cores (C#)](Get_Cores_Example_CSharp.htm)

## Remarks

Call this method before calling [IElectricalRoute::IGetCables](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute~IGetCables.html) to determine the size of the array for the cables for that method.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::GetCables Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetCables.html)

## Availability

SOLIDWORKS Routing 2006 FCS
