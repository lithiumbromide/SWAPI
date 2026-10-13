---
title: "ToPinReference Property (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "ToPinReference"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ToPinReference.html"
---

# ToPinReference Property (IWire)

Gets or sets the pin number or pin name to which the wire is connected.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToPinReference As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.String

instance.ToPinReference = value

value = instance.ToPinReference
```

### C#

```csharp
System.string ToPinReference {get; set;}
```

### C++/CLI

```cpp
property System.String^ ToPinReference {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Pin number or name to which the wire is connected

## VBA Syntax

See [Wire::ToPinReference](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~ToPinReference.html).

## Examples

[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::FromComponentReference Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~FromComponentReference.html)

## Availability

SOLIDWORKS Routing 2006 FCS
