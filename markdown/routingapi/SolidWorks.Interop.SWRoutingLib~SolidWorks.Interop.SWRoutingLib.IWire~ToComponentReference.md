---
title: "ToComponentReference Property (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "ToComponentReference"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ToComponentReference.html"
---

# ToComponentReference Property (IWire)

Gets or sets the name of the "to" component reference, the second component to which the wire is connected.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToComponentReference As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.String

instance.ToComponentReference = value

value = instance.ToComponentReference
```

### C#

```csharp
System.string ToComponentReference {get; set;}
```

### C++/CLI

```cpp
property System.String^ ToComponentReference {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the "to" component

## VBA Syntax

See [Wire::ToComponentReference](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~ToComponentReference.html).

## Examples

[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::FromComponentReference Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~FromComponentReference.html)
[IElectricalWire::RouteWires Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~RouteWires.html)

## Availability

SOLIDWORKS Routing 2006 FCS
