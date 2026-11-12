---
title: "PrimaryNaturalGas Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "PrimaryNaturalGas"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~PrimaryNaturalGas.html"
---

# PrimaryNaturalGas Property (ISustainabilityManufacturing)

Gets or sets the natural gas used to manufacture the current part.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrimaryNaturalGas As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Double

instance.PrimaryNaturalGas = value

value = instance.PrimaryNaturalGas
```

### C#

```csharp
System.double PrimaryNaturalGas {get; set;}
```

### C++/CLI

```cpp
property System.double PrimaryNaturalGas {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Natural gas usage in BTU/weight units

## VBA Syntax

See [SustainabilityManufacturing::PrimaryNaturalGas](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~PrimaryNaturalGas.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
