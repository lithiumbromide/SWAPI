---
title: "FromComponentReference Property (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "FromComponentReference"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~FromComponentReference.html"
---

# FromComponentReference Property (IWire)

Gets or sets the name of the "from" component reference, the first component to which the wire is connected.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromComponentReference As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.String

instance.FromComponentReference = value

value = instance.FromComponentReference
```

### C#

```csharp
System.string FromComponentReference {get; set;}
```

### C++/CLI

```cpp
property System.String^ FromComponentReference {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the "from" component

## VBA Syntax

See [Wire::FromComponentReference](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~FromComponentReference.html).

## Examples

[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::ToComponentReference Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ToComponentReference.html)
[IElectricalRoute::RouteWires Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRoute~RouteWires.html)

## Availability

SOLIDWORKS Routing 2006 FCS
