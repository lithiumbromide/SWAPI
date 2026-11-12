---
title: "IGetRouteErrors Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "IGetRouteErrors"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~IGetRouteErrors.html"
---

# IGetRouteErrors Method (IWire)

Gets the errors in the wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRouteErrors( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetRouteErrors(Count)
```

### C#

```csharp
System.IntPtr IGetRouteErrors(
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetRouteErrors(
   [Out] System.int Count
)
```

### Parameters

- `Count`: Number of errors

### Return Value

- in-process, unmanaged C++: Pointer to an array of errors as defined in [swWireRouteError_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swWireRouteError_e.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IWire::GetRouteErrorsCount](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteErrorsCount.html) before calling this method to determine the size of the return value array.

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::GetRouteErrors Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteErrors.html)

## Availability

SOLIDWORKS Routing 2006 FCS
