---
title: "PrimaryElectricity Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "PrimaryElectricity"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~PrimaryElectricity.html"
---

# PrimaryElectricity Property (ISustainabilityManufacturing)

Gets or sets the electricity used to manufacture the current part.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrimaryElectricity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Double

instance.PrimaryElectricity = value

value = instance.PrimaryElectricity
```

### C#

```csharp
System.double PrimaryElectricity {get; set;}
```

### C++/CLI

```cpp
property System.double PrimaryElectricity {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Electricity usage in kilowatt-hours/weight units

## VBA Syntax

See [SustainabilityManufacturing::PrimaryElectricity](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~PrimaryElectricity.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
