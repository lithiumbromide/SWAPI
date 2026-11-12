---
title: "GetFixedLength Method (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "GetFixedLength"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~GetFixedLength.html"
---

# GetFixedLength Method (IRouteProperty)

Gets the fixed length of a route segment having a fixed length constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFixedLength() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim value As System.Double

value = instance.GetFixedLength()
```

### C#

```csharp
System.double GetFixedLength()
```

### C++/CLI

```cpp
System.double GetFixedLength();
```

### Return Value

Fixed length

## VBA Syntax

See [RouteProperty::GetFixedLength](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~GetFixedLength.html).

## Examples

See the [IRouteProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html) examples.

## Remarks

This method gets lengths only for route segments that have been constrained to have a fixed length in the SOLIDWORKS user interface. To constrain a route segment to have a fixed length, right-click on the route segment and select **Fixed Length**. To change a fixed length, call [IRouteProperty::SetFixedLength](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteProperty~SetFixedLength.html).

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)

## Availability

SOLIDWORKS Routing 2009 SP4
