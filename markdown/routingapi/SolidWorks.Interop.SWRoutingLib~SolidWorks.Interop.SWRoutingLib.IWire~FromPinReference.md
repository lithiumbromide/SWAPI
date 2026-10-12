---
title: "FromPinReference Property (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "FromPinReference"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~FromPinReference.html"
---

# FromPinReference Property (IWire)

Gets or sets the "from" pin reference to which the wire is connected.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromPinReference As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.String

instance.FromPinReference = value

value = instance.FromPinReference
```

### C#

```csharp
System.string FromPinReference {get; set;}
```

### C++/CLI

```cpp
property System.String^ FromPinReference {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the "from" pin reference to which the wire is connected

## VBA Syntax

See [Wire::FromPinReference](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~FromPinReference.html).

## Examples

[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::ToPinReference Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ToPinReference.html)

## Availability

SOLIDWORKS Routing 2006 FCS
