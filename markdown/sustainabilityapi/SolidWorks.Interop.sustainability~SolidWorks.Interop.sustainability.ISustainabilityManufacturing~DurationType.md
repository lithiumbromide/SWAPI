---
title: "DurationType Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "DurationType"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~DurationType.html"
---

# DurationType Property (ISustainabilityManufacturing)

Gets or sets the units of time that the part is built to last.

## Syntax

### Visual Basic (Declaration)

```vb
Property DurationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Integer

instance.DurationType = value

value = instance.DurationType
```

### C#

```csharp
System.int DurationType {get; set;}
```

### C++/CLI

```cpp
property System.int DurationType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units for [ISustainabilityManufacturing::BuiltToLast](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing~BuiltToLast.html) as defined in [swSustainabilityDurationType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityDurationType_e.html)

## VBA Syntax

See [SustainabilityManufacturing::DurationType](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~DurationType.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
