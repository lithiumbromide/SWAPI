---
title: "ManufacturingRegion Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "ManufacturingRegion"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~ManufacturingRegion.html"
---

# ManufacturingRegion Property (ISustainabilityManufacturing)

Gets or sets the region of manufacture of the current part.

## Syntax

### Visual Basic (Declaration)

```vb
Property ManufacturingRegion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Integer

instance.ManufacturingRegion = value

value = instance.ManufacturingRegion
```

### C#

```csharp
System.int ManufacturingRegion {get; set;}
```

### C++/CLI

```cpp
property System.int ManufacturingRegion {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Region of manufacture as defined in [swSustainabilityRegionName_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityRegionName_e.html)

## VBA Syntax

See [SustainabilityManufacturing::ManufacturingRegion](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~ManufacturingRegion.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
