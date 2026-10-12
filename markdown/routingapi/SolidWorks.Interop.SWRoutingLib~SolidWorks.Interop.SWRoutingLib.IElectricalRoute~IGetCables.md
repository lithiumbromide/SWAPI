---
title: "IGetCables Method (IElectricalRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRoute"
member: "IGetCables"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~IGetCables.html"
---

# IGetCables Method (IElectricalRoute)

Gets the cables in this route.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCables( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRoute
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetCables(Count)
```

### C#

```csharp
System.IntPtr IGetCables(
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetCables(
   [Out] System.int Count
)
```

### Parameters

- `Count`: Number of cables in this electrical route

### Return Value

- in-process, unmanaged C++: Pointer to an array of [cables](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICable.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IElectricalRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute.html)
[IElectricalRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute_members.html)
[IElectricalRoute::GetCables Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~GetCables.html)

## Availability

SOLIDWORKS Routing 2006 FCS
