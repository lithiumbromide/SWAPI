---
title: "SubType Property (IElectricalRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRouteProperty"
member: "SubType"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty~SubType.html"
---

# SubType Property (IElectricalRouteProperty)

Gets or sets the electrical route subtype.

## Syntax

### Visual Basic (Declaration)

```vb
Property SubType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRouteProperty
Dim value As System.Integer

instance.SubType = value

value = instance.SubType
```

### C#

```csharp
System.int SubType {get; set;}
```

### C++/CLI

```cpp
property System.int SubType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Electrical route subtype as defined in [swElectricalRouteSubType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swElectricalRouteSubType_e.html)

## VBA Syntax

See [ElectricalRouteProperty::SubType](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRouteProperty~SubType.html).

## See Also

[IElectricalRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty.html)
[IElectricalRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
