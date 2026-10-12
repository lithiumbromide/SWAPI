---
title: "Color Property (IWireProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IWireProperty"
member: "Color"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWireProperty~Color.html"
---

# Color Property (IWireProperty)

Gets the color of the wire.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWireProperty
Dim value As System.Integer

value = instance.Color
```

### C#

```csharp
System.int Color {get;}
```

### C++/CLI

```cpp
property System.int Color {
   System.int get();
}
```

### Property Value

COLORREF value

## VBA Syntax

See [WireProperty::Color](ms-its:routingapivb6.chm::/SWRoutingLib~WireProperty~Color.html).

## Examples

See the [IWireProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWireProperty.html) examples.

## See Also

[IWireProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWireProperty.html)
[IWireProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWireProperty_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
