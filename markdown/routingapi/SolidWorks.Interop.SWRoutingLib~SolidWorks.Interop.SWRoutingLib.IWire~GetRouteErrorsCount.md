---
title: "GetRouteErrorsCount Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "GetRouteErrorsCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteErrorsCount.html"
---

# GetRouteErrorsCount Method (IWire)

Gets the number of errors in this wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteErrorsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.Integer

value = instance.GetRouteErrorsCount()
```

### C#

```csharp
System.int GetRouteErrorsCount()
```

### C++/CLI

```cpp
System.int GetRouteErrorsCount();
```

### Return Value

Number of errors

## VBA Syntax

See [Wire::GetRouteErrorsCount](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~GetRouteErrorsCount.html).

## Remarks

Call this method before calling [IWire::GetRouteErrors](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire~GetRouteErrors.html) to determine the size of the array for the errors.

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::GetRouteErrors Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteErrors.html)

## Availability

SOLIDWORKS Routing 2006 FCS
