---
title: "SurfaceArea Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "SurfaceArea"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~SurfaceArea.html"
---

# SurfaceArea Property (ISustainabilityManufacturing)

Gets the surface area for manufacturing the current part.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SurfaceArea As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Double

value = instance.SurfaceArea
```

### C#

```csharp
System.double SurfaceArea {get;}
```

### C++/CLI

```cpp
property System.double SurfaceArea {
   System.double get();
}
```

### Property Value

Surface area in square length units

## VBA Syntax

See [SustainabilityManufacturing::SurfaceArea](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~SurfaceArea.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
