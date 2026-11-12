---
title: "GetCables Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "GetCables"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetCables.html"
---

# GetCables Method (IElectricalRoute)

Gets the cables in the route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCables() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim value As System.Object

value = instance.GetCables()
```

### C#

```csharp
System.object GetCables()
```

### C++/CLI

```cpp
System.Object^ GetCables();
```

### Return Value

Array of the [cables](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICable.html)

## VBA Syntax

See [ElectricalRoute::GetCables](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRoute~GetCables.html).

## Examples

[Get Cable Cores (VBA)](Get_Cores_Example_VB.htm)
[Get Cable Cores (VB.NET)](Get_Cores_Example_VBNET.htm)
[Get Cable Cores (C#)](Get_Cores_Example_CSharp.htm)

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::IGetCables Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetCables.html)
[IElectricalRoute::GetCablesCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetCablesCount.html)

## Availability

SOLIDWORKS Routing 2006 FCS
