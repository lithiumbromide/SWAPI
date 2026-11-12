---
title: "GetRouteErrors Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "GetRouteErrors"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteErrors.html"
---

# GetRouteErrors Method (IWire)

Gets the errors in the wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteErrors() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.Object

value = instance.GetRouteErrors()
```

### C#

```csharp
System.object GetRouteErrors()
```

### C++/CLI

```cpp
System.Object^ GetRouteErrors();
```

### Return Value

Array of errors as defined in [swWireRouteError_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swWireRouteError_e.html)

## VBA Syntax

See [Wire::GetRouteErrors](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~GetRouteErrors.html).

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::IGetRouteErrors Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~IGetRouteErrors.html)
[IWire::GetRouteErrorsCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetRouteErrorsCount.html)

## Availability

SOLIDWORKS Routing 2006 FCS
