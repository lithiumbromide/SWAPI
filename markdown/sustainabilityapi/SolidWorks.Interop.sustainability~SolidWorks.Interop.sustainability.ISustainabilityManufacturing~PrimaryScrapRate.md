---
title: "PrimaryScrapRate Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "PrimaryScrapRate"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~PrimaryScrapRate.html"
---

# PrimaryScrapRate Property (ISustainabilityManufacturing)

Gets or sets the amount of material discarded as scrap while manufacturing the current part.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrimaryScrapRate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Double

instance.PrimaryScrapRate = value

value = instance.PrimaryScrapRate
```

### C#

```csharp
System.double PrimaryScrapRate {get; set;}
```

### C++/CLI

```cpp
property System.double PrimaryScrapRate {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Scrap percentage

## VBA Syntax

See [SustainabilityManufacturing::PrimaryScrapRate](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~PrimaryScrapRate.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
