---
title: "IGetWires Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "IGetWires"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetWires.html"
---

# IGetWires Method (IElectricalRoute)

Gets the wires in the route.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetWires( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetWires(Count)
```

### C#

```csharp
System.IntPtr IGetWires(
   ref System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetWires(
   System.int% Count
)
```

### Parameters

- `Count`: Number of wires in the route

### Return Value

- in-process, unmanaged C++: Pointer to an array of [wires](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IElectricalRoute::GetWiresCount](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute~GetWiresCount.html) before calling this method to determine the size of the array for the wires.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::GetWires Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetWires.html)

## Availability

SOLIDWORKS Routing 2006 FCS
